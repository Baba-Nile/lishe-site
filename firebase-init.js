/* Lazy Firebase loader. The SDK is only downloaded on pages/sections that need Firestore,
   so it never blocks first paint. Uses the existing LISHE_FIREBASE_CONFIG from firebase-config.js. */
(function () {
  'use strict';
  var SDK = 'https://www.gstatic.com/firebasejs/10.12.0/';
  var promise = null;

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = src; s.async = false;
      s.onload = resolve; s.onerror = function () { reject(new Error('Failed to load ' + src)); };
      document.head.appendChild(s);
    });
  }

  function db() {
    if (promise) return promise;
    promise = loadScript('firebase-config.js')
      .then(function () { return loadScript(SDK + 'firebase-app-compat.js'); })
      .then(function () { return loadScript(SDK + 'firebase-firestore-compat.js'); })
      .then(function () {
        // firebase-config.js declares a top-level const, which is global but not a window property
        if (!window.firebase.apps.length) window.firebase.initializeApp(LISHE_FIREBASE_CONFIG);
        return window.firebase.firestore();
      });
    promise.catch(function () { promise = null; });
    return promise;
  }

  // Run callback when `el` is near the viewport (or immediately if IntersectionObserver is missing)
  function whenNear(el, cb) {
    if (!el) return;
    if (!('IntersectionObserver' in window)) { cb(); return; }
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); cb(); }
    }, { rootMargin: '600px 0px' });
    io.observe(el);
  }

  function esc(v) {
    return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }

  window.LisheFirebase = { db: db, whenNear: whenNear, esc: esc };
})();
