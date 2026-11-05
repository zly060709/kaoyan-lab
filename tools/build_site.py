# -*- coding: utf-8 -*-
"""构建加密发布目录（dist/）：白名单拷贝 + data/**/* 全量 AES-256-GCM 加密。

合规口径（见 about.html 与优化清单「合规决策」）：站点为个人学习库，
内容层整体加密、口令不进仓库（GitHub Actions Secret KYL_PASS / 本地 .auth/site_pass.txt），
加密密文与口令分离；robots.txt 全站 Disallow + 每页 noindex，不生成 sitemap。

密码学口径：
  key = PBKDF2-HMAC-SHA256(password, salt, 310000, 32B)          —— salt 公开（tools/enc_salt.hex）
  每文件 iv = sha256("{path}|{sha256(plain)}|{salt}")[:12]        —— 内容寻址确定性 IV：
      同一文件内容不变 ⇒ iv 与密文均不变（跨构建/跨 SW 缓存一致）；
      内容变化 ⇒ iv 随之变化，无 (key, iv) 复用加密不同明文的情形。
  blob 文件名 = sha256(plain)[:16].bin                            —— 内容寻址，天然去重
  verify = AESGCM(key, 随机 iv, b"kaoyan-lab-v1")                 —— 解锁口令校验
用法:
  python -I -X utf8 tools/build_site.py --dist dist               # 口令取 KYL_PASS 环境变量
  python -I -X utf8 tools/build_site.py --dist dist --password-file .auth/site_pass.txt
"""
import argparse, base64, hashlib, io, json, os, shutil, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERIFY_PLAIN = b"kaoyan-lab-v1"
KDF_ITER = 310000

# 部署白名单（A06）：内部文档 / legacy / 工具 / 明文数据一律不进发布目录
ROOT_FILES = ["index.html", "lab3d.html", "diag.html", "404.html", "about.html", "robots.txt",
              "manifest.webmanifest", "sw.js", ".nojekyll"]
ROOT_DIRS = ["assets"]
VENDOR_FILES = [
    "vendor/katex/katex.min.js",
    "vendor/katex/katex.min.css",
    "vendor/katex/contrib/auto-render.min.js",
    "vendor/three.min.js",
    "vendor/OrbitControls.js",
]
VENDOR_FONT_EXT = (".woff2",)


def enc_salt():
    return open(os.path.join(ROOT, "tools", "enc_salt.hex"), encoding="utf-8").read().strip()


def derive_key_bytes(password: str, salt: bytes) -> bytes:
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=KDF_ITER)
    return kdf.derive(password.encode("utf-8"))


def content_iv(path: str, plain_sha_hex: str, salt_hex: str) -> bytes:
    h = hashlib.sha256(f"{path}|{plain_sha_hex}|{salt_hex}".encode("utf-8")).digest()
    return h[:12]


def collect_data_files():
    out = []
    for dirpath, _dirnames, filenames in os.walk(os.path.join(ROOT, "data")):
        for fn in filenames:
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, ROOT).replace("\\", "/")
            out.append(rel)
    return sorted(out)


def build(dist: str, password: str):
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    salt_hex = enc_salt()
    salt = bytes.fromhex(salt_hex)
    key = derive_key_bytes(password, salt)
    aes = AESGCM(key)

    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)

    # 1) 白名单根文件与目录
    for f in ROOT_FILES:
        src = os.path.join(ROOT, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dist, f))
    for d in ROOT_DIRS:
        src = os.path.join(ROOT, d)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dist, d))
    # 2) vendor 瘦身（E02：只带 min 版与 woff2 字体）
    for rel in VENDOR_FILES:
        src = os.path.join(ROOT, rel)
        if os.path.exists(src):
            dst = os.path.join(dist, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    fonts_src = os.path.join(ROOT, "vendor", "katex", "fonts")
    if os.path.isdir(fonts_src):
        fonts_dst = os.path.join(dist, "vendor", "katex", "fonts")
        os.makedirs(fonts_dst, exist_ok=True)
        for fn in os.listdir(fonts_src):
            if fn.endswith(VENDOR_FONT_EXT):
                shutil.copy2(os.path.join(fonts_src, fn), os.path.join(fonts_dst, fn))

    # 3) 全量加密 data/**
    files_meta = {}
    total_plain = 0
    enc_dir = os.path.join(dist, "enc")
    os.makedirs(enc_dir, exist_ok=True)
    for rel in collect_data_files():
        plain = open(os.path.join(ROOT, rel), "rb").read()
        total_plain += len(plain)
        sha = hashlib.sha256(plain).hexdigest()
        blob_name = sha[:16] + ".bin"
        iv = content_iv(rel, sha, salt_hex)
        ct = aes.encrypt(iv, plain, None)
        with open(os.path.join(enc_dir, blob_name), "wb") as f:
            f.write(ct)
        files_meta[rel] = {"f": blob_name, "iv": iv.hex(), "len": len(ct)}
    # 4) 口令校验块
    v_iv = os.urandom(12)
    v_ct = aes.encrypt(v_iv, VERIFY_PLAIN, None)
    manifest = {
        "v": 1,
        "kdf": {"salt": salt_hex, "iter": KDF_ITER, "bits": 256},
        "verify": {"iv": v_iv.hex(), "ct": base64.b64encode(v_ct).decode()},
        "files": files_meta,
    }
    with open(os.path.join(enc_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, separators=(",", ":"))

    n = len(files_meta)
    dist_mb = sum(
        os.path.getsize(os.path.join(dp, fn)) / 1e6
        for dp, _, fns in os.walk(dist) for fn in fns
    )
    print(f"dist/ 构建完成：加密 {n} 个内容文件（明文 {total_plain/1e6:.1f} MB），"
          f"发布目录 {dist_mb:.1f} MB；blob 去重后 {len(os.listdir(enc_dir)) - 1} 个密文文件")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default="dist")
    ap.add_argument("--password-env", default="KYL_PASS")
    ap.add_argument("--password-file", default=None)
    args = ap.parse_args()
    password = os.environ.get(args.password_env, "")
    if not password and args.password_file and os.path.exists(args.password_file):
        password = open(args.password_file, encoding="utf-8").read().strip()
    if not password:
        print("缺少口令：设置环境变量 KYL_PASS 或传 --password-file", file=sys.stderr)
        return 2
    build(args.dist, password)
    return 0


if __name__ == "__main__":
    sys.exit(main())
