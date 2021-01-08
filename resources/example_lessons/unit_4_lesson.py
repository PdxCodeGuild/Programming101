'''
Progamming 101
Unit 4

Lists
for loops
    - for item in sequence
    - for x in range()
'''

'''
Lists

'Ordered' and 'changeable' sequences of items. Items are 
separated by commas and surrounded by square brackets [].

Since they are 'ordered', their items can be referenced
using their position in the list.

An item's position in the list is called its 'index'.
'''

# define a list
blank_list = [] # blank list
# print(blank_list, type(blank_list)) # [] <class 'list'>

numbers = [11, 22, 33, -44] # list of integers
colors = ['red', 'green', 'blue'] # list of strings

# list items can be ANY datatype including other lists
jumble = ['cat', 99, 3.14, True, ['a', 'b', 'c']]

# list items can be organized vertically as well
colors = [
    'red',
    'green',
    'blue', # trailing comma in case we want to reorder items
]

# print(colors)

# items can be referenced using their indices
# print(colors[0]) # red - first index is 0
# print(colors[1]) # green
# print(colors[2]) # blue

# can't reference indices that don't exist
# print(colors[3]) # IndexError - index too far right

# last index in the list is one less than the length of the list

# Python allows negative indices
# print(colors[-1]) # blue - negative indices start from the right
# print(colors[-2]) # green
# print(colors[-3]) # red
# print(colors[-4]) # IndexError - index too far left

# change the value at an index
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# cannot assign values to indices that don't exist
# colors[40] = 'purple' # IndexError: list assignment index out of range

# ----------------------------------------------------- #

# add items using list methods

# .append(item) - add the item to the END of the list
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) - add the item at the given index
colors.insert(0, 'green')
# print(colors) # ['green', 'red', 'yellow', 'blue', 'purple']

# .extend(new_list) - add the new_list to the end of the old list
colors.extend(['teal', 'red'])
# print(colors) # ['green', 'red', 'yellow', 'blue', 'purple', 'teal', 'red']

# ---------------------------------------------------- #


# deleting items with list methods

# .remove(item) - remove the first occurrence of the item
colors.remove('red')
# print(colors) # ['green', 'yellow', 'blue', 'purple', 'teal', 'mauve', 'red']

# .pop(index) - remove the item at the index
# colors.pop() # if no index is provided, .pop() will remove the LAST item
colors.pop(0)
# print(colors) # ['yellow', 'blue', 'purple', 'teal', 'mauve', 'red']

# --------------------------------------------------- #

# .sort() - sort list items IN PLACE

# colors.sort() # goes into the colors list and sorts it

# ------------------------------------------------------ #

# .reverse() reverses the order of the list items IN PLACE
# print(colors) # ['yellow', 'blue', 'purple', 'teal', 'mauve', 'red']
colors.reverse()
# print(colors) # ['red', 'mauve', 'teal', 'purple', 'blue', 'yellow']

# -------------------------------------------------------- #

import random

# random.choice(sequence) - make a random selection out of a sequence
# print(random.choice(colors))

letters = 'abcdefghijklmnopqrstuvwxyz'
# print(random.choice(letters))

# -------------------------------------------------------- #

'''
Unit 4
for loops
'''

# a loop is a code block that repeats until a certain condition is met

# for item in sequence
colors = ['red', 'mauve', 'teal', 'purple', 'blue', 'yellow']

# item - arbitrary variable name that hold each item as it comes out of the list
# sequence - items through which to be looped

for color in colors:
    output = f'color: {color.upper()}'

    # print(output)

# ------------------------------------------------ #

letters = 'abcdefghijklmnopqrstuvwxyz'

# use a string as a sequence for looping
for letter in letters:
    output = f'letter: {letter}'
    # print(output)

# ------------------------------------------------ #

# for x in range():

# range(stop) - returns a range of numbers from 0 to stop-1
# list() # typecasting function to convert to list

# print out the range as a list
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    output = f'{x} squared is {x ** 2}'
    # print(output)

# ------------------------------------------------ #