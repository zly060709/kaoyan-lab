/* kaoyan-lab service worker — 版本化缓存，更新后页面提示刷新 */
const VER = "kaoyan-v0.3.6";
const CORE = ["index.html", "diag.html", "404.html", "manifest.webmanifest", "assets/icon.svg"];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(VER).then((c) => Promise.allSettled(CORE.map((u) => c.add(u)))).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== VER).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  const u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  // 数据与第三方库：stale-while-revalidate（离线可用，在线时后台更新）
  if (u.pathname.includes("/data/") || u.pathname.includes("/vendor/")) {
    e.respondWith(
      caches.open(VER).then(async (c) => {
        const hit = await c.match(e.request);
        const net = fetch(e.request)
          .then((r) => { if (r && r.ok) c.put(e.request, r.clone()); return r; })
          .catch(() => hit);
        return hit || net;
      })
    );
    return;
  }
  // 核心页面：network-first，失败回退缓存，导航失败回退 index（刷新不白屏）
  e.respondWith(
    fetch(e.request)
      .then((r) => {
        if (r && r.ok) { const cp = r.clone(); caches.open(VER).then((c) => c.put(e.request, cp)); }
        return r;
      })
      .catch(() =>
        caches.match(e.request).then((h) => h || (e.request.mode === "navigate" ? caches.match("index.html") : undefined))
      )
  );
});
