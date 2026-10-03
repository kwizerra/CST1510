# Week 2 — Extra Practice Projects

Optional. Beyond the lab — classic beginner projects, adapted from Angela
Yu's *100 Days of Code*, trimmed to use only what's been taught by this
week: `input()`, comparisons, `if`/`elif`/`else`, `while`, and `for`/`range`.
No lists, no functions, no `random` module yet — those come in Weeks 3–4.

---

## Python Pizza

**Uses:** `input()`, arithmetic, `if`/`elif`/`else`

Small pizza (S): $15. Medium (M): $20. Large (L): $25.
Pepperoni on a small: +$2. Pepperoni on medium/large: +$3.
Extra cheese, any size: +$1.

1. Ask what size pizza, what topping choices, using `input()`.
2. Work out the final bill from the choices.
3. Print `Your final bill is: $<amount>.` — get the wording and the
   trailing full stop exactly right.

*Adapted from: 100 Days of Code, Day 3.*

---

## Treasure Island

**Uses:** `input()`, nested `if`/`else`

A "choose your own adventure" text game. At each step, ask the player a
question (e.g. "left or right?") and use `if`/`else` — nested where a
choice only makes sense after an earlier one — to branch the story
towards different endings ("you found the treasure" / "you got eaten by
a dragon" / ...). Plan the branches on paper first before writing the
`if`s.

*Adapted from: 100 Days of Code, Day 3.*

---

## Higher or Lower

**Uses:** `while`, comparisons, `if`/`else`

The original game compares two things and asks which is higher. A
trimmed version for this week:

1. Store two things to compare as variables (e.g. two accounts and their
   follower counts) — hard-code them for now.
2. Ask the user which one they think is higher.
3. Compare their guess with `if`/`else` and print "Correct" or "Wrong".
4. Wrap it in a `while` loop so they can play again — stop when they type
   `"quit"`.

*Adapted from: 100 Days of Code, Day 14 (trimmed — the real version picks
two random accounts from a list, which needs Week 3's `random` module and
Week 4's lists).*

---

## Number Guessing Game

**Uses:** `while`, comparisons, `if`/`elif`/`else`

1. Pick a secret number and store it in a variable (hard-code it for now
   — no `random` yet).
2. Loop: ask the user to guess. If their guess is too high, say so. Too
   low, say so. Correct, congratulate them and stop the loop.
3. Count how many guesses it took.

**Revisit this in Week 3:** once you've met the `random` module, swap the
hard-coded secret number for `random.randint(1, 100)` — same game, now a
different number every time.

*Adapted from: 100 Days of Code, Day 12.*

---

Stuck on why a loop never stops? That's `03 - while Loops`, section 4,
"THE INFINITE LOOP", in this folder.
