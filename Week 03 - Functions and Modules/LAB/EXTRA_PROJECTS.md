# Week 3 — Extra Practice Projects

---

## Rock, Paper, Scissors

**Uses:** functions, `return`, `random.randint()`

1. At the top of your file, write `import random`.
2. Define a function called `get_computer_choice()`.
3. Inside it, create a variable `number` and set it to `random.randint(0, 2)`.
4. Use `if`/`elif`/`else` to check `number`:
   - if it is `0`, return `"rock"`
   - if it is `1`, return `"paper"`
   - otherwise, return `"scissors"`
5. Define a function called `decide_winner(user_choice, computer_choice)`.
6. Inside it, if `user_choice` equals `computer_choice`, return `"draw"`.
7. Add an `elif` that returns `"user"` if the user wins
   (rock beats scissors, paper beats rock, scissors beats paper).
8. Add an `else` that returns `"computer"`.
9. Outside the functions, use `input()` to ask the user for their choice
   and store it in a variable called `user_choice`.
10. Call `get_computer_choice()` and store the result in `computer_choice`.
11. Print the computer's choice.
12. Call `decide_winner(user_choice, computer_choice)` and store the result
    in `winner`.
13. Print who won.

---

## Calculator

**Uses:** functions, parameters, `return`, calling one function from another

1. Define a function `add(n1, n2)` that returns `n1 + n2`.
2. Define a function `subtract(n1, n2)` that returns `n1 - n2`.
3. Define a function `multiply(n1, n2)` that returns `n1 * n2`.
4. Define a function `divide(n1, n2)` that returns `n1 / n2`.
5. Use `input()` to ask for the first number. Convert it with `float()` and
   store it in `n1`.
6. Create a variable `keep_going` and set it to `True`.
7. Start a `while keep_going:` loop.
8. Inside the loop, ask for an operator (`+ - * /`) and store it in
   `operator`.
9. Ask for the second number, convert it with `float()`, and store it in `n2`.
10. Use `if`/`elif` to call the matching function and store the answer in
    `result`. For example, if `operator == "+"`, then `result = add(n1, n2)`.
11. Print the calculation and the result.
12. Ask the user: `"Type 'y' to continue with the result, or 'n' to start over:"`
13. If they type `"y"`, set `n1 = result`.
14. Otherwise, ask for a new first number and store it in `n1`.

**Extension, once you've done Week 4:** replace the `if`/`elif` in step 10
with a dictionary:
`operations = {"+": add, "-": subtract, "*": multiply, "/": divide}`
Then call `result = operations[operator](n1, n2)`.

---

## Number Guessing Game, upgraded

**Uses:** `random.randint()`

1. Open your Week 2 guessing game.
2. Add `import random` at the top of the file.
3. Find the line where you set the secret number.
4. Replace the fixed number with `random.randint(1, 100)`.
5. Run the game a few times and check that the secret number changes each time.

---

Stuck on why a function returning nothing gives you `None`? That's
`01 - Defining and Calling Functions`, section 4, in this folder.