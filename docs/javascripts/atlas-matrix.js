/* MLASTG × MITRE ATLAS coverage matrix — "periodic table" of ML attack
   techniques, grouped by the MLASVS control family that covers them.
   Data is sourced from docs/ATLAS-Mapping/2-atlas-navigator-layer.json. */
(function () {
  "use strict";

  // id, symbol, name, family, coverage, mapped controls
  var T = [
    ["AML.T0001", "TD", "Search for Tainted ML Data", "DATA", "full", "DATA-001"],
    ["AML.T0020", "PD", "Poison Training Data", "DATA", "full", "DATA-011, DATA-024, DATA-025"],
    ["AML.T0020.001", "LP", "Label Poisoning", "DATA", "partial", "DATA-011, DATA-013"],
    ["AML.T0021", "PP", "Publish Poisoned Datasets", "DATA", "partial", "DATA-002"],

    ["AML.T0005", "IA", "Exploit ML Model for Initial Access", "MODEL", "partial", "MODEL (partial)"],
    ["AML.T0007", "MI", "ML Model Inversion Attack", "MODEL", "full", "MODEL-003, MODEL-019, MODEL-020"],
    ["AML.T0010", "AD", "Craft Adversarial Data", "MODEL", "full", "MODEL-001, MODEL-002, MODEL-010, MODEL-016"],
    ["AML.T0011", "EV", "Evade ML Model", "MODEL", "full", "MODEL-001…003, INFRA-013"],
    ["AML.T0012", "BD", "Backdoor ML Model", "MODEL", "full", "MODEL-021, MODEL-022, SUPPLY-019"],
    ["AML.T0013", "EQ", "Model Extraction via Repeated Queries", "MODEL", "full", "MODEL-004…006, MODEL-018"],
    ["AML.T0014", "IV", "Invert ML Model", "MODEL", "full", "MODEL-003, MODEL-019, MODEL-020"],
    ["AML.T0018", "Bs", "Backdoor ML Model (supply variant)", "MODEL", "partial", "MODEL-021 (L2)"],
    ["AML.T0034", "MX", "ML Model Extraction", "MODEL", "full", "MODEL-004…006, MODEL-018, MODEL-023"],
    ["AML.T0035", "EI", "Erode ML Model Integrity", "MODEL", "full", "MODEL-007, MODEL-008, MODEL-014, MODEL-015"],
    ["AML.T0056", "BM", "ML Model Behavioral Manipulation", "MODEL", "full", "MODEL-013, INFRA-014, INFRA-018"],
    ["AML.T0058", "Mv", "ML Model Inversion Attack", "MODEL", "full", "MODEL-003, MODEL-019"],
    ["AML.T0059", "BP", "Backdoor ML Model via Poisoning", "MODEL", "full", "MODEL-021, MODEL-022, DATA-001"],

    ["AML.T0037", "DoS", "Model Denial of Service", "LLM", "full", "LLM-011…013, MODEL-012"],
    ["AML.T0051", "PI", "LLM Prompt Injection", "LLM", "full", "LLM-001, LLM-002, LLM-004, LLM-015, LLM-016"],
    ["AML.T0052", "DL", "LLM Data Leakage", "LLM", "full", "LLM-003, LLM-008, LLM-009, LLM-014"],
    ["AML.T0053", "PC", "LLM Plugin Compromise", "LLM", "partial", "LLM-006, LLM-007, LLM-020, LLM-021 (L2)"],
    ["AML.T0054", "JB", "LLM Jailbreak", "LLM", "full", "LLM-005, LLM-017, LLM-022"],
    ["AML.T0031", "XA", "Exfiltration via ML Inference API", "LLM", "partial", "LLM-008, MODEL-009"],
    ["AML.T0057", "DX", "ML Model Data Exfiltration", "LLM", "partial", "LLM-008, DATA-015"],

    ["AML.T0002", "PM", "Obtain ML Model from Public Source", "SUPPLY", "partial", "SUPPLY-002"],
    ["AML.T0003", "CS", "Compromise ML Supply Chain", "SUPPLY", "full", "SUPPLY-001, SUPPLY-002"],

    ["AML.T0000", "AS", "ML Attack Staging", "PIPELINE", "full", "PIPELINE controls"]
  ];

  var FAMILIES = [
    ["DATA",     "Data Security",   "MLASVS-DATA"],
    ["MODEL",    "Model Security",  "MLASVS-MODEL"],
    ["LLM",      "LLM Security",    "MLASVS-LLM"],
    ["SUPPLY",   "Supply Chain",    "MLASVS-SUPPLY"],
    ["PIPELINE", "Pipeline & MLOps","MLASVS-PIPELINE"]
  ];

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    var root = document.getElementById("atlas-matrix");
    if (!root) return;
    render(root);
  });

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function render(root) {
    var detail = document.getElementById("atlas-detail");

    // Columns by family
    var grid = el("div", "atlas-grid");
    FAMILIES.forEach(function (f) {
      var items = T.filter(function (t) { return t[3] === f[0]; });
      var col = el("div", "atlas-col");
      var head = el("div", "atlas-col__head");
      head.appendChild(el("span", "atlas-col__code", f[2]));
      head.appendChild(el("h3", null, f[1]));
      head.appendChild(el("span", "atlas-col__count", items.length + (items.length === 1 ? " technique" : " techniques")));
      col.appendChild(head);

      items.forEach(function (t) {
        var tile = el("button", "atlas-tile is-" + t[4]);
        tile.type = "button";
        tile.setAttribute("data-cov", t[4]);
        tile.setAttribute("data-q", (t[0] + " " + t[2]).toLowerCase());
        tile.setAttribute("aria-label", t[2] + " — " + (t[4] === "full" ? "full" : "partial") + " coverage");
        tile.innerHTML =
          '<span class="atlas-tile__id">' + t[0].replace("AML.", "") + '</span>' +
          '<span class="atlas-tile__dot"></span>' +
          '<span class="atlas-tile__sym">' + t[1] + '</span>' +
          '<span class="atlas-tile__name">' + t[2] + '</span>';
        tile.addEventListener("click", function () {
          [].forEach.call(root.querySelectorAll(".atlas-tile.is-active"), function (a) { a.classList.remove("is-active"); });
          tile.classList.add("is-active");
          showDetail(detail, t, f);
        });
        col.appendChild(tile);
      });
      grid.appendChild(col);
    });

    // Wire toolbar (filter + search) if present
    var toolbar = document.getElementById("atlas-toolbar");
    if (toolbar) {
      toolbar.addEventListener("click", function (e) {
        var b = e.target.closest("[data-filter]");
        if (!b) return;
        [].forEach.call(toolbar.querySelectorAll("[data-filter]"), function (x) { x.classList.remove("is-on"); });
        b.classList.add("is-on");
        applyFilters(root, b.getAttribute("data-filter"), searchVal());
      });
      var search = document.getElementById("atlas-search");
      if (search) search.addEventListener("input", function () {
        var on = toolbar.querySelector("[data-filter].is-on");
        applyFilters(root, on ? on.getAttribute("data-filter") : "all", searchVal());
      });
    }

    root.appendChild(grid);

    function searchVal() {
      var s = document.getElementById("atlas-search");
      return s ? s.value.trim().toLowerCase() : "";
    }
  }

  function applyFilters(root, cov, q) {
    [].forEach.call(root.querySelectorAll(".atlas-tile"), function (tile) {
      var okCov = cov === "all" || tile.getAttribute("data-cov") === cov;
      var okQ = !q || tile.getAttribute("data-q").indexOf(q) !== -1;
      tile.classList.toggle("is-hidden", !(okCov && okQ));
    });
    // Hide empty columns
    [].forEach.call(root.querySelectorAll(".atlas-col"), function (col) {
      var visible = col.querySelectorAll(".atlas-tile:not(.is-hidden)").length;
      col.classList.toggle("is-empty", visible === 0);
    });
  }

  function showDetail(detail, t, f) {
    if (!detail) return;
    var badge = t[4] === "full"
      ? '<span class="atlas-badge atlas-badge--full">Full coverage</span>'
      : '<span class="atlas-badge atlas-badge--partial">Partial coverage</span>';
    detail.innerHTML =
      '<div class="atlas-detail__top">' +
        '<span class="atlas-detail__id">' + t[0] + '</span>' + badge +
      '</div>' +
      '<h3 class="atlas-detail__name">' + t[2] + '</h3>' +
      '<div class="atlas-detail__meta">' +
        '<span class="atlas-detail__fam">' + f[2] + ' · ' + f[1] + '</span>' +
      '</div>' +
      '<p class="atlas-detail__label">Mapped controls</p>' +
      '<p class="atlas-detail__ctrls">' + t[5] + '</p>';
    detail.classList.add("is-shown");
  }
})();
