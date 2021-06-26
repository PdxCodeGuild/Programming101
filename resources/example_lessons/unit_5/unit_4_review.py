'''
Programming 101
Unit 4 Review
'''

'''
datatype: list (list)

'Ordered' and 'changeable' sequences of items.
Items are separated with commas ,
Lists are defined using square brackets []

Since lists are 'ordered', their items can be retrieved using their positions in the list.
An item's position in the list is called its 'index' (indices plural)
'''

fruits = ['apple', 'banana', 'orange']
# print(fruits) # ['apple', 'banana', 'orange']

# organized vertically
fruits = [
    'apple',
    'banana',
    'orange'
]

# ------------------------------------------------------------------------------------ #

# because lists are 'ordered', their items can be retrieved using their indices
# list indices start at 0

# print(fruits[0]) # apple
# print(fruits[1]) # banana
# print(fruits[2]) # orange

# step off the right edge of the list
# print(fruits[3]) # IndexError: list index out of range

# ---------------------------------------------------------------------- #

# last index of a list is one less than the list's length
# len(sequence) - return the length of the sequence as an integer

# print(len(fruits)) # 3

last_index = len(fruits) - 1
# print(last_index, fruits[last_index]) # 2 orange

# ----------------------------------------------------------------------------------- #

# Python allows negative indices
# -1 will be the last index in the list

# print(fruits[-1]) # orange
# print(fruits[-2]) # banana
# print(fruits[-3]) # apple

# step off the left edge of the list
# print(fruits[-4]) # IndexError: list index out of range

# ------------------------------------------------------------------------------------------ #

# strings are also 'ordered' sequences

letters = 'ABC'
# print(letters[1]) # B

# strings are NOT 'changeable'
# letters[1] = 'T' # TypeError: 'str' object does not support item assignment

# ------------------------------------------------------------------------------------------ #

# lists are changeable
fruits[1] = 'lime'
# print(fruits) # ['apple', 'lime', 'orange']

# cannot add items this way
# fruits[3] = 'lemon' # IndexError: list assignment index out of range

# --------------------------------------------------------------------------------------------- #

# use list methods to add items to a list
# .append(item) - add the item to the end of the list
fruits.append('lemon')
# print(fruits) # ['apple', 'lime', 'orange', 'lemon']

# .insert(index, item) - add the item at the index
fruits.insert(0, 'kiwi')
# print(fruits) # ['kiwi', 'apple', 'lime', 'orange', 'lemon']

# .extend(sequence) - add the items from the sequence to the end of the list
fruits.extend(['apple', 'guava', 'lychee'])
# print(fruits) # ['kiwi', 'apple', 'lime', 'orange', 'lemon', 'apple', 'guava', 'lychee']

# ----------------------------------------------------------------------------------------- #

# delete items with list methods

# .remove(item) - remove the first occurrence of the item from the list
fruits.remove('apple')
# print(fruits) # ['kiwi', 'lime', 'orange', 'lemon', 'apple', 'guava', 'lychee']

# .pop(index) - remove the item at the index and return it. index is -1 if not provided
# fruit = fruits.pop() # remove the last item in the list
# print(fruit, fruits) # lychee ['kiwi', 'lime', 'orange', 'lemon', 'apple', 'guava']

# fruits.pop(1) # remove the item at index 1
# print(fruits) # ['kiwi', 'orange', 'lemon', 'apple', 'guava']

# -------------------------------------------------------------------------------------- #

# .index(item) - return the index of the first occurrence of the item, if it exists

lemon_index = fruits.index('lemon')
# print(lemon_index, fruits[lemon_index]) # 3 lemon

# value must exist in the list to get its index
# fruits.index('cherry') # ValueError: 'cherry' is not in list

# --------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order in place (returns None)

# fruits.sort()
# print(fruits) # ['apple', 'guava', 'kiwi', 'lemon', 'lime', 'lychee', 'orange']

# use reverse=True to sort in descending order
# fruits.sort(reverse=True)
# print(fruits) # ['orange', 'lychee', 'lime', 'lemon', 'kiwi', 'guava', 'apple']

# ------------------------------------------------------------------------------------ #

# string methods that deal with lists

# convert the string to list
letters = list('ABC')
# print(letters) # ['A', 'B', 'C']

# .split(separator) - split the string into a list at each instance of the separator character
letters = 'A-B-C'.split('-')
# print(letters) # ['A', 'B', 'C']

# print('red, green, blue'.split(', ')) # ['red', 'green', 'blue']

# glue_string.join(list_of_strings) - join all the string in the list into a single string
#                                     by placing the 'glue_string' between each pair

# print(''.join(letters)) # ABC
# print(', '.join(letters)) # A, B, C
# print(' _-^-_ '.join(letters)) # A _-^-_ B _-^-_ C

# ----------------------------------------------------------------------------------------- #

# 'nested' lists

grid = [['O', 'O', 'X'], ['O', 'O', 'O'], ['O', 'O', 'O']]

grid = [
    ['O', 'O', 'X'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

# print(grid[0]) # first row - ['O', 'O', 'X']
# print(grid[0][2]) # 'X'

grid[1][1] = 'X'

# print(grid) # [['O', 'O', 'X'], ['O', 'X', 'O'], ['O', 'O', 'O']]


'''
for row in grid:
    print(row)
['O', 'O', 'X']
['O', 'X', 'O']
['O', 'O', 'O']
'''

# -------------------------------------------------------------------------------------------- #

# for item in sequence - loop through each item in a sequence
'''
for fruit in fruits:
    print(fruit)
'''

# --------------------------------------------------------------------------------------------- #

# print only the fruits that start with the letter 'L'
"""
for fruit in fruits:
    if fruit[0].upper() == 'L':
        print(fruit)
    
    else:
        print('...')
"""
# ----------------------------------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop) - return a range of numbers from 0 to stop-1

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
for x in range(10):
    print(x, '*' * x)
'''

# --------------------------------------------------------------------- #

# range(start, stop)
'''
for x in range(10, 21): # loop 10 - 20
    print(x)
'''

# ----------------------------------------------------------------------- #

# range(start, stop, step)
'''
for x in range(0, 11, 2): # count from 0-10 by 2s
    print(x)
'''

# ---------------------------------------------------------------------- #

# find the length of the list
# print(len(fruits)) # 7

# print(list(range(len(fruits)))) # [0, 1, 2, 3, 4, 5, 6]

# for index in range(len(fruits)):
#     print(index, fruits[index])

# -------------------------------------------------------------------- #