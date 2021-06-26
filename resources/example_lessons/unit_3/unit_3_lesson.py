'''
Programming 101
Unit 3
'''

# datatype: boolean (bool)
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# in Python, booleans are Capitalized
# b = true  # NameError: name 'true' is not defined

# ----------------------------------------------------------------------------- #

# Comparison operators - compare two pieces of data and result in a boolean
# all comparisons need TWO sides

x = 5
y = 5

# print(x == y) # == check equality - True
# print(x != y) # != check inequality - False

# print(x < y)  # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y)  # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True

# --------------------------------------------------------------------------- #

# other datatypes can be compared as well

word_1 = 'cat'
word_2 = 'cat'

# print(word_1 == word_2) # True

# -------------------------------------------------------------------------- #

# Logical operators - combine two comparisons and resuilt in single boolean
# and, or, not

x = 5

# and - True only if BOTH comparisons are True
# print(x == 5 and x < 10) # True - both comparisons are True
# print(x == 2 and x < 10)  # False - left comparison (x == 2) is False

# or - True if at least ONE comparison is True
# print(x == 2 or x < 10) # True - right comparison (x < 10) is True
# print(x == 2 or x > 10) # False - both comparisons are False

# not - flip a boolean
# print(x > 0) # True
# print(not x > 0) # False

# print(not False) # True

# 'not' is often used with the keyword 'in' to determine if an item is 'in' a sequence
# 'in' will result in a boolean

# print('k' in 'book') # True
# print('z' not in 'book') # True

# -------------------------------------------------------------------------------- #

# Conditional Statements - run different 'code blocks' based on the outcome of comparisons
# keywords: if, elif, else

'''
Code block - a section of code that executes together.
             In Python, code blocks are defined using horizontal indentation


-------------------------------------------------------------------------------

Conditional Statements:

- must start with an if
- every single if will be checked
- elif will only be checked if the preceding if and other elifs were False
- else will run if all other conditions were False

- if/elif will only be checked until a True condition is found
'''

# -------------------------------------------------------------------------- #

light_switch = "DIM"

if light_switch == "ON": # colon signifies the start of a code block
    # first line of a code block sets the indentation for the block
    # all other lines in the code block must match the first line's indentation
    message = "I can see!"

elif light_switch == "DIM":
    message = "The light is dim."

elif light_switch == "OFF":
    message = "It's dark in here!"

# print(message)

# -------------------------------------------------------------------------------- #

x = 10
y = 10

if x < y:
    output = f"{x} is less than {y}"

elif x == 14:
    output = "x is 14"

elif x > y:
    output = f"{x} is greater than {y}"

else: # else doesn't require a condition because it catches all other cases
    output = f"x and y are both {x}"

# print(output)

# --------------------------------------------------------------------------------------- #

import random

# Guess the Number 1 - 10

# set a secret number
# secret = 5
secret = random.randint(1, 10) # generate a random integer between 1 and 10

# ask the user for a guess
guess = input("Please guess a number 1 - 10: ")

# convert guess to integer
guess = int(guess)

# check the guess
if guess == secret:
    print(f"Congratulations! You guessed the secret number: {secret}!")

elif guess < secret: 
    print(f"Oops! Your guess of {guess} was too low! The secret was {secret}...")

elif guess > secret:
    print(f"Oops! Your guess of {guess} was too high! The secret was {secret}...")