---
title: "CHT Journal — User Guide"
description: "How to set up and use CHT Journal: logging trades, reviews, the dashboard, and guardrails."
url: "/journal/user-guide/"
ShowToc: true
---

## What it is

CHT Journal is a trade journal and performance analytics tool, and it's built around one idea: R first, dollars second. Log a win, a loss, a mistake, or how you felt going into a trade, and it gets measured as a multiple of what you risked instead of a dollar figure, so a trader risking £50 a trade and one risking £5,000 can compare their real edge on the same scale.

Staying profitable takes three things at once — an edge, risk sizing that survives a losing streak, and the discipline to execute both under pressure — and CHT Journal is built to make all three visible, not just to total up your P&L. That third one is the one most journals skip, so your emotion at entry and afterwards, confidence, and mistakes get logged as fields next to the trade itself rather than left to memory, because they're usually the ones quietly deciding whether the other two hold up.

## Getting started

Sign up, then set your timezone correctly before you go any further. Every stat that buckets by day, week, or session runs off it, and correcting a month of trades logged against the wrong timezone is a lot more fiddly than fixing it up front.

You'll then land in a short setup wizard:

- An optional leaderboard opt-in. The leaderboard is a future feature: tick it now and you'll be included when it opens. It will rank by average R-multiple, never by P&L or account size
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
| Mistake, emotion at entry, confidence | Hidden | Shown | Required |
| Emotion afterwards | Hidden | Shown | Shown (never required) |
| Entry / exit / trade-management ratings | Hidden | Shown | Required |
| Thesis, lesson learned, followed-my-plan, MAE/MFE | Hidden | Shown | Shown (never required) |

- **Simple** — price in, price out, for anyone who just wants a P&L log without the behavioural work.
- **Normal** — everything shown, nothing forced. This is the default.
- **Strict** — nothing saves until setup, mistake, emotion at entry, confidence, and all three post-trade ratings have been logged deliberately. For traders who want the habit enforced rather than left optional.

### R-multiple

What you made or lost, expressed as a multiple of what you risked. Risk £100 and make £200, and that's +2R regardless of account size or instrument, which is why the equity curve, the streaks, and the trading score are all built around R rather than currency.

### Emotion at entry and afterwards

There are two emotion fields, because how a trade felt going in and how it left you feeling are different things.

- **Emotion at entry** is how you felt going in, before you knew the result. If you're logging a trade later, such as one that came in by import or auto-sync, go back to that moment rather than how it feels now.
- **Emotion afterwards** is how the trade left you feeling once it was closed. It sits in the post-trade review section and it's optional.

A clean trade that loses can feel very different by the time you sit down to review it. Keeping the two apart stops that feeling rewriting how you felt when you took it.

### Followed my plan

Answer Yes or No, or leave it blank if you haven't decided. A blank answer shows as "Not marked" and isn't counted as breaking your plan, and it doesn't end your rule adherence streak. Click the selected answer again to clear it.

### Managing your tags

Setup, emotion, and mistake tags can all be changed in Settings.

- **Setup tags** start empty. Add the setups you actually trade.
- **Emotion tags** have separate lists for at entry and afterwards. Remove the ones you don't use and add up to 12 of your own to each.
- **Mistake tags** work the same way, also with up to 12 of your own. "None" always stays, because it's how your stats know a trade had no mistake.

Anything new you type under "Other" is added to your list when you save the trade, as long as you have room. Removing a tag only takes it off the form: trades already using it keep it. Removed emotion and mistake tags can be put back.

For emotions afterwards, you can mark your own tags as "felt bad". The Dashboard uses that when it counts clean losses that left you feeling bad.

In Simple mode the emotion and mistake lists are hidden, since those fields aren't on the form.

## Reviewing your trades

Two review systems work alongside each other here.

**Per-trade review.** History shows which trades still need review — no setup, mistake or emotion tag, notes, or plan-adherence marked. Click "Start review" and it jumps straight into the first one, and saving takes you straight to the next, so working through a backlog doesn't mean returning to History and reopening each trade by hand.

**Period reviews.** Reviews has three always-on cards — Today, This week, This month — each with a short set of reflection prompts and a 1–5 process rating. If you've logged emotions for that period, the card lists them too, at entry and afterwards. If a day gets missed, "Backfill a past review" opens (or creates) the entry for any past day, week, or month.

## Dashboard and stats

The Dashboard leads with your Trading Score, weighted 40% process, 30% consistency, and 30% expectancy, and surfaces:

- Win rate, average win versus average loss, profit factor, Sharpe (R)
- An equity curve, toggled between R and P&L
- Streaks — your current win/loss streak, plus process streaks: days of daily reviews, days of full rule adherence, days of logging how you felt at entry, all running in parallel. Streaks always cover your whole history, whichever range you've picked
- Clean losses: of the trades that lost even though you followed your plan with no mistake, how many left you feeling bad. It appears once you have three with an emotion logged afterwards
- R by time of day, R by how you felt at entry, R by process score
- A calendar heatmap of your daily results

The 30D, 60D, 90D and All buttons set how far back the rest of the Dashboard and Stats look.

Stats goes deeper still, with cost-of-mistake and cost-of-entry-emotion breakdowns and session or day-of-week performance. Two sections compare how you trade when you stick to the plan and when you don't:

- **Disciplined vs off-plan** puts the two side by side: number of trades, win rate, average result, and the emotions you most often logged at entry. Disciplined means you followed your plan with no mistake logged. Off-plan means you broke it or logged a mistake. Trades you haven't marked aren't counted.
- **Disciplined trades by week** shows the share of your marked trades that were disciplined, so you can see whether it's improving. It switches to months once you have more than a year of trades.

Three more look at how trades left you feeling and what came next:

- **Emotion afterwards × process** shows whether you're reacting to how you traded or just to the result.
- **Your next trade** shows how the next trade you opened within 24 hours went, first after a clean win against a clean loss, then by how the last one left you feeling. In a clean trade you followed your plan with no mistake, so any difference between the two is about the result, not how you traded.
- **Entry → afterwards** lists your most common pairs of feelings going in and coming out, with the average result.

They need a fair number of trades before the patterns mean much.

## Guardrails

A few optional guardrails live in Settings:

- **Max daily loss (R)** — a warning banner on the trade form once the day's losses reach this
- **Max consecutive losses** — the same, once a losing streak reaches this length
- **Oversize warning** — flags a trade whose size looks unusually large against your typical size

None of these block a trade from being logged. They're a nudge, not a lock.

## Prop firm challenges

Trading a prop firm challenge? Enable the module in Settings and attach trades to a specific challenge to track it separately from your main journal.

## Feedback

Spotted something wrong, or got an idea for what's missing? Use the Feedback link in the app sidebar, which opens the contact page.

---

*Nothing on this page is financial advice. Trade your own account, manage your own risk.*
