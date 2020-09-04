# Unit 5 Practice Solutions

## Exercise 3 - Guess the Number

### **1.1**

**Solution**

```python
import random

# secret number
secret = 5

# ask the user to guess
guess = input('Guess a number 1-10: ')

# convert guess to integer for comparisons
guess = int(guess)

if guess < 1 or guess > 10:
    message = f'Invalid guess: {guess}.'

# if they guess correctly
elif guess == secret:
    message = f'You guessed the secret!'

# if they guess too high
elif guess > secret:
    message = f'Your guess of {guess} was too high!!'

# if they guess too low
elif guess < secret:
    message = f'Your guess of {guess} was too low!!'

# display result with after a new line
print('\n' + message)
print(f'The secret was: {secret}')
```

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
    ---

    Guess a number 1-10: 400
    Invalid guess: 400

### **1.2**

**Solution**

```python
import random

# random secret number
secret = random.randint(1,10)

# loop until the user guesses the secret
while True:
    # ask the user to guess
    guess = input('\nGuess a number 1-10: ')

    # convert guess to integer for comparisons
    guess = int(guess)

    if guess < 1 or guess > 10:
        message = f'Invalid guess: {guess}.'
        print(message)
        # go to the top of the loop
        continue

    # if they guess correctly
    elif guess == secret:
        message = f'You guessed the secret: {secret}!'

        # display the winning message
        print(message)

        # end the loop
        break

    # if they guess too high
    elif guess > secret:
        message = f'Your guess of {guess} was too high!!'

    # if they guess too low
    elif guess < secret:
        message = f'Your guess of {guess} was too low!!'

    print(message)
```

**Output**

    Guess a number 1-10: 3
    Your guess of 3 was too low!!

    Guess a number 1-10: 7
    Your guess of 7 was too high!!

    Guess a number 1-10: 99
    Invalid guess: 99.

    Guess a number 1-10: 5
    You guessed the secret: 5!

### **1.3**

**Solution**

```python
import random

# random secret number
secret = random.randint(1,10)

# number of guesses
guesses_remaining = 3

# loop until no guesses remain
while guesses_remaining > 0:
    # display the remaining guesses
    print(f'You have {guesses_remaining} guesses remaining.')

    # ask the user to guess
    guess = input('\nGuess a number 1-10: ')

    # convert guess to integer for comparisons
    guess = int(guess)

    if guess < 1 or guess > 10:
        message = f'Invalid guess: {guess}.'
        print(message)
        # go to the top of the loop
        continue

    # if they guess correctly
    elif guess == secret:
        message = f'You guessed the secret: {secret}!'

        # display the winning message
        print(message)

        # end the loop
        break

    # if they guess too high
    elif guess > secret:
        message = f'Your guess of {guess} was too high!!'

    # if they guess too low
    elif guess < secret:
        message = f'Your guess of {guess} was too low!!'

    # if the guess was too high or low,
    # remove a guess
    guesses_remaining -= 1
    print(message)

# when the user runs out of guesses
else:
    print(f'Sorry! You ran out of guesses. The secret was {secret}.')
```

**Output**

    You have 3 guesses remaining.

    Guess a number 1-10: 100
    Invalid guess: 100.
    You have 3 guesses remaining.

    Guess a number 1-10: 10
    Your guess of 10 was too high!!
    You have 2 guesses remaining.

    Guess a number 1-10: 6
    Your guess of 6 was too low!!
    You have 1 guesses remaining.

    Guess a number 1-10: 8
    Your guess of 8 was too low!!
    Sorry! You ran out of guesses. The secret was 9.

## [< Exercise 2](../exercise_2.md) | [Exercise 4 >](../exercise_4.md)

### [<< Back to Unit 5 Practice](/practice/unit_5/)
