/* MLASVS conformance self-assessment. Loads the control register, lets a team
   mark each control Pass / Fail / N-A, computes live L1/L2/category conformance,
   persists to localStorage, and exports an evidence JSON. No backend. */
(function () {
  "use strict";

  var KEY = "mlastg-conformance-v1";
  var STATES = ["pass", "fail", "na"];

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    var root = document.getElementById("cf-app");
    if (!root) return;
    var src = root.getAttribute("data-src") || "../controls.json";
    fetch(src)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) { init(root, d.controls || []); })
      .catch(function (e) { root.innerHTML = '<p class="cr-error">Could not load controls (' + e.message + ').</p>'; });
  });

  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
  function esc(s) { return (s == null ? "" : String(s)).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function init(root, controls) {
    var state = load();
    var cats = {};
    controls.forEach(function (c) { (cats[c.category] = cats[c.category] || []).push(c); });

    var html =
      '<div class="cf-score" id="cf-score"></div>' +
      '<div class="cf-actions">' +
        '<button type="button" id="cf-export" class="cr-download">Export results (JSON)</button>' +
        '<button type="button" id="cf-reset" class="cf-reset">Reset</button>' +
        '<span class="cf-hint">Saved in this browser only.</span>' +
      '</div>';
    Object.keys(cats).forEach(function (cat) {
      html += '<section class="cf-cat"><h2 class="cf-cat__h">' + cat +
        ' <span id="cf-cat-' + cat + '" class="cf-cat__score"></span></h2>';
      cats[cat].forEach(function (c) {
        html +=
          '<div class="cf-row" data-id="' + c.id + '" data-level="' + c.level + '" data-cat="' + c.category + '">' +
            '<div class="cf-row__meta"><span class="cf-id">' + esc(c.id) + '</span>' +
              '<span class="cr-lvl cr-lvl--' + c.level.toLowerCase() + '">' + c.level + '</span>' +
              '<span class="cf-title">' + esc(c.title) + '</span></div>' +
            '<div class="cf-toggle" role="group" aria-label="' + esc(c.id) + ' status">' +
              STATES.map(function (s) {
                return '<button type="button" data-s="' + s + '"' + (state[c.id] === s ? ' class="is-on is-' + s + '"' : '') + '>' +
                  (s === "pass" ? "Pass" : s === "fail" ? "Fail" : "N/A") + '</button>';
              }).join("") +
            '</div>' +
          '</div>';
      });
      html += '</section>';
    });
    root.innerHTML = html;

    root.addEventListener("click", function (e) {
      var b = e.target.closest(".cf-toggle button"); if (!b) return;
      var row = b.closest(".cf-row"); var id = row.getAttribute("data-id"); var s = b.getAttribute("data-s");
      if (state[id] === s) { delete state[id]; } else { state[id] = s; }
      [].forEach.call(row.querySelectorAll(".cf-toggle button"), function (x) { x.className = ""; });
      if (state[id]) b.className = "is-on is-" + state[id];
      save(state); recompute();
    });

    document.getElementById("cf-reset").addEventListener("click", function () {
      state = {}; save(state);
      [].forEach.call(root.querySelectorAll(".cf-toggle button"), function (x) { x.className = ""; });
      recompute();
    });
    document.getElementById("cf-export").addEventListener("click", function () {
      var data = exportData(controls, state);
      var blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "mlastg-conformance.json";
      a.click(); URL.revokeObjectURL(a.href);
    });

    function recompute() {
      document.getElementById("cf-score").innerHTML = scorePanel(controls, state);
      Object.keys(cats).forEach(function (cat) {
        var s = tally(cats[cat], state);
        document.getElementById("cf-cat-" + cat).textContent =
          s.applicable ? s.pass + "/" + s.applicable + " (" + pct(s.pass, s.applicable) + "%)" : "—";
      });
    }
    recompute();
  }

  function tally(list, state) {
    var t = { pass: 0, fail: 0, na: 0, none: 0, total: list.length };
    list.forEach(function (c) {
      var s = state[c.id];
      if (s === "pass") t.pass++; else if (s === "fail") t.fail++;
      else if (s === "na") t.na++; else t.none++;
    });
    t.applicable = t.total - t.na; // N/A excluded from the denominator
    return t;
  }

  function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }

  function scorePanel(controls, state) {
    var l1 = tally(controls.filter(function (c) { return c.level === "L1"; }), state);
    var l2 = tally(controls.filter(function (c) { return c.level === "L2"; }), state);
    function card(label, t, cls) {
      var conformant = t.none === 0 && t.fail === 0 && t.applicable > 0;
      return '<div class="cf-card ' + cls + (conformant ? " is-conformant" : "") + '">' +
        '<span class="cf-card__pct">' + pct(t.pass, t.applicable) + '%</span>' +
        '<span class="cf-card__label">' + label + ' conformance</span>' +
        '<span class="cf-card__sub">' + t.pass + ' pass · ' + t.fail + ' fail · ' + t.na + ' N/A · ' + t.none + ' unassessed</span>' +
        (conformant ? '<span class="cf-card__badge">CONFORMANT</span>' : '') +
      '</div>';
    }
    return card("L1 — Standard", l1, "cf-card--l1") + card("L2 — Defense-in-Depth", l2, "cf-card--l2");
  }

  function exportData(controls, state) {
    var l1 = tally(controls.filter(function (c) { return c.level === "L1"; }), state);
    var l2 = tally(controls.filter(function (c) { return c.level === "L2"; }), state);
    return {
      standard: "MLASVS",
      assessed_at: new Date().toISOString(),
      scores: {
        L1: { pass: l1.pass, fail: l1.fail, na: l1.na, unassessed: l1.none, conformance_pct: pct(l1.pass, l1.applicable) },
        L2: { pass: l2.pass, fail: l2.fail, na: l2.na, unassessed: l2.none, conformance_pct: pct(l2.pass, l2.applicable) }
      },
      results: controls.map(function (c) { return { id: c.id, level: c.level, status: state[c.id] || "unassessed" }; })
    };
  }
})();
