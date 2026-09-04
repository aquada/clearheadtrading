---
title: "CHT Journal — User Guide"
description: "How to set up and use CHT Journal: logging trades, reviews, the dashboard, and guardrails."
url: "/journal/user-guide/"
ShowToc: true
---

## What it is

CHT Journal is a trade journal and performance analytics tool, and it's built around one idea: R first, dollars second. Log a win, a loss, a mistake, or how you felt going into a trade, and it gets measured as a multiple of what you risked instead of a dollar figure, so a trader risking £50 a trade and one risking £5,000 can compare their real edge on the same scale.

Staying profitable takes three things at once — an edge, risk sizing that survives a losing streak, and the discipline to execute both under pressure — and CHT Journal is built to make all three visible, not just to total up your P&L. That third one is the one most journals skip, so emotion, confidence, and mistakes get logged as fields next to the trade itself rather than left to memory, because they're usually the ones quietly deciding whether the other two hold up.

## Getting started

Sign up, then set your timezone correctly before you go any further. Every stat that buckets by day, week, or session runs off it, and correcting a month of trades logged against the wrong timezone is a lot more fiddly than fixing it up front.

You'll then land in a short setup wizard:

- An optional leaderboard opt-in, ranked by average R-multiple, never by P&L or account size — nobody can see your account size
- A quick R-multiple explainer
- Your trade log detail level: Simple, Normal, or Strict (below)
- Optional setup tags for your own trading strategies or patterns — start with none and add only what you use
- A choice between trying it out with 25 trades of realistic sample data, or logging your first real trade straight away

You can reopen this wizard from Settings any time you want to change something.

## Logging a trade

There are three ways to get trades in:

1. **Manual entry** — the trade form, one trade at a time
2. **CSV / MT4 report import** — a bulk import from a broker export
3. **EA auto-sync** — closed trades push in automatically from your MT4/MT5 terminal, on the Paid tier. See the [EA Auto-Sync Setup](/journal/ea-setup/) guide.

### Trade log detail: Simple, Normal, Strict

How much you log per trade is up to you, and it's changeable in Settings whenever you like.

| | Simple | Normal | Strict |
|---|---|---|---|
| Instrument, direction, entry/exit, size, R, P&L | Shown | Shown | Shown |
| Setup | Shown | Shown | Required |
| Notes | Shown | Shown | Shown |
| Mistake, emotion, confidence | Hidden | Shown | Required |
| Entry / exit / trade-management ratings | Hidden | Shown | Required |
| Thesis, lesson learned, followed-my-plan, MAE/MFE | Hidden | Shown | Shown (never required) |

- **Simple** — price in, price out, for anyone who just wants a P&L log without the behavioural work.
- **Normal** — everything shown, nothing forced. This is the default.
- **Strict** — nothing saves until setup, mistake, emotion, confidence, and all three post-trade ratings have been logged deliberately. For traders who want the habit enforced rather than left optional.

### R-multiple

What you made or lost, expressed as a multiple of what you risked. Risk £100 and make £200, and that's +2R regardless of account size or instrument, which is why the equity curve, the streaks, and the trading score are all built around R rather than currency.

## Reviewing your trades

Two review systems work alongside each other here.

**Per-trade review.** History shows which trades still need review — no setup, mistake or emotion tag, notes, or plan-adherence marked. Click "Start review" and it jumps straight into the first one, and saving takes you straight to the next, so working through a backlog doesn't mean returning to History and reopening each trade by hand.

**Period reviews.** Reviews has three always-on cards — Today, This week, This month — each with a short set of reflection prompts and a 1–5 process rating. If a day gets missed, "Backfill a past review" opens (or creates) the entry for any past day, week, or month.

## Dashboard and stats

The Dashboard leads with your Trading Score, weighted 40% process, 30% consistency, and 30% expectancy, and surfaces:

- Win rate, average win versus average loss, profit factor, Sharpe (R)
- An equity curve, toggled between R and P&L
- Streaks — your current win/loss streak, plus process streaks: days of daily reviews, days of full rule adherence, days of logging how you felt, all running in parallel
- R by time of day, R by how you felt, R by process score
- A 12-week calendar heatmap

Stats goes deeper still, with cost-of-mistake and cost-of-emotion breakdowns and session or day-of-week performance.

## Guardrails

A few optional guardrails live in Settings:

- **Max daily loss (R)** — a warning banner on the trade form once the day's losses reach this
- **Max consecutive losses** — the same, once a losing streak reaches this length
- **Oversize warning** — flags a trade whose size looks unusually large against your typical size

None of these block a trade from being logged. They're a nudge, not a lock.

## Prop firm challenges

Trading a prop firm challenge? Enable the module in Settings and attach trades to a specific challenge to track it separately from your main journal.

## Feedback

Spotted something wrong, or got an idea for what's missing? Use the Feedback link in the app sidebar, which opens the contact form.

---

*Nothing on this page is financial advice. Trade your own account, manage your own risk.*
