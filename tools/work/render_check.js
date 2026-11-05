// 用仓库自带的 KaTeX 把 data/math3/*.json 里所有 $…$ 片段真渲染一遍。
// 合同第 7 章要求「LaTeX 公式渲染失败数 = 0」，此前只在浏览器里抽查过，这里做全量静态验证。
// 用法：node tools/work/render_check.js [subject]   （默认 math3）
const fs = require("fs"), path = require("path");
const katex = require(path.join(__dirname, "..", "..", "vendor", "katex", "katex.js"));
const root = path.join(__dirname, "..", "..");
const subject = process.argv[2] || "math3";
const dir = path.join(root, "data", subject);

let files = fs.readdirSync(dir).filter(f => f.endsWith(".json") && /^\d{4}/.test(f)).sort();
let segs = 0, fails = [];
for (const f of files) {
  const doc = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  for (const q of doc.questions || []) {
    const texts = [["stem", q.stem], ["answer", q.answer]]
      .concat((q.options || []).map((o, i) => ["opt" + (i + 1), o]))
      .concat((q.source_blocks || []).map((b, i) => ["block" + i, b.text]));
    for (const [name, t] of texts) {
      if (typeof t !== "string") continue;
      // 整段必须整体捕获：写成 /\$([^$]|\\\$)+?\$/ 时捕获组只留最后一个字符
      for (const m of t.matchAll(/\$((?:[^$]|\\\$)+?)\$/g)) {
        segs++;
        try {
          katex.renderToString(m[1], { throwOnError: true, displayMode: false });
        } catch (e) {
          fails.push(`${q.id} ${name}: ${String(e.message).slice(0, 90)} :: ${m[1].slice(0, 60)}`);
        }
      }
    }
  }
}
console.log(`[${subject}] ${files.length} 个年份文件，${segs} 个 $…$ 片段，渲染失败 ${fails.length}`);
fails.slice(0, 25).forEach(x => console.log("  FAIL", x));
