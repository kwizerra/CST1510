# Week 4 — Extra Practice Projects

This week's new tools: lists, dicts, `.get()`, and looping over both. Combine freely with Week 2's
loops and Week 3's functions and `random` module.

---

## Banker Roulette

**Uses:** lists, `random.choice()`, `random.randint()`, `len()`

1. At the top of your file, write `import random`.
2. Create a variable called `friends` and set it to a list of names,
   for example `["Alice", "Bob", "Charlie", "Dana", "Ella"]`.

**Version 1 — `random.choice()`**

3. Call `random.choice(friends)` and store the result in a variable
   called `payer`.
4. Print `payer` along with a message, for example
   `f"{payer} is paying the bill today!"`.

**Version 2 — `random.randint()` and an index**

5. Use `len(friends)` to get the number of names and store it in
   `num_friends`.
6. Create a variable `index` and set it to
   `random.randint(0, num_friends - 1)`.
   (Lists start at index `0`, so the last valid index is one less than
   the length.)
7. Use the index to pick a name from the list: `payer = friends[index]`.
8. Print `payer` with the same message as before.
9. Run both versions a few times and check that a different name can
   come up each time.

*Adapted from: 100 Days of Code, Day 4.*

---

## Password Generator

**Uses:** lists, `random.choice()`, `random.shuffle()`, `for` loops,
string building

1. At the top of your file, write `import random`.
2. Create a list called `letters` containing every letter `a`–`z` and
   `A`–`Z` as separate strings, for example `["a", "b", "c", ...]`.
3. Create a list called `numbers` containing the strings `"0"` to `"9"`.
4. Create a list called `symbols` containing some symbols, for example
   `["!", "#", "$", "%", "&", "(", ")", "*", "+"]`.
5. Use `input()` to ask how many letters the user wants. Convert it with
   `int()` and store it in `nr_letters`.
6. Do the same for symbols, storing the answer in `nr_symbols`.
7. Do the same for numbers, storing the answer in `nr_numbers`.

**Easy version — letters, then symbols, then numbers**

8. Create a variable `password` and set it to an empty string `""`.
9. Write a `for` loop using `range(nr_letters)`. Inside it, add
   `random.choice(letters)` to the end of `password` using `+=`.
10. Write a second `for` loop using `range(nr_symbols)` that does the
    same with `symbols`.
11. Write a third `for` loop using `range(nr_numbers)` that does the
    same with `numbers`.
12. Print `password`.

**Hard version — shuffled order**

13. Create a variable `password_list` and set it to an empty list `[]`.
14. Repeat steps 9–11, but this time use `.append()` to add each random
    character to `password_list` instead of adding it to a string.
15. Call `random.shuffle(password_list)` to mix up the order.
    (Note: `shuffle()` changes the list in place and returns `None`, so
    don't write `password_list = random.shuffle(password_list)`.)
16. Create a variable `password` and set it to `""`.
17. Write a `for char in password_list:` loop that adds each `char` to
    `password`.
18. Print `password`. Run it a few times with the same inputs and check
    the order changes each time.

**Extension:** replace steps 16–17 with one line:
`password = "".join(password_list)`.

*Adapted from: 100 Days of Code, Day 5.*

---

## Blind Auction

**Uses:** dictionaries, `while` loops, looping over `.items()`

1. Create a variable called `bids` and set it to an empty dictionary
   `{}`.
2. Create a variable `keep_bidding` and set it to `True`.
3. Start a `while keep_bidding:` loop.
4. Inside the loop, use `input()` to ask for the bidder's name and store
   it in `name`.
5. Ask for their bid, convert it with `int()`, and store it in `bid`.
6. Add the pair to the dictionary: `bids[name] = bid`.
7. Ask: `"Are there any other bidders? Type 'yes' or 'no':"` and store
   the answer in `other_bidders`.
8. If `other_bidders == "no"`, set `keep_bidding = False`.
9. If they typed `"yes"`, print `"\n" * 100` to push the previous bid off
   the screen, so the next bidder can't see it.
10. Outside the loop, create a variable `highest_bid` and set it to `0`.
11. Create a variable `winner` and set it to `""`.
12. Write a loop: `for name, bid in bids.items():`
13. Inside the loop, use an `if` to check whether `bid > highest_bid`.
    If it is:
    - set `highest_bid = bid`
    - set `winner = name`
14. After the loop, print the winner and their bid, for example
    `f"The winner is {winner} with a bid of £{highest_bid}."`
    Never print anyone else's bid — that's the point of a *blind*
    auction.

*Adapted from: 100 Days of Code, Day 9.*

---

## Coffee Machine

**Uses:** dictionaries, nested dicts, `.get()`, `.items()`, functions
(Week 3), `while` loops

A simulated coffee machine with a fixed menu and finite resources.

**Set up the data**

1. Create a dict called `resources`:
   ```python
   resources = {"water": 300, "milk": 200, "coffee": 100}
   ```
   (Water and milk are in ml, coffee is in g.)
2. Create the menu as a dict of dicts:
   ```python
   MENU = {
       "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
       "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
       "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
   }
   ```

**Write the functions**

3. Define a function called `report()`.
4. Inside it, loop over `resources.items()` and print each resource and
   its amount, for example `water: 300`.
5. Define a function called `is_resource_sufficient(ingredients)`.
6. Inside it, write a loop: `for item, amount in ingredients.items():`
7. Inside the loop, if `amount > resources[item]`:
   - print `f"Sorry, there is not enough {item}."`
   - return `False`
8. After the loop (not inside it), return `True`.
9. Define a function called `make_coffee(drink_name, ingredients)`.
10. Inside it, loop over `ingredients.items()` and subtract each
    `amount` from the matching resource: `resources[item] -= amount`.
11. After the loop, print `f"Here is your {drink_name}. Enjoy!"`

**Write the main loop**

12. Outside the functions, create a variable `machine_on` and set it to
    `True`.
13. Start a `while machine_on:` loop.
14. Inside the loop, ask
    `"What would you like? (espresso/latte/cappuccino):"` and store the
    answer in `choice`.
15. If `choice == "off"`, set `machine_on = False`.
16. Add an `elif choice == "report":` that calls `report()`.
17. Add an `else:`. Inside it, look up the drink with
    `drink = MENU.get(choice)`.
18. If `drink` is `None`, print `"Sorry, that's not on the menu."`
19. Otherwise, call `is_resource_sufficient(drink["ingredients"])`. If it
    returns `True`:
    - print the price using `drink["cost"]`
    - ask the user how much they are paying, convert it with `float()`,
      and store it in `payment`
    - if `payment >= drink["cost"]`, work out
      `change = round(payment - drink["cost"], 2)`, print the change, then
      call `make_coffee(choice, drink["ingredients"])`
    - otherwise, print `"Sorry, that's not enough money. Money refunded."`
20. Run the program and order lattes until the machine runs out of
    something. Check that it tells you what's missing. Then type
    `report` and `off` to test the extra commands.


---

Stuck on `.get()` vs `[]` for a key that might not exist? That's
`02 - Dictionaries`, section 4, in this folder. (Step 17 of the Coffee
Machine uses `.get()` for exactly this reason.)
