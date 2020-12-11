'''
Unit 4 Review
'''
import random

'''
Lists

ordered and changeable sequences of items
items are separated by commas and surrounded by square brackets
'''

colors = ['green', 'red', 'blue']

# organize list items vertically
colors = [
    'green',
    'red',
    'blue'
]

# list items can be ANY datatype, including other lists
jumble = [10, 3.14, True, [11, 22, 33]]

# reference an item at its index
# print(colors[0]) # green
# print(colors[1]) # red
# print(colors[2]) # blue
# print(colors[3]) # ERROR! Index doesn't exist. IndexError: list index out of range

# In Python, negative indices can be used as well
# print(colors[-1]) # blue - last item in the list
# print(colors[-2]) # red
# print(colors[-3]) # green
# print(colors[-4]) # ERROR! Index doesn't exist. IndexError: list index out of range

# adding items:

# .append(item) add the item to the END of the list
colors.append('teal')
# print(colors)

# .insert(index, item) add the item at the given index
colors.insert(0, 'mauve')
# print(colors)

# .extend(list) add the list to the original
colors.extend(['yellow', 'red'])
# print(colors)

# deleting items from a list

# keyword: del
del colors[0] # delete item at index 0
# print(colors)

# .remove(item) delete the first occurance of the item
removed_color = colors.remove('red')
# print(colors)
# print(removed_color) # None - remove() doesn't return the removed value

# .pop(index) remove the item at the index AND return it to you
removed_color = colors.pop(0)
# print(removed_color, colors) # green ['blue', 'purple', 'teal', 'yellow', 'red']

colors.reverse()
# print(colors) ['red', 'yellow', 'teal', 'purple', 'blue']

random.shuffle(colors) # randomize a list
# print(colors) # ['teal', 'blue', 'yellow', 'purple', 'red']

# .count(item) count the number of times the item occurs 
# colors.append('blue')
# print(colors.count('blue')) # 2
# print(colors.count('brown')) # 0

# -------------------------------------------------------------------------- #

# .index(item) find the index of the first occurance of an item if it exists
# print(colors)
# print(colors.index('yellow'))
# print(colors.index('brown')) # ValueError: 'brown' is not in list

# check an index for an item without breaking the code with .index()
desired_color = 'red'

if desired_color in colors:
    index = colors.index(desired_color)
else:
    index = f'{desired_color} is not in the list'

print(index)

# -------------------------------------------------------------------------- #

# sort a list
colors.sort()
# print(colors) # ['blue', 'purple', 'red', 'teal', 'yellow']

colors.sort(reverse=True) # sort in descending order - 
# print(colors) # ['yellow', 'teal', 'red', 'purple', 'blue']

# ------------------------------------------------------------ #


# working with 'nested' lists
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# laid out like a grid
grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

grid[1][1] = 'X'

print(grid) # [[0, 0, 0], [0, 'X', 0], [0, 0, 0]]

for row in grid:
    print(row)

# -------------------------------------------------------------------------- #

# for loops

# for item in sequence
for color in colors:
    output = f'color: {color}'
    # print(output)

# -------------------------------------------------------------------------- #

for color in colors:
    # change output based on color value
    # if color == 'yellow' or color == 'red': # check for 'yellow' or 'red'
    if color in ['yellow', 'red', 'purple']: # check if the color is in a list
        output = f'I like {color}!'

    else:
        output = f'I don\'t like {color}'

    # print(output)

# -------------------------------------------------------------------------- #

# nested loops
# loop through all the colors
for color in colors:
    print(color)
    # loop through the color string
    for letter in color:
        # print each letter with a tab
        print(letter)

# -------------------------------------------------------------------------- #

# for x in range() - used to loop a certain number of times
# list() - typecasting function for lists. Convert to list
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(stop) - start default to 0, stop is omitted
for x in range(10):
    output = f'x: {x}'
    # print(output)

# len(sequence) return the length of the sequence
number_of_colors = len(colors)
# loop over the indices of the list
for index in range(number_of_colors):
    color = colors[index] # use the index variable to get the current color

    output = f'{index}: {color}'
    # print(output)

# range(start, stop)
for x in range(10, 21): # loop from 10 to 20, because 21 is omitted
    output = f'x: {x}'
    # print(output)

# range(start, stop, step)
for x in range(0, 11, 2): # count 0 - 10 by 2s
    output = f'x: {x}'
    # print(output)

# range(start, stop, step)
for x in range(10, -1, -1): # count down from 10 to 0 by 1
    output = f'x: {x}'
    # print(output)

