# Checklist: move clearheadtrading.com from Netlify to Cloudflare

Decided 2026-11-18 along with the other sites (Netlify serves Greyton from
Amazon São Paulo, Cloudflare from Johannesburg). This follows the tested
handcraftedpages.com runbook. barechart.com stays on Netlify until it expires.

The code side is done on `website-changes`: `wrangler.jsonc`, `worker/index.js`
(www → bare domain), `static/_redirects` (the `/go/` links), and the Monday workflow now calls a
Cloudflare deploy hook. The contact form is gone (email + Telegram instead), so
there's no Netlify Forms dependency left.
Checked locally with `wrangler dev`: pages, 404, `/go/` 302s, cache headers,
www redirect.

Netlify keeps serving the live site right up to step 6, so anything before
that can be abandoned without harm.

## 1. Merge and push (Claude, after your review)
- Merge `website-changes` into `main` and push. Netlify deploys it as usual.
- Done 2026-11-19: `hello@`, `journal@` and `support@clearheadtrading.com` are
  MXroute forwarders to your main inbox (not Cloudflare Email Routing, which
  would replace the MXroute MX records). `noreply@` is left unforwarded. Expert
  Spam Filtering stayed off (MXroute only forces it for Gmail/Yahoo/AOL-type
  destinations). Leave it off: the main inbox is on MXroute too, so the
  forwarding stays inside MXroute.
- Tested 2026-11-19 from Proton: all three arrive (hello@ and journal@ took a
  while on the first try, so a delay isn't a fault).

## 2. Create the Worker (Cloudflare dashboard)
- Workers & Pages → Create application → import `aquada/clearheadtrading`.
- Build command: `(git fetch --unshallow || true) && hugo --gc --minify --environment production`.
  Deploy command: `npx wrangler deploy`.
  Done 2026-11-19. Plain `hugo --gc --minify` built in non-production mode on
  Cloudflare (every page `noindex, nofollow`, robots.txt `Disallow: /`) despite
  `HUGO_ENV`, and its shallow clone gave every sitemap `lastmod` the latest
  commit's date. With this command the sitemap is byte-identical to Netlify's.
- API token: create a new one for this site rather than reusing the
  handcraftedpages build token (same permissions, but independent).
- Build variables (Settings → **Build** → Variables and secrets, not the
  runtime Variables and Secrets section):
  - `HUGO_VERSION` = `0.162.1` (otherwise it uses an old Hugo)
  - `HUGO_ENABLEGITINFO` = `true` (sitemap last-updated dates come from git)
  - `TZ` = `Africa/Johannesburg` (keeps sitemap times in SAST, as now)
  - Not `HUGO_ENV`: `hugo` already builds in production mode.
- Check that the production branch is `main`, then retry the deployment so it uses the variables.
- If the build complains about a missing theme, the PaperMod submodule wasn't
  fetched. Tell Claude rather than working around it.

## 3. Test the workers.dev copy
Done 2026-11-19 (https://clearheadtrading.daniel-516.workers.dev): pages, 404,
`/go/` 302s, cache headers, robots/noindex, sitemap identical to Netlify's.
- Open `https://clearheadtrading.<your-subdomain>.workers.dev`. It may look
  partly unstyled, because the pages load CSS from the live domain. That's expected.
- Check `/go/ftmo` (should go to FTMO), `/contact/`, and a made-up page (404).

## 4. Deploy hook for the Monday rebuild
Done 2026-11-19: hook "GitHub scheduled publish" (main), secret
`CLOUDFLARE_DEPLOY_HOOK` added, test run of the workflow queued a Cloudflare build.
- Worker → Settings → Builds → Deploy Hooks → create one for `main`, copy the URL.
- GitHub → aquada/clearheadtrading → Settings → Secrets and variables →
  Actions → New secret `CLOUDFLARE_DEPLOY_HOOK` = that URL. (Use the web page:
  `gh secret set` needs a prompt that doesn't work through `!`.)

## 5. Add the domain to Cloudflare (Free plan)
Done by Claude via the Cloudflare MCP server, 2026-11-19. Zone
`clearheadtrading.com` (id `b4cfc6b56b06c47c8446f796451b5c9e`), created without
the scan, holding exactly these records, all DNS only:

| Type | Name | Value |
|---|---|---|
| MX | @ | `london.mxroute.com` priority 10 |
| MX | @ | `london-relay.mxroute.com` priority 20 |
| TXT | @ | `v=spf1 include:mxroute.com -all` |
| TXT | @ | `google-site-verification=uyx4kJn9kZZShq8wMFi3bUmNz5zldK4D4nt5PIz5IlY` |
| TXT | x._domainkey | MXroute DKIM key (copied exactly) |
| A | @ and www | 54.232.119.62 (Netlify) until step 6 |
| A | journal | 75.2.60.5 (Netlify's load balancer: CHT Journal stays on Netlify until it moves too, planned separately in its own repo) |

DNSSEC is off on both sides. AI crawler blocking, managed robots.txt and bot
fight mode are all off (AI crawlers stay allowed, Dan's call). Always Use HTTPS
is on (only affects proxied traffic). Free plan can't lower the SOA negative
TTL, hence the gap-free plan in step 6.

`licensing.clearheadtrading.com` (the licensing EA's API) doesn't exist yet;
give it a record here when it goes live.

- Done 2026-11-19 (zone active the same morning). Porkbun → clearheadtrading.com → Nameservers →
  replaced with `elle.ns.cloudflare.com` and `todd.ns.cloudflare.com`. Nothing
  changes for visitors: Cloudflare answers with the same records as Netlify.
- Wait for the zone to go active (Claude can check).

## 6. Switch the site to the Worker (Claude, once the zone is active)
Done 2026-11-19 (`b4712a9` routes; records edited a few minutes later).
Gap-free, instead of the dashboard's delete-and-attach custom domain:
1. Wait until the zone's Universal SSL certificate is active.
2. Add `routes` for `clearheadtrading.com/*` and `www.clearheadtrading.com/*`
   to `wrangler.jsonc` and push (deploys override routes added any other way,
   so they live in the config). With the records still DNS only, the routes
   don't affect anyone yet.
3. Edit (not delete) the `@` and `www` A records to `192.0.2.1`, proxied. Each
   is a single edit, so there's never a moment with no record.

## 7. Verify (Claude)
Done 2026-11-19, all served by Cloudflare: Let's Encrypt certificate to Feb 2027,
http → https, www → bare, pages, 404, both `/go/` links, robots `index, follow`,
sitemap byte-identical to Netlify's, MX/SPF/DKIM/Google verification unchanged,
journal still on Netlify, scheduled-publish workflow triggers a Cloudflare build.
Pages load in about 0.2–0.7 s (Netlify: 1.3–2.3 s). The workers.dev address
is now off (deploys disable it without `workers_dev` in the config).
- **You:** send a test email from Proton to hello@ to confirm mail still flows.

## 8. After a week of no problems
- Netlify: remove clearheadtrading.com and www from the *website's* Netlify
  site, stop its auto-builds, and delete the clearheadtrading.com DNS zone
  (unused since the nameserver switch). Leave journal.clearheadtrading.com on
  the journal's Netlify site until the journal itself moves, and leave
  barechart.com alone.
- Delete `netlify.toml`, the `NETLIFY_BUILD_HOOK` secret and its step in
  `scheduled-publish.yml`, and this file.
