# Checklist: move clearheadtrading.com from Netlify to Cloudflare

Decided 2026-11-18 along with the other sites (Netlify serves Greyton from
Amazon São Paulo, Cloudflare from Johannesburg). This follows the tested
handcraftedpages.com runbook. barechart.com stays on Netlify until it expires.

The code side is done on `website-changes`: `wrangler.jsonc`, `worker/index.js`
(www → bare domain), `static/_redirects` (the `/go/` links), Web3Forms on the
contact form, and the Monday workflow now calls a Cloudflare deploy hook.
Checked locally with `wrangler dev`: pages, 404, `/go/` 302s, cache headers,
www redirect.

Netlify keeps serving the live site right up to step 6, so anything before
that can be abandoned without harm.

## 1. Merge and push (Claude, after your review)
- Merge `website-changes` into `main` and push. Netlify deploys it as usual.
- Send yourself a test message through https://clearheadtrading.com/contact/.
  It should land on the "Message sent" page and arrive by email from Web3Forms.

## 2. Create the Worker (Cloudflare dashboard)
- Workers & Pages → Create application → import `aquada/clearheadtrading`.
- Build command: `hugo --gc --minify`. Deploy command: `npx wrangler deploy`.
- Afterwards, Settings → Build → Variables, add:
  - `HUGO_VERSION` = `0.162.1` (otherwise it uses an old Hugo)
  - `TZ` = `Africa/Johannesburg`
  - `HUGO_ENV` = `production`
  - `HUGO_ENABLEGITINFO` = `true`
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
Certificate, http → https, www → bare, pages, 404, `/go/` links, contact form,
MX/SPF/DKIM unchanged, a manual run of the scheduled-publish workflow, and a test
email to yourself.

## 8. After a week of no problems
- Netlify: remove clearheadtrading.com from the site and its DNS zone (not
  barechart.com's), and stop the site's auto-builds.
- Delete `netlify.toml`, the `NETLIFY_BUILD_HOOK` secret and its step in
  `scheduled-publish.yml`, and this file.
