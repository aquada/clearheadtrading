---
title: "Get in Touch"
description: "Contact Clear Head Trading — EA development enquiries, feedback, or questions about the site."
url: "/contact/"
disableShare: true
hideMeta: true
ShowToc: false
---

Whether you're after custom EA work, spotted something wrong on the site, or just want to say hello, drop me an email or a message on Telegram. I read everything myself and usually reply within a couple of days.

<div class="contact-options">
  <div class="contact-option">
    <span class="contact-option-label">Email</span>
    <a class="contact-option-value" href="mailto:hello@clearheadtrading.com">hello@clearheadtrading.com</a>
  </div>
  <div class="contact-option">
    <span class="contact-option-label">Telegram</span>
    <a class="contact-option-value" href="https://t.me/danphillips" rel="noopener" target="_blank">@danphillips</a>
  </div>
</div>

## Writing about something specific?

These open an email with the subject filled in, which helps me get back to you sooner.

<ul class="contact-topics">
  <li><a data-topic="ea" href="mailto:hello@clearheadtrading.com?subject=Clear%20Head%20Trading%3A%20EA%20development&amp;body=What%20I%27m%20trying%20to%20build%3A%0A%0AInstrument%20and%20timeframe%3A%0A%0AWhat%20I%27ve%20already%20tried%3A%0A">Custom EA or indicator development</a></li>
  <li><a data-topic="tools" href="mailto:hello@clearheadtrading.com?subject=Clear%20Head%20Trading%3A%20prop%20firms%20or%20brokers">The prop firms or brokers comparison</a></li>
  <li><a data-topic="journal" href="mailto:hello@clearheadtrading.com?subject=CHT%20Journal%3A%20feedback">CHT Journal feedback</a></li>
  <li><a data-topic="site" href="mailto:hello@clearheadtrading.com?subject=Clear%20Head%20Trading%3A%20site%20feedback">Site feedback or a correction</a></li>
</ul>

<script>
(function () {
  // The CHT Journal app's Feedback link opens /contact/?from=journal:<page>.
  // Point the journal email at that page and move it to the top.
  var params = new URLSearchParams(window.location.search);
  var from = params.get("from");
  if (!from || from.indexOf("journal:") !== 0) return;

  var page = from.slice("journal:".length).slice(0, 80);
  var link = document.querySelector('.contact-topics a[data-topic="journal"]');
  if (!link) return;

  var subject = "CHT Journal: feedback" + (page ? " (" + page + ")" : "");
  // Built from parts rather than read back from the link, so it still works
  // after Cloudflare's email obfuscation has rewritten the page's mailto links.
  link.href = "mailto:" + "hello" + "@" + "clearheadtrading.com" +
    "?subject=" + encodeURIComponent(subject);
  link.textContent = "Send feedback about CHT Journal" + (page ? " (" + page + ")" : "");
  var item = link.parentNode;
  item.classList.add("contact-topic-current");
  item.parentNode.insertBefore(item, item.parentNode.firstChild);
})();
</script>
