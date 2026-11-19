# Clear Head Trading

Source for [clearheadtrading.com](https://clearheadtrading.com) — a Hugo static site covering trading education (Learn), a blog, tool reviews/affiliate content, and comparison tools for prop firms and brokers.

## Stack

- **Hugo** (extended, v0.162.1, set as the `HUGO_VERSION` build variable in Cloudflare) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme as a git submodule under `themes/PaperMod`.
- **Cloudflare Workers** (static assets) for hosting, moved from Netlify in November 2026. Workers Builds runs `hugo --gc --minify` and then `npx wrangler deploy`, which uploads `public/` (gitignored, not committed) as configured in `wrangler.jsonc`. `worker/index.js` only redirects www to the bare domain; everything else is served straight from `public/`.
- `static/_redirects` holds the `/go/*` affiliate links and `static/_headers` the cache headers. Cloudflare reads both from the build output.
- The contact form posts to **Web3Forms**, which emails each message and then redirects to `/contact/thanks/`. Its access key is public by design and sits in `content/contact/index.md`.
- `netlify.toml` only remains while Netlify is kept as a fallback; delete it once Netlify is switched off.
- No JS build step and no `package.json` — everything is plain Hugo templates/content.

## Local development

```sh
git clone --recurse-submodules git@github.com:aquada/clearheadtrading.git
cd clearheadtrading
hugo server -D --baseURL http://localhost:1313/
```

- `--recurse-submodules` matters — the theme lives in a submodule (`git submodule update --init` if you forgot).
- Always pass `--baseURL` for local dev; the config's `baseURL` is the production domain, and Hugo will otherwise generate absolute links pointing at `clearheadtrading.com`.
- Don't run a production build (`hugo --gc --minify`) into `public/` while `hugo server` is running — they can race on the same output directory.
- `static/_redirects` (`/go/*` affiliate links) only works on the deployed site, not under `hugo server`, so a local 404 on one of those is expected. To test them locally, build into a scratch folder and run `npx wrangler dev` there (copy `wrangler.jsonc` and `worker/` alongside `public/`).

## Content layout

- `content/learn/` — structured trading curriculum, organised by section (Foundations, Reading Charts, Market Structure, Risk Management, …). Each topic is a Hugo page bundle (`index.md` + co-located images).
- `content/blog/` — blog posts and trader interviews, also page bundles where they carry images.
- `content/prop-firms/` and `content/brokers/` — comparison tools. Data lives in `static/data/propfirms.json` / `static/data/brokers.json`; the client-side compare/filter UI is in `layouts/prop-firms/` and `layouts/brokers/`.
- `content/tools/` — affiliate write-ups for third-party trading tools.
- `content/shop/`, `content/services/` — commercial pages.

## Data refresh and content research

`static/data/propfirms.json` and `static/data/brokers.json` need periodic re-verification against live sources, and the weekly blog cadence includes research-driven posts (market reviews, tool comparisons). This is done live in a Claude Code session rather than via a scheduled headless API job — there's no `ANTHROPIC_API_KEY`-driven automation in this repo. (An earlier version of this repo had one; it was removed 2026-08-10 since it required separate pay-as-you-go Anthropic Console billing on top of a Claude subscription plan.)

`.github/workflows/scheduled-publish.yml` runs weekly (Monday 06:00 UTC) and triggers a Cloudflare rebuild via a `CLOUDFLARE_DEPLOY_HOOK` repo secret (and Netlify's `NETLIFY_BUILD_HOOK` while it's still the fallback), so future-dated blog posts go live even on a week with no other push. In practice, pushing to `main` also deploys immediately through Cloudflare's GitHub integration, so this job only matters for a post whose `date` crosses into the past with no push happening that day.

## Deployment

Cloudflare builds on every push to `main` (and via the weekly scheduled-publish workflow above). There's no separate staging environment — `hugo server` locally is the way to preview changes before pushing.
