/* kaoyan-lab service worker v0.5.0
   双缓存桶（A12/E07）：
   - kyl-core-<VER>  核心壳（版本化，升级即清）：页面 + KaTeX
   - kyl-content     内容层（跨版本保留）：data/ enc/ vendor/ —— 升级不清，离线可用不缩水
   策略：内容 SWR；核心页 network-first（1.5s 竞速回缓存）；enc/manifest.json 始终走网络。 */
const VER = "kyl-0.5.4";
const CORE = "kyl-core-" + VER;
const CONTENT = "kyl-content";
const CORE_FILES = [
  "index.html", "diag.html", "404.html", "lab3d.html", "robots.txt",
  "manifest.webmanifest", "assets/icon.svg",
  "vendor/katex/katex.min.css", "vendor/katex/katex.min.js",
  "vendor/katex/contrib/auto-render.min.js",
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CORE).then((c) => Promise.allSettled(CORE_FILES.map((u) => c.add(u)))).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k.startsWith("kyl-core-") && k !== CORE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("message", (e) => {
  if (e.data && e.data.type === "VERSION" && e.source) e.source.postMessage({ type: "VERSION", ver: VER });
});

function timeoutFetch(request, ms) {
  return new Promise((resolve) => {
    const ctl = new AbortController();
    const t = setTimeout(() => ctl.abort(), ms);
    fetch(request, { signal: ctl.signal })
      .then((r) => { clearTimeout(t); resolve(r); })
      .catch(() => { clearTimeout(t); resolve(undefined); });
  });
}

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  const u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  const p = u.pathname;

  if (p.endsWith("/enc/manifest.json")) {
    e.respondWith(
      fetch(e.request).then((r) => {
        if (r && r.ok) { const cp = r.clone(); caches.open(CONTENT).then((c) => c.put(e.request, cp)); }
        return r;
      }).catch(() => caches.match(e.request))
    );
    return;
  }
  if (p.includes("/data/") || p.includes("/enc/") || p.includes("/vendor/")) {
    e.respondWith(
      caches.open(CONTENT).then(async (c) => {
        const hit = await c.match(e.request);
        const net = fetch(e.request)
          .then((r) => { if (r && r.ok) c.put(e.request, r.clone()); return r; })
          .catch(() => hit);
        return hit || net;
      })
    );
    return;
  }
  e.respondWith(
    (async () => {
      const net = await timeoutFetch(e.request, 1500);
      if (net && net.ok) { const cp = net.clone(); caches.open(CORE).then((c) => c.put(e.request, cp)); return net; }
      const hit = await caches.match(e.request);
      if (hit) return hit;
      if (e.request.mode === "navigate") {
        const ih = await caches.match("index.html");
        if (ih) return ih;
      }
      return net || new Response("离线且无缓存", { status: 503 });
    })()
  );
});
