---
title: "Get in Touch"
description: "Contact Clear Head Trading — EA development enquiries, feedback, or questions about the site."
url: "/contact/"
disableShare: true
hideMeta: true
ShowToc: false
---

Whether you're after custom EA work, spotted something wrong on the site, or just want to say hello, use the form below and I'll get back to you personally, usually within a couple of days.

<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/contact/thanks/" class="contact-form">
  <input type="hidden" name="form-name" value="contact" />
  <p class="contact-hp" hidden>
    <label>Don't fill this in if you're human: <input name="bot-field" /></label>
  </p>

  <div class="contact-field">
    <label for="contact-name">Name</label>
    <input type="text" id="contact-name" name="name" required>
  </div>

  <div class="contact-field">
    <label for="contact-email">Email</label>
    <input type="email" id="contact-email" name="email" required>
  </div>

  <div class="contact-field">
    <label for="contact-reason">What's this about?</label>
    <select id="contact-reason" name="reason">
      <option value="EA development">Custom EA / indicator development</option>
      <option value="Prop firms or brokers">Prop firms or brokers tool</option>
      <option value="Site feedback">Site feedback or a correction</option>
      <option value="Something else">Something else</option>
    </select>
  </div>

  <div class="contact-field">
    <label for="contact-message">Message</label>
    <textarea id="contact-message" name="message" rows="6" required placeholder="For EA work: what you're trying to build, what instrument and timeframe, and what you've already tried."></textarea>
  </div>

  <button type="submit" class="contact-submit">Send message</button>
</form>
