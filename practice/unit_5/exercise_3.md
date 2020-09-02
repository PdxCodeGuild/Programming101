# Unit 5 Practice

## **Exercise 3 - Guess the Number**

### **1.1**

Select a number between 1 and 10 to act as a `secret`.

Have the user attempt to `guess` the number.

If they `guess` then `secret`, tell them they win!

If they `guess` a higher number than the `secret`, tell them they guessed too high.

If they `guess` a lower number than the `secret`, tell them they guessed too low.

If they guess a number that isn't between 1 and 10, tell them they were out of bounds.

**Output**

    Guess a number 1-10: 3

    Your guess of 3 was too low!!
    The secret was: 5
    ---

    Guess a number 1-10: 7

    Your guess of 7 was too high!!
    The secret was: 5
    ---

    Guess a number 1-10: 5

    You guessed the secret!
    The secret was: 5

### **1.2**

Generate a random integer between 1 and 10 to act as a `secret` number.

Using a `while` loop, have the game repeat until the user guesses the `secret`.

**Output**

    Guess a number 1-10: 6
    Your guess of 6 was too low!!

    Guess a number 1-10: 9
    Your guess of 9 was too high!!

    Guess a number 1-10: -99
    Invalid guess: -99.

    Guess a number 1-10: 7
    You guessed the secret: 7!

### **1.3**

Allow the user three guesses. If they don't guess the number in three guesses, game over!

Display the number of remaining guesses with each loop.

Invalid guesses shouldn't affect the number of remaining guesses.

**Output**

### Exercise 1 [solution](./solutions/exercise_1_solution.md)

---

## [< Exercise 2](exercise_2.md) | [Exercise 4 >](exercise_4.md)

### [<< Back to Unit 5 Practice](/practice/unit_5/)
