---
title: "CHT Journal — EA Auto-Sync Setup"
description: "Connect an MT4/MT5 Expert Advisor so closed trades push into CHT Journal automatically."
url: "/journal/ea-setup/"
ShowToc: true
---

Auto-sync pushes your closed trades from MT4 or MT5 straight into CHT Journal, with no manual entry and no CSV export. It's available on the Paid tier.

## 1. Download the EA

Grab the version that matches your platform: [TradeLoggerSyncEA for MT4](/downloads/TradeLoggerSyncEA.ex4) or [TradeLoggerSyncEA for MT5](/downloads/TradeLoggerSyncEA.ex5).

In MetaTrader, go to File → Open Data Folder, then drop the file into `MQL4/Experts` (MT4) or `MQL5/Experts` (MT5). Restart MetaTrader, or right-click Expert Advisors in the Navigator panel and choose Refresh, and it'll show up ready to attach.

## 2. Get an API key

In CHT Journal: Settings → API keys → New key, give it a label (something like "FP Markets MT5" is enough to tell it apart later) → Create. Copy the key immediately, because it's shown once and never again. This key only ever lets the EA add trades to your own account — it can't do anything else.

## 3. Allow the connection in MT4/MT5

MetaTrader blocks EAs from making web requests by default, so CHT Journal's domain needs adding to the allow-list first: Tools → Options → Expert Advisors → check "Allow WebRequest for listed URL" → add `https://journal.clearheadtrading.com`.

## 4. Attach the EA to a chart

Drag TradeLoggerSyncEA from the Navigator panel (Expert Advisors) onto any chart — it doesn't matter which instrument or timeframe, because the EA tracks your whole account, not just that one chart. In the EA's Inputs tab, set:

- **ApiKey** — paste the key from step 2
- **IngestUrl** — leave as `https://journal.clearheadtrading.com/api/import/trades`
- **PollSeconds** — how often it checks for newly closed trades, in seconds (30 by default, not minutes)
- **OnlyAfter** — only syncs trades opened on or after this date. Leave it at 1970.01.01 to sync your whole history, or set a cutoff if you've already imported older trades another way. Set this once, before first use — changing it later won't reach trades older than ones already synced.

Make sure "Allow live trading" (or "Allow automated trading") is enabled for the EA, and check for the smiley-face icon in the chart's top-right corner confirming it's running.

## Troubleshooting

**Nothing showing up in CHT Journal.** Check the terminal's Experts log for errors first. A 401 means the API key is wrong or was revoked; a connection error usually means step 3's allow-list is missing the URL, or has a typo in it.

**Missing a chunk of history after correcting OnlyAfter.** If OnlyAfter was ever set to a future date, trades that fell inside that window get permanently skipped by design, even after the date's fixed. To recover them: Tools → Global Variables (F3) → delete `TradeLoggerSync_LastTicket_<account>` (MT4) or `TradeLoggerSync_LastPositionId_<account>` (MT5), then let the EA re-scan. This is safe, and already-imported trades won't duplicate.

**A large history import feels slow, or the terminal briefly freezes on attach.** That's expected for a big backlog on first attach. It batches up to 200 trades per request rather than sending one at a time, so even a few hundred trades should finish in well under a minute.

---

*Nothing on this page is financial advice. Trade your own account, manage your own risk.*
