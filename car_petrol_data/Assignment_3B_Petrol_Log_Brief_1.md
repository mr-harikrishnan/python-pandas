# Assignment 3B — One Year of a Car, Told in Charts

**Dataset:** `car_petrol_log.csv`
**Tools allowed:** pandas + **pure matplotlib only**. No seaborn, no plotly, no pandas `.plot()` styling shortcuts beyond basic usage. Every axis, tick, label, and annotation must be something you placed deliberately.
**Deliverable:** One Jupyter notebook + a written "story" summary (5–8 sentences).

---

## The situation

This is a **real petrol log** kept by a real car owner for 14 months (June 2025 – July 2026). It was written by hand into a phone note, which means it has all the problems real data has: some columns were only recorded later, some entries were skipped, and one row isn't a refill at all.

Your job is not just to draw charts. Your job is to **find the story in this data and tell it visually**, the way an analyst would present it to the car's owner.

## Part 1 — Load and prepare (20%)

1. Load the CSV. Parse `date` into a proper datetime column. Note the dates are in mixed text formats ("June 1 2025", "Sept 5 2025", "March 1 2026") — handle this in code, not by editing the CSV.
2. Identify every data quality issue you can find and list them in a markdown cell. For each one, state **what you will do about it and why**.
3. Any row you exclude or any value you estimate must be documented with a `# WHY:` comment. A `# WHY:` comment defends a decision — it does not restate the operation.

## Part 2 — Required charts (50%)

All four charts must be built with explicit `fig, ax = plt.subplots()` calls, manual titles, axis labels with units, and readable tick labels.

**Chart 1 — Monthly fuel spend (bar chart).**
One bar per month, value labels on top of each bar (use a loop with `ax.text()` or `ax.annotate()`, not `bar_label` alone). Highlight the highest-spend month in a different color and annotate *why* it might be high (look at the individual fills in that month before you guess).

**Chart 2 — Odometer over time (line chart).**
Plot the odometer reading against date. Your chart must honestly handle the fact that the first 10 refills have **no odometer reading** — decide how to show or exclude that period and defend it in a `# WHY:` comment.

**Chart 3 — Driving intensity (km per day between refills).**
Compute km driven between consecutive odometer readings, divide by days elapsed, and plot it over time. At least **two data points on this chart require an `ax.annotate()` with an arrow** explaining what happened. Finding *which* two points need explanation is part of the assignment.

**Chart 4 — Your story chart (free choice).**
One chart that combines at least two quantities (for example spend vs distance, or cost per km over time) and makes a single clear point. This is the chart you would show the car owner first. A twin-axis chart (`ax.twinx()`) is acceptable if you can defend it.

## Part 3 — Mandatory verification section (20%)

**This section is not optional. An assignment without it is an automatic Redo.**

Write at least **three coded checks** that run and print PASS/FAIL, for example (you may design your own, but they must be real checks against the data, not comments):

- Check that the odometer column is strictly increasing wherever it exists.
- Check that the sum of your monthly spend chart equals the sum of the raw `price_inr` column. If your chart totals don't match the raw data, your chart is lying.
- Check that every km-per-day value is physically plausible for a personal car, and **print any rows that fail**. Then look at the failures and decide: data error, or real event? Your answer goes in the story summary.
- If you compute fuel efficiency (km/l) anywhere, check that every value falls in a plausible range for a petrol car. If any value is impossible, do not delete it silently — explain what caused it.

Run the checks. **Read the output.** If a check fails, that is the assignment talking to you.

## Part 4 — The story (10%)

In 5–8 sentences, written for the car's owner (a non-programmer): What does this car cost to run? How much is it driven? What changed over the year? What can't you know from this log, and why?

## Rules

- Every non-obvious decision needs a `# WHY:` comment.
- Do not invent numbers. If you estimate something (for example litres from price and an assumed petrol rate), state the assumption in the notebook and in the story.
- You will present Chart 3 verbally, without the screen, and explain how you built the annotations and what the two annotated events were.
