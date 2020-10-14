'''
Unit 3

- Operators
    - Arithmetic
    - Assignment/Re-assignment
    - comparison
    - logical
- datatype: boolean
    - True/False
- Conditional statements
    - if / elif / else
'''

x = 17 # assignment operator
y = 6

# Arithmetic operators
# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # 'regular' division - returns a float
# print(x // y) # 'floor' division - always rounds down (cuts off the decimal)
# print(x ** y) # exponentiation - x^y
# print(x % y) # remainder after division

# modulus is good for finding even/odd
# print(562934937 % 2) # 1 - odd
# print(598394834 % 2) # 0 - even



num_of_interested = 20
drop_outs = 6
total_attendees = num_of_interested - drop_outs

attendance_rate = (total_attendees / num_of_interested) * 100

# print(f'''
# There were {num_of_interested} people interested in going hiking
# but {drop_outs} dropped out. Now there will be {total_attendees} people going hiking!
# That's an attendance rate of {attendance_rate}%.
# ''')

# ---------------------- #

x = 5
x + 3

# print(x + 3) # 8 - uses the value of x, but doesn't change it
# print(x) # 5 - x is still 5

x = x + 3 # overwrite the value of x with its previous value (5) + 3
# print(x) # 8

# re-assignment operators
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3
x %= 3 # x = x % 3

# ------------------------- #

# Datatype: Boolean
# True/False

a = True
b = False
# print(a, b) # True, False

# ------------------------- #

# Comparison operators (compare 2 or more values)

x = 5
y = 5

# print(x == y) # True - equality
# print(x != y) # False - inequality
# print(x < y) # False - less than
# print(x <= y) # True - less than or equal to
# print(x > y) # False - greater than
# print(x >= y) # True - greater than or equal to

# can also compare strings
word1 = 'cat'
word2 = 'dog'

# print(word1 == word2) # False
# print(word1 != word2) # True

# beware when using <, <=, >, >= with strings
# print(word1 < word2) # True - word1 starts with 'c' and word2 starts with 'd'

# -------------------------------- #

# Logical operators - combine (compare) comparisons
# and / or / not

# and - returns True only if BOTH sides are True
'''
4<5  and 5<6
True and 5<6
True and True
True

5 < 4 and 1 < 2
False and 1 < 2
False and True
False
'''

# print(1 == 1 and 2 == 2) # True
# print(1 == 0 and 2 == 2) # False
# print(True and True) # True
# print(True and False) # False

# or - returns True if at least ONE side is True
# print(1 == 0 or 1 == 1) # True
# print(1 == 0 or 2 == 1) # False
# print(True or False) # True
# print(False or False) # False

'''
2 > 5  or 4 > 6
False or 4 > 6 
False or False
False   

5 < 4 or 1 < 2
False or 1 < 2
False or True
True
'''

# not - returns the opposite of the result
# print(1 == 1) # True
# print(not 1 == 1) # False

# logical comparisons can be combined
# print((1 == 1 and 1 < 10) and (500 < 300 or 1 < 5) or (100 < 13 or 1 == 1 )) # True
# print(not ((1 == 1 and 1 < 10) and (500 < 300 or 1 < 5) or (100 < 13 or 1 == 1 ))) # False

# ------------------------- # 

# Conditional statments
# if / elif / else

x = 4
y = 10

# if/elif/else statements MUST start with if
if x < y:
    # everything in this 'code block'
    # will run if x is less than y
    # code blocks are denoted by INDENTATION
    message = 'x is less than y'
elif x > y:
    message = 'x is greater than y'
# elif some_other_condition:
# elif yet_another_condition:
# as many elifs as you want
else:
    # else block will run 
    # if no other condition was True
    message = 'x is equal to y'

# print(message)

# ------------------ #

# Guess the number

# set a secret number
secret = 5

# ask the user for a guess
guess = input("Guess a number between 1 and 10: ")

# guess must be converted to integer before comparing
guess = int(guess)

# compare the guess with the secret
if guess == secret:
    result = f'You guessed the secret, {secret}!'
elif guess < secret:
    result = f'Your guess ({guess}) was too low! The secret was {secret}!'
elif guess > secret:
    result = f'Your guess ({guess}) was too high! The secret was {secret}!'

print(result)
