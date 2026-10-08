// Rosora — shared site behaviour: mobile nav, accessibility panel, forms.
(function () {
  "use strict";

  /* ---------- Mobile nav toggle ---------- */
  var navToggle = document.querySelector(".nav-toggle");
  var mainNav = document.querySelector(".main-nav");
  if (navToggle && mainNav) {
    navToggle.addEventListener("click", function () {
      var open = mainNav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.textContent = open ? "✕" : "☰";
    });
  }

  /* ---------- Accessibility panel ---------- */
  var root = document.documentElement;
  var panel = document.querySelector(".a11y-panel");
  var overlay = document.querySelector(".a11y-overlay");
  var openBtns = document.querySelectorAll(".a11y-toggle");
  var closeBtn = document.querySelector(".a11y-close");

  function openPanel() {
    panel.classList.add("open");
    overlay.classList.add("open");
    panel.setAttribute("aria-hidden", "false");
  }
  function closePanel() {
    panel.classList.remove("open");
    overlay.classList.remove("open");
    panel.setAttribute("aria-hidden", "true");
  }
  openBtns.forEach(function (b) { b.addEventListener("click", openPanel); });
  if (closeBtn) closeBtn.addEventListener("click", closePanel);
  if (overlay) overlay.addEventListener("click", closePanel);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closePanel();
  });

  var STORE_KEY = "rosora-a11y-prefs";
  function loadPrefs() {
    try { return JSON.parse(localStorage.getItem(STORE_KEY)) || {}; }
    catch (e) { return {}; }
  }
  function savePrefs(p) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(p)); } catch (e) {}
  }

  var prefs = loadPrefs();

  function applyFontScale(scale) {
    root.style.setProperty("--a11y-font-scale", scale);
    document.querySelectorAll("[data-font-btn]").forEach(function (btn) {
      var isActive = btn.getAttribute("data-font-btn") === String(scale);
      btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      btn.classList.toggle("active", isActive);
    });
  }
  function applyContrast(on) {
    if (on) root.setAttribute("data-a11y-contrast", "high");
    else root.removeAttribute("data-a11y-contrast");
    var el = document.querySelector('[data-a11y-switch="contrast"]');
    if (el) el.checked = on;
  }
  function applySpacing(on) {
    if (on) root.setAttribute("data-a11y-spacing", "wide");
    else root.removeAttribute("data-a11y-spacing");
    var el = document.querySelector('[data-a11y-switch="spacing"]');
    if (el) el.checked = on;
  }
  function applyMotion(on) {
    if (on) root.setAttribute("data-a11y-motion", "reduced");
    else root.removeAttribute("data-a11y-motion");
    var el = document.querySelector('[data-a11y-switch="motion"]');
    if (el) el.checked = on;
  }
  function applyLinks(on) {
    if (on) root.setAttribute("data-a11y-links", "highlight");
    else root.removeAttribute("data-a11y-links");
    var el = document.querySelector('[data-a11y-switch="links"]');
    if (el) el.checked = on;
  }

  applyFontScale(prefs.fontScale || 1);
  applyContrast(!!prefs.contrast);
  applySpacing(!!prefs.spacing);
  applyMotion(!!prefs.motion);
  applyLinks(!!prefs.links);

  document.querySelectorAll("[data-font-btn]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var scale = parseFloat(btn.getAttribute("data-font-btn"));
      applyFontScale(scale);
      prefs.fontScale = scale;
      savePrefs(prefs);
    });
  });
  var contrastSwitch = document.querySelector('[data-a11y-switch="contrast"]');
  if (contrastSwitch) contrastSwitch.addEventListener("change", function (e) {
    prefs.contrast = e.target.checked; savePrefs(prefs); applyContrast(e.target.checked);
  });
  var spacingSwitch = document.querySelector('[data-a11y-switch="spacing"]');
  if (spacingSwitch) spacingSwitch.addEventListener("change", function (e) {
    prefs.spacing = e.target.checked; savePrefs(prefs); applySpacing(e.target.checked);
  });
  var motionSwitch = document.querySelector('[data-a11y-switch="motion"]');
  if (motionSwitch) motionSwitch.addEventListener("change", function (e) {
    prefs.motion = e.target.checked; savePrefs(prefs); applyMotion(e.target.checked);
  });
  var linksSwitch = document.querySelector('[data-a11y-switch="links"]');
  if (linksSwitch) linksSwitch.addEventListener("change", function (e) {
    prefs.links = e.target.checked; savePrefs(prefs); applyLinks(e.target.checked);
  });
  var resetBtn = document.querySelector("[data-a11y-reset]");
  if (resetBtn) resetBtn.addEventListener("click", function () {
    prefs = {}; savePrefs(prefs);
    applyFontScale(1); applyContrast(false); applySpacing(false); applyMotion(false); applyLinks(false);
  });

  /* ---------- Simple enquiry form (Start Your Journey) ---------- */
  var journeyForm = document.querySelector("#start-journey-form");
  if (journeyForm) {
    journeyForm.addEventListener("submit", function (e) {
      e.preventDefault();
      journeyForm.style.display = "none";
      var success = document.querySelector("#journey-success");
      if (success) success.classList.add("show");
      if (success) success.setAttribute("tabindex", "-1"), success.focus();
    });
  }

  /* ---------- Generic contact form (no backend in this local build) ---------- */
  var contactForm = document.querySelector("#contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      contactForm.style.display = "none";
      var success = document.querySelector("#contact-success");
      if (success) success.classList.add("show");
    });
  }
})();
