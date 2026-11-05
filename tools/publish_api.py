# -*- coding: utf-8 -*-
"""用 GitHub Data API（blob→tree→commit→ref）发布工作副本，绕过本机坏掉的 git pack 通道。

只上传与远端 tree 内容不同的文件，其余由 base_tree 继承，因此工作副本可以是部分检出。
token 只从环境变量 GH_TOKEN 读取，不打印、不落盘。

用法：
  GH_TOKEN=... python tools/publish_api.py --root <工作副本> -m "提交信息" [--dry-run] [--only 前缀]
"""
import base64
import hashlib
import io
import json
import os
import sys
import urllib.request

API = "https://api.github.com"
REPO = "zly060709/kaoyan-lab"
SKIP_DIRS = {"__pycache__", ".git", ".idea"}


def die(msg):
    print("失败:", msg)
    sys.exit(1)


def gh(path, method="GET", payload=None, tries=4):
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Authorization", "Bearer " + os.environ["GH_TOKEN"])
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, data) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # 本机链路会把大响应截断（IncompleteRead）
            last = e
    raise last


def git_hash(blob):
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(blob))
    h.update(blob)
    return h.hexdigest()


def local_files(root):
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, root).replace("\\", "/")
            out[rel] = p
    return out


def main():
    args = sys.argv[1:]
    root = args[args.index("--root") + 1] if "--root" in args else None
    msg = args[args.index("-m") + 1] if "-m" in args else None
    dry = "--dry-run" in args
    only = args[args.index("--only") + 1] if "--only" in args else None
    if not root or not msg:
        die("需要 --root 与 -m")
    if not os.environ.get("GH_TOKEN"):
        die("环境变量 GH_TOKEN 未设置")

    ref = gh("/repos/%s/git/ref/heads/main" % REPO)
    head_sha = ref["object"]["sha"]
    commit = gh("/repos/%s/git/commits/%s" % (REPO, head_sha))
    base_tree = commit["tree"]["sha"]

    known = {}
    tc = args[args.index("--tree-cache") + 1] if "--tree-cache" in args else None
    tree = None
    if tc and os.path.exists(tc):
        cached = json.load(io.open(tc, encoding="utf-8"))
        if cached.get("sha") == head_sha:
            tree = {"tree": cached["tree"], "truncated": False}
            print("远端 tree 用本地缓存", tc)
    if tree is None:
        tree = gh("/repos/%s/git/trees/%s?recursive=1" % (REPO, base_tree))
    for e in tree.get("tree", []):
        if e["type"] == "blob":
            known[e["path"]] = (e["sha"], e.get("mode", "100644"))
    if tree.get("truncated"):
        die("远端 tree 被截断，无法安全比对")

    locals_ = local_files(root)
    changed = []
    for rel, p in sorted(locals_.items()):
        if only and not rel.startswith(only):
            continue
        blob = io.open(p, "rb").read()
        sha = git_hash(blob)
        if rel in known and known[rel][0] == sha:
            continue
        changed.append((rel, p, sha, known.get(rel, (None, "100644"))[1], blob))
    print("工作副本 %d 个文件，与远端不同的 %d 个" % (len(locals_), len(changed)))
    for rel, _, _, _, b in changed:
        print("   %s  %dKB" % (rel, len(b) // 1024))
    if dry or not changed:
        return

    entries = []
    for i, (rel, _, sha, mode, blob) in enumerate(changed):
        got = gh("/repos/%s/git/blobs" % REPO, "POST",
                 {"content": base64.b64encode(blob).decode(), "encoding": "base64"})["sha"]
        if got != sha:
            die("%s 回传 sha 与本地 git hash 不一致" % rel)
        entries.append({"path": rel, "mode": mode if rel in known else "100644",
                        "type": "blob", "sha": sha})
        print("  [%d/%d] %s" % (i + 1, len(changed), rel))

    nt = gh("/repos/%s/git/trees" % REPO, "POST",
            {"base_tree": base_tree, "tree": entries})["sha"]
    nc = gh("/repos/%s/git/commits" % REPO, "POST",
            {"message": msg, "tree": nt, "parents": [head_sha]})["sha"]
    gh("/repos/%s/git/refs/heads/main" % REPO, "PATCH", {"sha": nc})
    print("已推送 commit", nc[:8], "tree", nt[:8], "（文件 %d 个）" % len(changed))


if __name__ == "__main__":
    main()
