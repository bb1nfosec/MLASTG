/* MLASVS control register explorer — loads the generated controls.json and
   renders a filterable, searchable traceability table
   (control → level → ATLAS → test). */
(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    var root = document.getElementById("cr-app");
    if (!root) return;
    var src = root.getAttribute("data-src") || "../controls.json";
    fetch(src)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (data) { init(root, data); })
      .catch(function (e) {
        root.innerHTML = '<p class="cr-error">Could not load the control register (' + e.message + ').</p>';
      });
  });

  function atlasLink(id) {
    if (!id) return '<span class="cr-muted">—</span>';
    // Tactics are AML.TAxxxx, techniques AML.Txxxx
    var isTactic = /AML\.TA/.test(id);
    var url = isTactic
      ? "https://atlas.mitre.org/tactics/" + id
      : "https://atlas.mitre.org/techniques/" + id.split(".").slice(0, 2).join(".");
    return '<a href="' + url + '" target="_blank" rel="noopener">' + id + "</a>";
  }

  function esc(s) {
    return (s == null ? "" : String(s)).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function init(root, data) {
    var controls = data.controls || [];
    var cats = data.summary && data.summary.by_category ? data.summary.by_category : {};
    var catKeys = Object.keys(cats);

    root.innerHTML =
      '<div class="cr-toolbar">' +
        '<div class="cr-filters" id="cr-cat" role="group" aria-label="Filter by category">' +
          '<button data-cat="all" class="is-on">All</button>' +
          catKeys.map(function (c) { return '<button data-cat="' + c + '">' + c + "</button>"; }).join("") +
        "</div>" +
        '<div class="cr-filters" id="cr-lvl" role="group" aria-label="Filter by level">' +
          '<button data-lvl="all" class="is-on">L1 + L2</button>' +
          '<button data-lvl="L1">L1</button>' +
          '<button data-lvl="L2">L2</button>' +
        "</div>" +
        '<input id="cr-search" class="cr-search" type="search" placeholder="Search controls…" aria-label="Search controls">' +
        '<a class="cr-download" href="' + (root.getAttribute("data-src") || "../controls.json") + '" download>Download JSON</a>' +
      "</div>" +
      '<p class="cr-count" id="cr-count"></p>' +
      '<div class="cr-tablewrap"><table class="cr-table">' +
        "<thead><tr>" +
          "<th>ID</th><th>Control</th><th>Lvl</th><th>MITRE ATLAS</th><th>Test</th><th>Weakness</th><th>Frameworks</th><th>Description</th>" +
        "</tr></thead><tbody id='cr-body'></tbody>" +
      "</table></div>";

    var body = root.querySelector("#cr-body");
    controls.forEach(function (c) {
      var tr = document.createElement("tr");
      tr.setAttribute("data-cat", c.category);
      tr.setAttribute("data-lvl", c.level);
      var weak = (c.mlaswe || []).join(", ");
      var refs = c.references || {};
      var refMap = { nist_ai_rmf: "NIST", owasp: "OWASP", owasp_ai_exchange: "AIX", eu_ai_act: "EU" };
      var refTags = Object.keys(refMap).filter(function (k) { return refs[k]; }).map(function (k) {
        return '<span class="cr-fw" title="' + esc(refMap[k] + ": " + refs[k]) + '">' + refMap[k] + "</span>";
      }).join("");
      tr.setAttribute("data-q", (c.id + " " + (c.title || "") + " " + (c.description || "") + " " + (c.atlas || "") + " " + weak + " " + Object.values(refs).join(" ")).toLowerCase());
      tr.innerHTML =
        '<td class="cr-id">' + esc(c.id) + "</td>" +
        "<td>" + esc(c.title) + "</td>" +
        '<td><span class="cr-lvl cr-lvl--' + c.level.toLowerCase() + '">' + c.level + "</span></td>" +
        "<td class='cr-atlas'>" + atlasLink(c.atlas) + "</td>" +
        '<td class="cr-test">' + (c.test ? esc(c.test) : '<span class="cr-muted">—</span>') + "</td>" +
        '<td class="cr-weak">' + (weak ? esc(weak) : '<span class="cr-muted">—</span>') + "</td>" +
        '<td class="cr-fws">' + (refTags || '<span class="cr-muted">—</span>') + "</td>" +
        '<td class="cr-desc">' + esc(c.description) + "</td>";
      body.appendChild(tr);
    });

    var state = { cat: "all", lvl: "all", q: "" };
    function apply() {
      var shown = 0;
      [].forEach.call(body.querySelectorAll("tr"), function (tr) {
        var ok =
          (state.cat === "all" || tr.getAttribute("data-cat") === state.cat) &&
          (state.lvl === "all" || tr.getAttribute("data-lvl") === state.lvl) &&
          (!state.q || tr.getAttribute("data-q").indexOf(state.q) !== -1);
        tr.style.display = ok ? "" : "none";
        if (ok) shown++;
      });
      root.querySelector("#cr-count").textContent =
        shown + " of " + controls.length + " controls";
    }

    root.querySelector("#cr-cat").addEventListener("click", function (e) {
      var b = e.target.closest("[data-cat]"); if (!b) return;
      setOn(this, b); state.cat = b.getAttribute("data-cat"); apply();
    });
    root.querySelector("#cr-lvl").addEventListener("click", function (e) {
      var b = e.target.closest("[data-lvl]"); if (!b) return;
      setOn(this, b); state.lvl = b.getAttribute("data-lvl"); apply();
    });
    root.querySelector("#cr-search").addEventListener("input", function () {
      state.q = this.value.trim().toLowerCase(); apply();
    });

    function setOn(group, btn) {
      [].forEach.call(group.querySelectorAll("button"), function (x) { x.classList.remove("is-on"); });
      btn.classList.add("is-on");
    }

    apply();
  }
})();
