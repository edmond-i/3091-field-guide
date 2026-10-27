/* Practice engine for the 3.091 Field Guide.
   Enhances static <article class="pq"> question blocks: checking answers, saving progress
   (localStorage, per browser), a "my practice" drawer, topic filters and a timed quiz mode.
   Everything degrades gracefully: without JS the questions, hints and worked solutions are plain <details>. */
(function () {
  "use strict";
  var KEY = "3091-practice-v1";
  var store = {};
  try { store = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { store = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* ---------- number parsing: 3.74e-19, 3.74x10^-19, 3.74*10^-19, 1/2, 2.33 eV ---------- */
  function parseNum(raw) {
    var s = String(raw).trim().toLowerCase()
      .replace(/[−–—]/g, "-").replace(/,/g, "").replace(/\s+/g, " ");
    var f = s.match(/^([+-]?\d+(?:\.\d+)?)\s*\/\s*(\d+(?:\.\d+)?)/);
    if (f) return parseFloat(f[1]) / parseFloat(f[2]);
    var m = s.match(/^([+-]?\d*\.?\d+)\s*(?:e\s*([+-]?\d+)|(?:x|×|\*|·)\s*10\s*\^?\s*\(?\s*([+-]?\d+)\s*\)?)?/);
    if (!m) return NaN;
    var v = parseFloat(m[1]);
    var ex = m[2] !== undefined ? m[2] : m[3];
    if (ex !== undefined) v = v * Math.pow(10, parseInt(ex, 10));
    return v;
  }
  function near(v, a, tol, atol) {
    if (isNaN(v)) return false;
    var allowed = Math.max(Math.abs(a) * tol, atol || 0);
    return Math.abs(v - a) <= allowed + 1e-12 * Math.abs(a);
  }

  /* ---------- per-question behaviour ---------- */
  function status(id) { return (store[id] && store[id].s) || ""; }
  function setStatus(id, s) {
    var r = store[id] || { n: 0 };
    r.s = s; r.n = (r.n || 0) + 1; r.t = Date.now();
    store[id] = r; save();
  }
  function paint(q) {
    var s = status(q.getAttribute("data-id"));
    q.setAttribute("data-status", s);
    var badge = $(".pq-state", q);
    if (badge) badge.textContent = s === "c" ? "✓ got it" : s === "w" ? "retry" : s === "s" ? "peeked" : s === "m" ? "missed" : "";
  }
  function fb(q, ok, html) {
    var box = $(".pq-fb", q);
    if (!box) return;
    box.hidden = false;
    box.className = "pq-fb " + (ok ? "pq-ok" : "pq-bad");
    box.innerHTML = html;
  }
  function solOpened(q) { var d = $(".pq-sol", q); return d && d.open; }

  function check(q) {
    var id = q.getAttribute("data-id"), type = q.getAttribute("data-type");
    if (type === "mc") {
      var sel = $("input[type=radio]:checked", q);
      if (!sel) { fb(q, false, "Pick an answer first."); return; }
      var lab = sel.closest("label"), good = sel.hasAttribute("data-correct");
      $$("label.pq-choice", q).forEach(function (l) { l.classList.remove("is-right", "is-wrong"); });
      lab.classList.add(good ? "is-right" : "is-wrong");
      var why = sel.getAttribute("data-why");
      if (good) {
        fb(q, true, "<b>Correct.</b> " + (why ? why : "") + " Now open the worked solution and compare <em>how</em> you got there.");
        if (!solOpened(q)) setStatus(id, "c"); else if (status(id) !== "c") setStatus(id, "s");
      } else {
        fb(q, false, "<b>Not quite.</b> " + (why ? why : "") + " Try again, or open the hint.");
        if (status(id) !== "c") setStatus(id, "w");
      }
    } else if (type === "num") {
      var inp = $(".pq-input", q), v = parseNum(inp.value);
      if (isNaN(v)) { fb(q, false, "Type a number (for example <code>3.74e-19</code> or <code>3.74x10^-19</code>)."); return; }
      var a = parseFloat(q.getAttribute("data-answer")), tol = parseFloat(q.getAttribute("data-tol") || "0.02");
      var atol = parseFloat(q.getAttribute("data-atol") || "0");
      var alts = (q.getAttribute("data-alt") || "").split(";").filter(Boolean).map(parseFloat);
      var good = near(v, a, tol, atol) || alts.some(function (x) { return near(v, x, tol, atol); });
      var unit = q.getAttribute("data-unit") || "";
      if (good) {
        fb(q, true, "<b>Correct.</b> Answer: " + (q.getAttribute("data-text") || (q.getAttribute("data-answer") + " " + unit)) + ". Open the worked solution to compare methods.");
        if (!solOpened(q)) setStatus(id, "c"); else if (status(id) !== "c") setStatus(id, "s");
      } else {
        var close = Math.abs(v - a) <= Math.abs(a) * 0.15;
        fb(q, false, "<b>Not yet.</b> " + (close ? "You are close: check rounding, units or a sign. " : "Check the setup (units? which formula?). ") + "Open the hint if you are stuck.");
        if (status(id) !== "c") setStatus(id, "w");
      }
    }
    paint(q); refresh();
  }

  function wire(q) {
    var id = q.getAttribute("data-id");
    paint(q);
    var cb = $(".pq-check", q);
    if (cb) cb.addEventListener("click", function () { check(q); });
    var inp = $(".pq-input", q);
    if (inp) inp.addEventListener("keydown", function (e) { if (e.key === "Enter") check(q); });
    var sol = $(".pq-sol", q);
    if (sol) sol.addEventListener("toggle", function () {
      if (sol.open) {
        if (status(id) !== "c" && q.getAttribute("data-type") !== "self") { setStatus(id, "s"); paint(q); refresh(); }
        var self = $(".pq-self", q); if (self) self.hidden = false;
      }
    });
    $$(".pq-self button", q).forEach(function (b) {
      b.addEventListener("click", function () {
        setStatus(id, b.getAttribute("data-r")); paint(q); refresh();
        $$(".pq-self button", q).forEach(function (x) { x.classList.toggle("on", x === b); });
      });
    });
  }

  /* ---------- progress summaries ---------- */
  function counts(scope) {
    var qs = $$(".pq", scope), c = 0, w = 0, tot = qs.length;
    qs.forEach(function (q) { var s = status(q.getAttribute("data-id")); if (s === "c") c++; else if (s === "w" || s === "s" || s === "m") w++; });
    return { c: c, w: w, t: tot };
  }
  function refresh() {
    $$(".pq-block").forEach(function (blk) {
      var k = counts(blk), bar = $(".pq-bar > i", blk), txt = $(".pq-sum", blk);
      if (bar) bar.style.width = (k.t ? Math.round(100 * k.c / k.t) : 0) + "%";
      if (txt) txt.textContent = k.c + " of " + k.t + " done" + (k.w ? " · " + k.w + " to retry" : "");
    });
    var d = $("#pq-drawer");
    if (d && !d.hidden) renderDrawer();
    var all = counts(document), btn = $("#pq-fab");
    if (btn) btn.querySelector("b").textContent = all.c + "/" + all.t;
  }

  /* ---------- drawer: my practice ---------- */
  function renderDrawer() {
    var body = $("#pq-drawer .pq-dbody");
    var topics = {}, order = [];
    $$(".pq").forEach(function (q) {
      var t = q.getAttribute("data-topic") || "other";
      if (!topics[t]) { topics[t] = { c: 0, w: 0, t: 0, title: q.getAttribute("data-topic-title") || t }; order.push(t); }
      var s = status(q.getAttribute("data-id"));
      topics[t].t++; if (s === "c") topics[t].c++; else if (s === "w" || s === "s" || s === "m") topics[t].w++;
    });
    var html = "";
    order.forEach(function (t) {
      var x = topics[t], pct = x.t ? Math.round(100 * x.c / x.t) : 0;
      html += '<div class="pq-trow"><div class="pq-tname">' + x.title + '</div><div class="pq-bar"><i style="width:' + pct + '%"></i></div><div class="pq-tnum">' + x.c + "/" + x.t + "</div></div>";
    });
    var missed = $$(".pq").filter(function (q) { var s = status(q.getAttribute("data-id")); return s === "w" || s === "s" || s === "m"; });
    html += '<h4>To retry (' + missed.length + ")</h4>";
    if (!missed.length) html += '<p class="small">Nothing here yet. Wrong answers, peeked solutions and “missed it” ratings land here.</p>';
    else html += '<ul class="pq-miss">' + missed.map(function (q) { return '<li><a href="#' + q.id + '">' + (q.getAttribute("data-label") || q.id) + "</a></li>"; }).join("") + "</ul>";
    html += '<p><button class="pq-btn pq-ghost" id="pq-reset">Reset my progress</button></p>';
    body.innerHTML = html;
    var r = $("#pq-reset", body);
    if (r) r.addEventListener("click", function () {
      if (confirm("Clear all saved practice progress in this browser?")) { store = {}; save(); $$(".pq").forEach(paint); refresh(); }
    });
    $$("a", body).forEach(function (a) { a.addEventListener("click", function () { $("#pq-drawer").hidden = true; }); });
  }
  function buildDrawer() {
    if (!$$(".pq").length) return;
    var fab = document.createElement("button");
    fab.id = "pq-fab"; fab.className = "pq-fab"; fab.type = "button";
    fab.innerHTML = 'My practice <b>0/0</b>';
    var dr = document.createElement("aside");
    dr.id = "pq-drawer"; dr.className = "pq-drawer"; dr.hidden = true;
    dr.innerHTML = '<div class="pq-dhead"><strong>My practice</strong><button class="pq-x" type="button" aria-label="Close">×</button></div><div class="pq-dbody"></div>';
    document.body.appendChild(fab); document.body.appendChild(dr);
    fab.addEventListener("click", function () { dr.hidden = !dr.hidden; if (!dr.hidden) renderDrawer(); });
    $(".pq-x", dr).addEventListener("click", function () { dr.hidden = true; });
  }

  /* ---------- filters (quiz-review page) ---------- */
  function applyFilters() {
    var bar = $("#pq-filters"); if (!bar) return;
    var topic = bar.getAttribute("data-topic") || "all", diff = bar.getAttribute("data-diff") || "all", st = bar.getAttribute("data-state") || "all";
    $$(".pq").forEach(function (q) {
      var s = status(q.getAttribute("data-id")), ok = true;
      if (topic !== "all" && q.getAttribute("data-topic") !== topic) ok = false;
      if (diff !== "all" && q.getAttribute("data-diff") !== diff) ok = false;
      if (st === "todo" && s === "c") ok = false;
      if (st === "retry" && !(s === "w" || s === "s" || s === "m")) ok = false;
      q.classList.toggle("is-filtered", !ok);
    });
    $$(".pq-topic").forEach(function (sec) {
      var any = $$(".pq:not(.is-filtered)", sec).length > 0;
      sec.classList.toggle("is-empty", !any && (topic !== "all" || diff !== "all" || st !== "all"));
    });
  }
  function wireFilters() {
    var bar = $("#pq-filters"); if (!bar) return;
    $$("[data-f]", bar).forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-f"), v = b.getAttribute("data-v");
        bar.setAttribute("data-" + k, v);
        $$('[data-f="' + k + '"]', bar).forEach(function (x) { x.classList.toggle("on", x === b); });
        applyFilters();
      });
    });
  }

  /* ---------- timed quiz mode ---------- */
  var timer = null, endAt = 0, quizSet = [];
  function fmt(ms) { var s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + ":" + ("0" + (s % 60)).slice(-2); }
  function startQuiz() {
    var panel = $("#pq-quiz"); if (!panel) return;
    var n = parseInt($("#qz-n").value, 10) || 5, mins = parseInt($("#qz-min").value, 10) || 10;
    var topics = $$("#qz-topics input:checked").map(function (i) { return i.value; });
    var pool = $$(".pq").filter(function (q) {
      var t = q.getAttribute("data-type");
      return (t === "mc" || t === "num") && (!topics.length || topics.indexOf(q.getAttribute("data-topic")) > -1);
    });
    if (!pool.length) { $("#qz-msg").textContent = "No auto-scored questions match those topics yet."; return; }
    pool.sort(function () { return Math.random() - 0.5; });
    quizSet = pool.slice(0, n);
    $$(".pq").forEach(function (q) { q.classList.remove("in-quiz"); q.removeAttribute("data-qn"); });
    quizSet.forEach(function (q, i) {
      q.classList.add("in-quiz"); q.setAttribute("data-qn", i + 1);
      store[q.getAttribute("data-id")] = store[q.getAttribute("data-id")] || { n: 0 };
      delete store[q.getAttribute("data-id")].s; paint(q);
      var sol = $(".pq-sol", q); if (sol) { sol.open = false; }
      var fbk = $(".pq-fb", q); if (fbk) fbk.hidden = true;
      $$("label.pq-choice", q).forEach(function (l) { l.classList.remove("is-right", "is-wrong"); });
      $$("input[type=radio]", q).forEach(function (r) { r.checked = false; });
      var inp = $(".pq-input", q); if (inp) inp.value = "";
    });
    document.body.classList.add("quiz-mode"); document.body.classList.remove("quiz-done");
    $("#qz-result").hidden = true;
    endAt = Date.now() + mins * 60000;
    clearInterval(timer);
    timer = setInterval(tick, 500); tick();
    window.scrollTo(0, ($("#pq-stage") || panel).offsetTop - 10);
    refresh();
  }
  function tick() {
    var left = endAt - Date.now(), el = $("#qz-clock");
    el.textContent = fmt(left); el.classList.toggle("warn", left < 60000);
    if (left <= 0) finishQuiz(true);
  }
  function finishQuiz(timeUp) {
    clearInterval(timer);
    document.body.classList.add("quiz-done");
    var right = 0;
    quizSet.forEach(function (q) { if (status(q.getAttribute("data-id")) === "c") right++; });
    // unanswered auto-scored questions count as missed
    quizSet.forEach(function (q) { var id = q.getAttribute("data-id"); if (status(id) !== "c" && status(id) !== "w") { store[id] = store[id] || { n: 0 }; store[id].s = "m"; paint(q); } });
    save();
    var res = $("#qz-result");
    res.hidden = false;
    res.innerHTML = "<strong>" + (timeUp ? "Time’s up. " : "") + "You got " + right + " of " + quizSet.length + " right.</strong> " +
      (right === quizSet.length ? "Clean sweep. Do another set with different topics." : "Open each worked solution below, then retry the missed ones from <em>My practice</em>.") +
      ' <button class="pq-btn" id="qz-again" type="button">New quiz</button>';
    $("#qz-again").addEventListener("click", endQuiz);
    refresh();
  }
  function endQuiz() {
    clearInterval(timer);
    document.body.classList.remove("quiz-mode", "quiz-done");
    $$(".pq").forEach(function (q) { q.classList.remove("in-quiz"); q.removeAttribute("data-qn"); });
    var res = $("#qz-result"); if (res) res.hidden = true;
    window.scrollTo(0, 0);
  }
  function wireQuiz() {
    var go = $("#qz-start"); if (!go) return;
    go.addEventListener("click", startQuiz);
    var sub = $("#qz-submit"); if (sub) sub.addEventListener("click", function () { finishQuiz(false); });
    var quit = $("#qz-quit"); if (quit) quit.addEventListener("click", endQuiz);
  }

  function init() {
    $$(".pq").forEach(wire);
    buildDrawer(); wireFilters(); wireQuiz(); applyFilters(); refresh();
    if (location.hash) { var t = $(location.hash); if (t && t.classList && t.classList.contains("pq")) t.scrollIntoView(); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
