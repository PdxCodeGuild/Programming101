'''
Programming 101
Unit 3 Review
'''

# datatype: boolean (bool)
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# booleans are Capitalized in Python
# a = false # NameError: name 'false' is not defined

# ---------------------------------------------------------------------------------- #

# all datatypes have typecasting functions
# str(), int(), float()

# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# If an object has value, it will convert to True
# If an object has NO value, it will convert to False


x = 0 # zero has no value - False
y = 1 # 1 (or any number other than zero) has value - True

x = '' # blank string has no value - False
y = 'a' # string with at least one character has value - True

x = [] # blank list has no value
y = ['a'] # list with at least one item has value

# print(bool(x), bool(y))
# -------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean
# all comparisons need two sides

x = 5
y = 5

# print(x == y)  # == equality - True
# print(x != y)  # != inequality - False

# print(x < y)  # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y)  # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True

# ------------------------------------------------------------------------------------ #

# other datatypes can be compared
word_1 = 'cat'
word_2 = 'dog'

# print(word_1 == word_2) # False
# print(word_1 == 'cat' and word_2 == 'dog') # True

# avoid < and > with datatypes other than numbers (at least for now)
# print('a' < 'A') # False (confusing)

# checking for alphabetical order
# print('h' < 'w')

# ---------------------------------------------------------------------------------- #

# Logical Operators - combine two comparisons and result in a single boolean
# and, or, not

# all logical statements needs two comparisons

x = 2
y = 10

# and - True only if BOTH comparisons are True
# print(x == 2 and y == 10)  # True - both comparisons result in True
# print(x < 0 and y == 10) # False - left comparison (x < 0) results in False

# or - True if at least ONE comparison is True
# print(x < 0 or y == 10) # True - right comparison (y == 10) results in True
# print(x < 0 or y < 0) # False - both comparisons result in False

# ----------------------------------------------------------------------------------------- #

# not - flip a boolean

# 'not' works in front of any code that produces a boolean
# .isnumeric() - string method which returns a boolean indicating if the string is all numbers or not

string = '12a34'
# print(string.isnumeric()) # False
# print(not string.isnumeric()) # True

# ----------------------------------------------------------------------------------------- #

# 'not' with Truthy/Falsey

word = ''

# These two lines both check if the 'word' variable contains a blank string
# print(word == '') # True
# print(not word) # True


# ------------------------------------------------------------------------------------------------ #

# Conditional Statements - run different 'code blocks' based on the outcome of comparisons
# keywords: if, elif, else

# code block - A section of code that executes together.
#              In Python, code blocks are defined using horizontal indentation

'''
Conditional Statements
----------------------
- must start with an if
- every single if will be checked
- elif will only be checked if the preceding if and other elifs were False
- else will run if all other conditions were False
- if/elif will only be checked until a True condition is found
'''

'''
if/elif combos
--------------
if
if / else
if / elif
if / elif / else
if / elif / elif / ... / elif
if / elif / elif / ... / else
'''
# ------------------------------------------------------------------------------- #

'''
# ask the user for a color
color = input('Enter a color: ')

if color == 'green' or color == 'yellow':
    output = f"I like the color '{color}'!"

elif color == 'blue' or color == 'orange':
    output = f"{color.upper()}!!!"

elif 'p' in color:
    output = f"The color {color} contains the letter 'p'."

# elif color == '':
elif not word: # same as line 155
    output = "Color cannot be blank!"

else:
    output = f"I'm indifferent to the color '{color}'..."


print(output)
'''

# ----------------------------------------------------------------------------------- #

# 'nested conditionals' - conditionals within the code block of other conditionals

'''
# avoid repeating x < 10 using a nested conditional
if x < 10 and x < 5:
    # ... do something
elif x < 10 and x == 5:
    # ... # do something
elif x < 10 and x > 5:
    # ... # do something
    
'''
x = 15

if x < 10:
    output = f"{x} is less than 10"

    if x == 5:
        output += ' and x is 5'

    elif x < 5:
        output += f" and {x} is less than 5."

    elif x > 5:
        output += f" and {x} is greater than 5."


else:
    if x == 10:
        output = "x is 10"

    elif x > 10:
        output = f"{x} is greater than 10"

# print(output)