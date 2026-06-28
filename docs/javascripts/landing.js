/* MLASTG landing interactions — counters, scroll reveal, hero matrix.
   GPU-friendly (transform/opacity only) and reduced-motion aware. */
(function () {
  "use strict";

  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    var matrix = document.getElementById("mlx-matrix");
    if (!matrix) return; // not the landing page

    buildMatrix(matrix);
    setupReveal();
    setupCounters();
  });

  /* Faint coverage heat-map behind the hero — evokes the ATLAS Navigator. */
  function buildMatrix(host) {
    var cols = 26, rows = 12, total = cols * rows;
    host.style.setProperty("--mlx-cols", cols);
    var frag = document.createDocumentFragment();
    for (var i = 0; i < total; i++) {
      var cell = document.createElement("span");
      cell.className = "mlx-cell";
      var r = Math.random();
      if (r > 0.86) cell.classList.add("is-hot");        // orange — critical
      else if (r > 0.62) cell.classList.add("is-warm");  // indigo — covered
      if (!reduce && r > 0.62) {
        cell.style.animationDelay = (Math.random() * 6).toFixed(2) + "s";
      }
      frag.appendChild(cell);
    }
    host.appendChild(frag);
  }

  /* Scroll-reveal with a light per-group stagger. */
  function setupReveal() {
    var items = [].slice.call(document.querySelectorAll("[data-reveal]"));
    if (reduce || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var sibs = [].slice.call(el.parentNode.querySelectorAll(":scope > [data-reveal]"));
        var idx = sibs.indexOf(el);
        el.style.transitionDelay = (Math.max(idx, 0) * 70) + "ms";
        el.classList.add("is-in");
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    items.forEach(function (el) { io.observe(el); });
  }

  /* Count-up stats when the band scrolls into view. */
  function setupCounters() {
    var nums = [].slice.call(document.querySelectorAll("[data-count]"));
    if (!nums.length) return;
    if (reduce || !("IntersectionObserver" in window)) {
      nums.forEach(function (el) { el.textContent = el.getAttribute("data-count"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        animateCount(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    nums.forEach(function (el) { io.observe(el); });
  }

  function animateCount(el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0;
    var dur = 1100, start = performance.now();
    function tick(now) {
      var t = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - t, 3); // ease-out cubic
      el.textContent = Math.round(target * eased).toString();
      if (t < 1) requestAnimationFrame(tick);
      else el.textContent = target.toString();
    }
    requestAnimationFrame(tick);
  }
})();
