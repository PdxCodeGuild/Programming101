'''
Programming 101
Unit 4
'''

import random

'''
datatype: list (list)

'Ordered' and 'changeable' sequences of items.
Items are separated with commas ,
Lists are defined using square brackets []

Since lists are 'ordered', their items can be retrieved using their positions in the list.
An item's position in the list is called its 'index' (indices plural)
'''

# define an empty list
empty_list = []
# print(empty_list, type(empty_list)) # [] <class 'list'>

# --------------------------------------------------------------------------------------- #

numbers = [22, -11, 33, -44] # list of integers
colors = ['yellow', 'cyan', 'magenta'] # list of strings

# list items can be ANY datatype, including other lists
jumble = ['cat', False, 3.14, 99, None, [1, 2, 3]]
# print(jumble) # ['cat', False, 3.14, 99, None, [1, 2, 3]]

# ------------------------------------------------------------------------------------- #

# list items can be organized vertically as well
colors = [
    'yellow',
    'cyan',
    'magenta'
]
# print(colors) # ['yellow', 'cyan', 'magenta']

# ------------------------------------------------------------------------------------- #

# retrieve an item from the list using its index
# place the index in square brackets after the list or its variable name

# list indices always start at 0
# print(colors[0]) # yellow
# print(colors[1]) # cyan
# print(colors[2]) # magenta

# can't use indices that don't exist
# print(colors[3]) # IndexError: list index out of range

# the last index in the list is one less than the list's length
# an item's index is one less than its position

# -------------------------------------------------------------------------------------- #

# Python allows negative indices
# print(colors[-1]) # magenta
# print(colors[-2]) # cyan
# print(colors[-3]) # yellow

# can't use indices that don't exist
# print(colors[-4]) # IndexError: list index out of range

# ------------------------------------------------------------------------------------- #

# strings are 'ordered' sequences as well
# indices can be used to access their characters

letters = 'ABCDEFG'
# print(letters[0]) # 'A'

# strings are NOT changeable
# letters[0] = 'Z' # TypeError: 'str' object does not support item assignment

# to change a string, we need to create a new string with the changes
# letters = letters.replace('A', 'Z')
# print(letters) # ZBCDEFG

# typecast the string as a list in order to change its items
letters = list(letters) # convert to list

# lists ARE changeable
letters[0] = 'Z' # change the first item

letters = ''.join(letters) # join the list back into a string
# print(letters)

# ------------------------------------------------------------- #

colors[0] = 'teal'
# print(colors) # ['teal', 'cyan', 'magenta']

# cannot add items this way
# colors[3] = 'purple' # IndexError: list assignment index out of range

# ------------------------------------------------------------- #

# add items to the list using list methods

# .append(item) - add a single item to the END of the list
colors.append('purple')
# print(colors) # ['teal', 'cyan', 'magenta', 'purple']

# .insert(index, item) - add the item at the index
colors.insert(1, 'pink')
# print(colors) # ['teal', 'pink', 'cyan', 'magenta', 'purple']

# .extend(sequence) - add the items from the sequence to the end of the list
colors.extend(['yellow', 'teal', 'maroon'])
# print(colors) # ['teal', 'pink', 'cyan', 'magenta', 'purple', 'yellow', 'teal', 'maroon']

# ------------------------------------------------------------------------------------------- #

# .remove(item) - remove the first occurrence of the item from the list
colors.remove('teal')
# print(colors) # ['pink', 'cyan', 'magenta', 'purple', 'yellow', 'teal', 'maroon']

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided
# color = colors.pop() # remove the last item
# print(color, colors) # maroon ['pink', 'cyan', 'magenta', 'purple', 'yellow', 'teal']

# colors.pop(1)
# print(colors) # ['pink', 'magenta', 'purple', 'yellow', 'teal']

# ------------------------------------------------------------------------------------------ #

# random.choice(sequence) - return a random selection from the sequence

# select a random color from the colors list
random_color = random.choice(colors)
# print(random_color)

ABCs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_letter = random.choice(ABCs)
# print(random_letter)

# ------------------------------------------------------------------------------------------ #

# loop - a code block that repeats until a certain condition is met

# 'for' loop

# for item in sequence - loop through each item in a sequence

'''
for/in - Python operators
item - variable with an arbitrary name which will hold each item from the sequence as it's visited
sequence - iterable (loopable) object (list, string, etc...) through which to loop
'''

colors = ['pink', 'cyan', 'magenta', 'purple', 'yellow', 'teal', 'maroon']

'''
for color in colors:
    print(color)
'''

# --------------------------------------------------------------------------------- #


counter = 1 # to label the colors

for color in colors:
    output = f"{counter}. {color.capitalize()}"
    
    # print(output)

    # increment the counter each loop to increase the label number
    counter += 1

# ------------------------------------------------------------------------------------ #


# use a string as a sequence for looping

# define a list of vowels
vowels = ['A', 'E', 'I', 'O', 'U']

# loop through all the letters in the alphabet
for letter in ABCs:
    # check if the current letter is a vowel
    if letter in vowels:
        output = letter

    else:
        output = '...'

    # print(output)

# ------------------------------------------------------------------------------------------ #

# for x in range() - loop a certain number of times

# range(stop_value) - return a range of numbers from 0 to stop_value-1

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
for number in range(10):
    print(number)
    
'''

# ------------------------------------------------------------------------------------- #

# generate a list of 10 random integers between 0 and 100

# blank list of numbers
numbers = []

# loop 10 times
for x in range(10):
    # generate a random integer
    random_number = random.randint(0, 100)

    # add the number to the list
    numbers.append(random_number)

    # print(numbers) # print the list after each item is added

# print the list after the loop has ended
# print(numbers)


# -------------------------------------------------------------------------------- #

powers_of_2 = []

# generate a list of the powers of 2 from 0 to 10

for exponent in range(11):
    # raise 2 to the power of 'exponent' and add it to the list
    powers_of_2.append(2 ** exponent)

# print(powers_of_2)