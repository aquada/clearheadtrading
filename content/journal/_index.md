---
title: "CHT Journal"
description: "A trade journal and performance analytics tool built around R, not P&L — with emotion, mistakes, and discipline tracked as real data."
hideMeta: true
disableShare: true
---

<div class="journal-hero">
  <p class="journal-kicker">CHT Journal</p>
  <h1>The trade journal built around R, not P&L.</h1>
  <p class="journal-hero-sub">Log a trade and it's measured against what you risked, not what it made, so your edge shows up on the same scale whether you're trading £50 a trade or £5,000. Alongside it, CHT Journal tracks the part most journals leave in a notes field nobody rereads: how you felt going in, whether you stuck to your plan, and what your mistakes are really costing you in R.</p>
  <div class="journal-cta-row">
    <a href="https://journal.clearheadtrading.com/signup" class="journal-cta journal-cta-primary">Sign up free</a>
    <a href="https://journal.clearheadtrading.com/login" class="journal-cta journal-cta-secondary">Sign in</a>
  </div>
</div>

---

## Why it's different

<div class="journal-diff-grid">

<div class="journal-diff-card">

### R first, always

Every stat in the app runs off R, not currency, so a losing streak taken at correct size and a winning streak taken oversized don't get flattened onto the same number. The equity curve, the streaks, and the Trading Score are all built on that same scale.

</div>

<div class="journal-diff-card">

### Emotion tracked, not guessed

Log emotion and confidence next to the trade itself, and it stops being a vague feeling and becomes a chart: R by how you felt, a cost-of-mistake breakdown in Stats, a streak for how many days running you've logged it honestly. Strict mode won't let a trade save until it's there.

</div>

<div class="journal-diff-card">

### Full analytics on the free tier

The whole Dashboard, Stats, and review system come with the free tier — no stripped-down demo. Paid adds EA auto-sync and prop firm challenge tracking, but the behavioural analytics are there from the first trade you log, not held back until you upgrade.

</div>

</div>

---

## See it in action

Click any screenshot to view it full size — the lightbox scrolls through the whole set.

<div class="journal-gallery">

<figure class="journal-gallery-hero">
  <img src="/images/journal/dashboard-emotion-breakdown.jpg" alt="R by how you felt and R by process score charts in CHT Journal, showing Confident trades averaging +1.57R and Hesitant trades averaging -0.75R" tabindex="0" role="button">
  <figcaption>Which emotions cost you money, and by how much.</figcaption>
</figure>

<div class="journal-gallery-grid">

<figure>
  <img src="/images/journal/dashboard-overview.jpg" alt="CHT Journal Dashboard showing the Trading Score, win rate, and equity curve" tabindex="0" role="button">
  <figcaption>Trading Score, win rate, and equity curve at a glance.</figcaption>
</figure>

<figure>
  <img src="/images/journal/trade-form-emotion-picker.jpg" alt="Mistake and emotion pill-pickers on the CHT Journal trade form" tabindex="0" role="button">
  <figcaption>Mistake and emotion, logged in two taps.</figcaption>
</figure>

<figure>
  <img src="/images/journal/trade-form-top.jpg" alt="Top of the CHT Journal trade entry form" tabindex="0" role="button">
  <figcaption>Price, size, R, MAE/MFE — logged in one form.</figcaption>
</figure>

<figure>
  <img src="/images/journal/trade-form-post-review.jpg" alt="Post-trade entry, exit, and trade management ratings in CHT Journal" tabindex="0" role="button">
  <figcaption>Rate your entry, exit, and trade management separately.</figcaption>
</figure>

<figure>
  <img src="/images/journal/reviews-page.jpg" alt="CHT Journal daily review card with reflection prompts" tabindex="0" role="button">
  <figcaption>Daily, weekly, monthly reviews with real prompts.</figcaption>
</figure>

<figure>
  <img src="/images/journal/stats-breakdowns.jpg" alt="CHT Journal Stats page showing R breakdowns by setup and instrument" tabindex="0" role="button">
  <figcaption>Your edge, broken down by setup and instrument.</figcaption>
</figure>

<figure>
  <img src="/images/journal/trade-history.jpg" alt="CHT Journal trade history table with running R" tabindex="0" role="button">
  <figcaption>Every trade, with running R.</figcaption>
</figure>

</div>

</div>

<div class="journal-lightbox" id="journal-lightbox" hidden>
  <button type="button" class="journal-lightbox-close" aria-label="Close">&times;</button>
  <button type="button" class="journal-lightbox-prev" aria-label="Previous screenshot">&#8249;</button>
  <img class="journal-lightbox-img" src="" alt="">
  <button type="button" class="journal-lightbox-next" aria-label="Next screenshot">&#8250;</button>
  <p class="journal-lightbox-caption"></p>
</div>

<script>
(function () {
  var gallery = document.querySelectorAll(".journal-gallery img");
  var items = Array.prototype.map.call(gallery, function (img) {
    return { src: img.src, alt: img.alt, caption: img.closest("figure").querySelector("figcaption").textContent };
  });
  var lightbox = document.getElementById("journal-lightbox");
  var lightboxImg = lightbox.querySelector(".journal-lightbox-img");
  var lightboxCaption = lightbox.querySelector(".journal-lightbox-caption");
  var current = 0;

  function show(index) {
    current = (index + items.length) % items.length;
    var item = items[current];
    lightboxImg.src = item.src;
    lightboxImg.alt = item.alt;
    lightboxCaption.textContent = item.caption;
  }

  function open(index) {
    show(index);
    lightbox.hidden = false;
  }

  function close() {
    lightbox.hidden = true;
    lightboxImg.src = "";
  }

  gallery.forEach(function (img, index) {
    img.addEventListener("click", function () { open(index); });
    img.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(index); }
    });
  });

  lightbox.querySelector(".journal-lightbox-close").addEventListener("click", close);
  lightbox.querySelector(".journal-lightbox-prev").addEventListener("click", function () { show(current - 1); });
  lightbox.querySelector(".journal-lightbox-next").addEventListener("click", function () { show(current + 1); });

  lightbox.addEventListener("click", function (e) {
    if (e.target === lightbox) close();
  });

  document.addEventListener("keydown", function (e) {
    if (lightbox.hidden) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });
})();
</script>

---

## Pricing

<div class="journal-pricing-grid">

<div class="journal-pricing-tier">

### Free

Manual and CSV/MT4 import logging, the full Dashboard and Stats suite, per-trade and period reviews, guardrails, and the leaderboard.

</div>

<div class="journal-pricing-tier journal-pricing-tier-paid">

### Paid — $12/mo

Everything in Free, plus EA auto-sync from MT4/MT5 and prop firm challenge tracking.

</div>

</div>

<div class="journal-cta-row">
  <a href="https://journal.clearheadtrading.com/signup" class="journal-cta journal-cta-primary">Sign up free</a>
</div>

---

## Guides

- **[User Guide](/journal/user-guide/)** — setup, logging trades, reviews, the dashboard, guardrails, prop firm tracking.
- **[EA Auto-Sync Setup](/journal/ea-setup/)** — connecting an MT4/MT5 Expert Advisor so closed trades push into the journal automatically.

---

*Nothing on this page is financial advice. Trade your own account, manage your own risk.*
