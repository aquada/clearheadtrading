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
- Open `https://clearheadtrading.<your-subdomain>.workers.dev`. It may look
  partly unstyled, because the pages load CSS from the live domain. That's expected.
- Check `/go/ftmo` (should go to FTMO), `/contact/`, and a made-up page (404).

## 4. Deploy hook for the Monday rebuild
- Worker → Settings → Builds → Deploy Hooks → create one for `main`, copy the URL.
- GitHub → aquada/clearheadtrading → Settings → Secrets and variables →
  Actions → New secret `CLOUDFLARE_DEPLOY_HOOK` = that URL. (Use the web page:
  `gh secret set` needs a prompt that doesn't work through `!`.)

## 5. Add the domain to Cloudflare (Free plan)
DNSSEC is not on (checked: no DS record), so the switch is safe.
- If Cloudflare offers "managed robots.txt" or AI-crawler blocking while adding
  the zone, that's your call; it adds rules to the site's robots.txt. Tell
  Claude what you chose so step 7 checks the result.
- Add `clearheadtrading.com`. Compare the scanned records against this list,
  which is what Netlify DNS serves today (checked 2026-11-19). Set everything to
  **DNS only** (grey cloud), and add anything missing. The DKIM record is the one most often missed.

  | Type | Name | Value |
  |---|---|---|
  | MX | @ | `london.mxroute.com` priority 10 |
  | MX | @ | `london-relay.mxroute.com` priority 20 |
  | TXT | @ | `v=spf1 include:mxroute.com -all` |
  | TXT | @ | `google-site-verification=uyx4kJn9kZZShq8wMFi3bUmNz5zldK4D4nt5PIz5IlY` |
  | TXT | x._domainkey | DKIM key below |
  | A | @ and www | Netlify's (54.232.119.62 today). Leave these; step 6 replaces them |

  DKIM value (paste as one string, no quotes):
  ```
  v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwiThXo4WuEtZSDZZkRpQgkoJ2EmXW9/Eg4y2qa0gjvk+cKdN+oI2dvk5pvQoSXYByH2ZDTPHRPips55R2bY6Pd2jZPFePap4KCBYzXB9ucRu/rOaTFqIEGjk5WWxUqj3QmJ6O0IZlnQw1a3IyZ31TR432LY1161xXP6lPcHHI0iFi7898qDuoSovC8s8BwgwS2sik6g7m+M0NMt/04H6Ou6u1VVvvi9O9O7jQe4Ck/lPN1K3OH/HJFxJTlBRlsWe3u2vcU5nuYxBnRlsEkyv7ZILlgoiEGafsLzJXZTt7rHPhlbDV/FRQZIICO5bl6MsPBebCia5CIBQ3O2P/z4z3wIDAQAB
  ```
  Also look in Netlify → Domains → clearheadtrading.com → DNS records for
  anything not on this list. Only records someone queries show up from outside.
- Porkbun → clearheadtrading.com → Nameservers → replace the four
  `dnsN.p05.nsone.net` with the two Cloudflare gives you.
- Wait for Cloudflare to email you that the zone is active.

## 6. As soon as the zone is active (do this promptly)
- Worker → Settings → Domains & Routes → add custom domains
  `clearheadtrading.com` and `www.clearheadtrading.com`. It will ask you to delete
  the old A records first. Do that and attach the domains straight away: last time, resolvers
  that asked during the gap cached "no record" for 30 minutes (the Pi-holes included).
- SSL/TLS → Edge Certificates → **Always Use HTTPS**: on.

## 7. Verify (Claude)
Certificate, http → https, www → bare, pages, 404, `/go/` links, contact page,
MX/SPF/DKIM unchanged, a manual run of the scheduled-publish workflow, and a test
email to yourself.

## 8. After a week of no problems
- Netlify: remove clearheadtrading.com from the site and its DNS zone (not
  barechart.com's), and stop the site's auto-builds.
- Delete `netlify.toml`, the `NETLIFY_BUILD_HOOK` secret and its step in
  `scheduled-publish.yml`, and this file.
