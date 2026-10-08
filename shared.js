/* Lishe Kwa Mtoto — shared behaviour
   Navigation and footer are rendered as static HTML on every page.
   This file only adds behaviour: menu, reveal, counters, hero video, lightbox, filters, analytics. */
(function () {
  'use strict';
  var doc = document;
  doc.documentElement.classList.add('js');
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Analytics (unchanged property) ---- */
  var ga = doc.createElement('script');
  ga.async = true;
  ga.src = 'https://www.googletagmanager.com/gtag/js?id=G-SPJJ708ZR6';
  doc.head.appendChild(ga);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', 'G-SPJJ708ZR6');
  window.gtag = gtag;

  /* ---- Mobile menu ---- */
  var toggle = doc.getElementById('navToggle');
  var panel = doc.getElementById('mobileNav');
  function setMenu(open) {
    if (!toggle || !panel) return;
    panel.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    toggle.querySelector('i').className = open ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
    doc.body.classList.toggle('menu-open', open);
    if (open) { panel.removeAttribute('inert'); } else { panel.setAttribute('inert', ''); }
  }
  if (toggle && panel) {
    panel.setAttribute('inert', '');
    toggle.addEventListener('click', function () { setMenu(!panel.classList.contains('is-open')); });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('is-open')) { setMenu(false); toggle.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 1100) setMenu(false); });
  }

  /* ---- Desktop dropdowns (click for touch/keyboard; hover handled in CSS) ---- */
  doc.querySelectorAll('.nav__trigger').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var item = btn.closest('.nav__item');
      var open = !item.classList.contains('is-open');
      doc.querySelectorAll('.nav__item.is-open').forEach(function (i) { i.classList.remove('is-open'); i.querySelector('.nav__trigger').setAttribute('aria-expanded', 'false'); });
      item.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  doc.addEventListener('click', function () {
    doc.querySelectorAll('.nav__item.is-open').forEach(function (i) { i.classList.remove('is-open'); i.querySelector('.nav__trigger').setAttribute('aria-expanded', 'false'); });
  });
  doc.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') doc.querySelectorAll('.nav__item.is-open').forEach(function (i) { i.classList.remove('is-open'); });
  });

  /* ---- Reveal on scroll ---- */
  var reveals = doc.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- Counters (final value is in the HTML, so no-JS still shows it) ---- */
  var counters = doc.querySelectorAll('[data-count]');
  function runCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1600, t0 = null;
    function frame(t) {
      if (t0 === null) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  if ('IntersectionObserver' in window && !reduceMotion) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { runCounter(en.target); cio.unobserve(en.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---- Home hero video ---- */
  var hero = doc.querySelector('[data-hero]');
  if (hero) {
    var video = hero.querySelector('.hero__video');
    var pauseBtn = hero.querySelector('.hero__pause');
    var conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection || {};
    var slow = conn.saveData || /(^|-)2g$/.test(conn.effectiveType || '');
    var allow = video && !reduceMotion && !slow;
    if (allow) {
      var mobile = window.matchMedia('(max-width: 700px)').matches;
      var base = hero.getAttribute('data-video-base') || 'media/hero-';
      var set = mobile ? 'mobile' : 'desktop';
      function addSource(type, ext) {
        var s = doc.createElement('source');
        s.src = base + set + '.' + ext;
        s.type = type;
        video.appendChild(s);
      }
      function start() {
        addSource('video/webm; codecs="vp9"', 'webm');
        addSource('video/mp4', 'mp4');
        video.muted = true; video.defaultMuted = true; video.setAttribute('muted', '');
        video.load();
        var p = video.play();
        var showing = function () { hero.classList.add('is-playing', 'has-video'); };
        video.addEventListener('playing', showing, { once: true });
        if (p && p.catch) p.catch(function () { /* autoplay blocked: poster stays */ });
      }
      // Start after first paint so the poster (LCP) is never delayed by the video
      if (doc.readyState === 'complete') { setTimeout(start, 50); }
      else { window.addEventListener('load', function () { setTimeout(start, 50); }, { once: true }); }
      if (pauseBtn) {
        pauseBtn.addEventListener('click', function () {
          var icon = pauseBtn.querySelector('i'), label = pauseBtn.querySelector('span');
          if (video.paused) { video.play(); icon.className = 'fa-solid fa-pause'; label.textContent = 'Pause video'; pauseBtn.setAttribute('aria-label', 'Pause background video'); }
          else { video.pause(); icon.className = 'fa-solid fa-play'; label.textContent = 'Play video'; pauseBtn.setAttribute('aria-label', 'Play background video'); }
        });
      }
      // Pause when the tab is hidden or hero is off-screen (saves battery and data)
      doc.addEventListener('visibilitychange', function () { if (doc.hidden) video.pause(); else if (hero.classList.contains('is-playing') && pauseBtn && pauseBtn.querySelector('span').textContent === 'Pause video') video.play().catch(function () {}); });
    } else if (video) {
      video.remove();
      if (pauseBtn) pauseBtn.remove();
    }
  }

  /* ---- Lightbox ---- */
  var items = Array.prototype.slice.call(doc.querySelectorAll('[data-lightbox]'));
  var lb = doc.getElementById('lightbox');
  if (items.length && lb) {
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('figcaption');
    var idx = 0, lastFocus = null;
    function visible() { return items.filter(function (i) { return !i.hidden; }); }
    function show(n) {
      var list = visible(); if (!list.length) return;
      idx = (n + list.length) % list.length;
      var it = list[idx];
      lbImg.src = it.getAttribute('data-full'); lbImg.alt = it.getAttribute('data-alt') || '';
      lbCap.textContent = it.getAttribute('data-caption') || '';
    }
    function open(el) { lastFocus = el; var list = visible(); lb.classList.add('open'); doc.body.style.overflow = 'hidden'; show(list.indexOf(el)); lb.querySelector('.lb-close').focus(); }
    function close() { lb.classList.remove('open'); doc.body.style.overflow = ''; lbImg.src = ''; if (lastFocus) lastFocus.focus(); }
    items.forEach(function (el) { el.addEventListener('click', function () { open(el); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    doc.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(idx - 1);
      else if (e.key === 'ArrowRight') show(idx + 1);
      else if (e.key === 'Tab') { // keep focus inside dialog
        var f = lb.querySelectorAll('button'); var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* ---- Header shadow on scroll + back to top ---- */
  var hdr = doc.querySelector('.site-header');
  var top = doc.createElement('button');
  top.type = 'button'; top.className = 'to-top'; top.setAttribute('aria-label', 'Back to top');
  top.innerHTML = '<i class="fa-solid fa-arrow-up" aria-hidden="true"></i>';
  top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }); });
  doc.body.appendChild(top);
  function onScroll() {
    var y = window.scrollY || doc.documentElement.scrollTop;
    if (hdr) hdr.classList.toggle('is-scrolled', y > 8);
    top.classList.toggle('show', y > 1200);
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---- Sub-navigation scroll-spy ---- */
  var subLinks = Array.prototype.slice.call(doc.querySelectorAll('.subnav a'));
  if (subLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    subLinks.forEach(function (a) { var t = doc.getElementById(a.getAttribute('href').slice(1)); if (t) map[t.id] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { subLinks.forEach(function (a) { a.removeAttribute('aria-current'); }); map[en.target.id].setAttribute('aria-current', 'true'); var ul = map[en.target.id].closest('ul'); if (ul && ul.scrollWidth > ul.clientWidth) ul.scrollLeft = map[en.target.id].offsetLeft - 20; }
      });
    }, { rootMargin: '-35% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) { spy.observe(doc.getElementById(id)); });
  }

  /* ---- Footer newsletter (Firestore "subscribers", loaded on submit) ---- */
  doc.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    var input = form.querySelector('input'), status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = input.value.trim();
      if (!/^\S+@\S+\.\S+$/.test(email)) { status.textContent = 'Please enter a valid email address.'; return; }
      status.textContent = 'Subscribing...';
      window.LisheFirebase.db().then(function (db) {
        return db.collection('subscribers').add({ email: email, subscribedAt: window.firebase.firestore.FieldValue.serverTimestamp(), source: 'footer' });
      }).then(function () { status.textContent = 'Subscribed. Thank you.'; form.reset(); })
        .catch(function () { status.textContent = 'Subscription failed. Please try again.'; });
    });
  });

  /* ---- Gallery filters ---- */
  var filterBtns = doc.querySelectorAll('[data-filter]');
  if (filterBtns.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var cat = btn.getAttribute('data-filter');
        filterBtns.forEach(function (b) { var on = b === btn; b.classList.toggle('active', on); b.setAttribute('aria-pressed', String(on)); });
        doc.querySelectorAll('[data-cat]').forEach(function (el) { el.hidden = !(cat === 'all' || el.getAttribute('data-cat') === cat); });
      });
    });
  }
})();
