---
title: "Entry Execution"
description: "Getting into a trade at the level you planned, not the level emotion talks you into."
section: "Execution"
section_slug: "execution"
order: 4
weight: 4
status: "published"
tags: ["execution", "order types", "entries"]
related: ["managing-the-trade", "risk-to-reward-ratio", "fear-greed-and-fomo"]
---

Planning a trade and getting into it are two different skills, and the gap between them is where a good setup on the chart turns into a mediocre one on the account, because the price filled at rarely matches the price imagined in the plan.

---

## The level you planned vs the level you got

{{< figure src="entry-slippage.png" caption="A limit order fills on the planned level. A market order sent after price has already moved fills further along, at a worse price, the gap known as slippage." >}}

A limit order waits for price to reach the planned level and fills there, or not at all if price never comes back. A market order fills immediately at whatever price is available, which in a fast-moving market can sit meaningfully worse than the level that was planned for. Neither is wrong on its own, but the gap between them is where a chart that looked like a clean setup quietly becomes a worse trade than the one that was analysed.

---

## Order types are part of execution, not a technicality

Choosing between a limit and a market order is itself a planned decision, made before the trade is live, not an afterthought at the moment of entry. A limit order suits a setup where the exact level matters more than certainty of getting filled, a breakout retest, for instance. A market order suits a setup where being in the trade matters more than a few points of price, a fast-moving move that won't wait for a pullback. Picking the wrong one for the situation adds risk the original analysis never accounted for.

A third option, a stop-entry order, sits between the two. It places a market order automatically once price reaches a specified level, useful for a strategy that wants to enter on confirmation of a breakout instead of waiting for a retest that might never come. The trade-off is the same as a plain market order once triggered, the fill can land past the trigger level in a fast move, but it removes the need to be watching the chart at the exact moment the level breaks.

---

## Spreads and slippage widen when it matters most

Execution risk isn't constant through the day. In the seconds around a major scheduled release, the spread on an instrument can widen sharply as liquidity providers pull back, and a market order sent into that window can fill considerably worse than the same order would have a minute earlier or later. A strategy that relies on entering right as a number is released is, in practice, also relying on the platform's execution holding up in the worst possible moment for it to fail, which is one of the reasons a trading plan's rules about avoiding trades around major news exist in the first place.

Every broker's platform behaves slightly differently around these moments, some requote, some widen the spread instead, some do both. A demo account, covered in [Demo vs Live Trading](/learn/foundations/demo-vs-live-trading/), is a reasonable place to see how a specific broker handles a live news release before finding out the hard way with real money at risk.

---

## Chasing a missed entry is a different trade

If the planned level is missed and price runs without it, entering anyway at a level that's merely "close enough" quietly changes the trade's risk-to-reward without touching the stop that was set for the original level. That's not a small variation on the planned trade, it's a new trade with worse numbers, wearing the old plan's name and borrowing its confidence.

---

## Key takeaways

- A limit order fills at the planned level or not at all; a market order fills immediately, sometimes at a meaningfully worse price
- A stop-entry order triggers a market order automatically at a set level, useful for entering on confirmation without watching the chart live
- Choosing an order type is a decision the plan should make in advance, not one made in the moment of entry
- Spreads and slippage are worst in the seconds around major scheduled news, right when a market order is most tempting
- Testing how a specific broker's platform handles execution around news on a demo account beats finding out live
- Chasing a missed level with a "close enough" entry changes the trade's risk-to-reward while the stop stays where it was for a different price

---

*Nothing on this page is financial advice. Trade your own account, manage your own risk.*
