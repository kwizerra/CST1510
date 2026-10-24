
---

## Blackjack, Object-Oriented

**Uses:** classes, `__init__`, methods, `self`

**Starting point:** your Blackjack from Day 11 of *100 Days of Code*
(deal two cards each, hit or stand, dealer plays to 17, compare scores),
built with loose functions like `deal_card()`, `calculate_score(cards)`,
and `compare(user_score, computer_score)`.

### Step 1: Make a copy of your original game
Save your working Day 11 version under a new filename so you can compare
the two when you're done.

### Step 2: Create the `Hand` class
Define a class called `Hand`. In `__init__(self)`, give it one attribute:
an empty list, `self.cards`.

### Step 3: Add an `add_card` method
Inside `Hand`, write `add_card(self)`. It should deal one card and append
it to `self.cards`. Reuse the logic from your old `deal_card()` function.

### Step 4: Add a `score` method
Inside `Hand`, write `score(self)`. It should return the total of
`self.cards`, including the special rules from your old
`calculate_score(cards)`:
- an ace counts as 11, or as 1 if 11 would bust the hand
- two cards totalling 21 is a blackjack

Note that `score` takes no `cards` argument. It reads `self.cards`
instead.

### Step 5: Test `Hand` on its own
Before touching the game loop, create a `Hand`, call `add_card()` a few
times, and print `cards` and `score()` to check they behave correctly.

### Step 6: Decide how to represent the players
Pick one approach:
- **Simpler:** use two `Hand` objects directly, `user_hand` and
  `computer_hand`.
- **Stretch:** write a `Player` class that holds a `Hand` as an
  attribute.

### Step 7: Rewrite the game loop
Replace every place that passes a card list into a function. For
example, `calculate_score(user_cards)` becomes `user_hand.score()`, and
appending `deal_card()` to a list becomes `user_hand.add_card()`. Do the
same for the computer's hand and the dealer-plays-to-17 loop.

### Step 8: Update the comparison
Keep `compare(...)` as a function, but feed it `user_hand.score()` and
`computer_hand.score()`.

### Step 9: Play and compare
Run several games to confirm the rules still work. Then put the two
versions side by side. No Blackjack rules have changed; only where the
data and the logic that acts on it live. They now sit together on one
object, instead of a card list and separate functions that need it
passed in every time.


---

**Want to see this refactor done step by step on a simpler example
first?** See `03 - Many Objects Together` in this folder. Week 8's
`04 - From Functions to a Class` does the same move again on real pulled
data.