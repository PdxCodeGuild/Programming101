import random # for random.choice()

'''
Unit 4

- Datatype - lists
- random module
    - random.choice()
- For loops
    - for item in sequence
    - for x in range()
- loop control
    - continue
    - break
'''

# lists - 'ordered' and 'changeable' sequences of items, separated by commas and 
# surrounded by square brackets []. Since they're 'ordered', items can be referenced
# by their position in the list. An item's position in the list is called its 'index'.


# define a list
blank_list = [] # blank list
# print(type(blank_list)) # <class 'list'>


numbers = [654, 73, 109, -15] # list of integers

# list of strings (items on multiple lines)
colors = [
    'red',
    'green',
    'blue'
]

# list items can be ANY datatype
jumble = ['cat', '3', 6, 3.1415, True, None, [1,2,3]]
# print(jumble) #['cat', '3', 6, 3.1415, True, None, [1,2,3]]

# items can be referenced by their index (position in the list)
# print(colors[0]) # list indices start at 0 - red
# print(colors[1]) # NOT THE FIRST ITEM - green
# print(colors[2]) # last item in the list - blue
# print(colors[3]) # ERROR! Index too far right.

# In Python, NEGATIVE indices can also be used
# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red
# print(colors[-4]) # ERROR! Index too far left.


# change a value at an index
# print(colors) # ['red', 'green', 'blue']
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# add an item by adding a list
# colors += 'orange' # can't just add an item
# print(colors) # ['red', 'yellow', 'blue', 'o', 'r', 'a', 'n', 'g', 'e']

colors += ['orange'] # must add a list to a list
# print(colors) # ['red', 'yellow', 'blue', 'orange']

colors2 = ['purple', 'orange']
colors += colors2
# print(colors)

# list methods
# .append(item) add the item to the end of the list
colors.append('burgundy') # can only add one item at a time
# print(colors)

# .insert(index, item) add the item at the index
colors.insert(2, 'pink')
# print(colors)

# .remove(item) remove the first occurance of the item from the list
# print(colors) # ['red', 'yellow', 'pink', 'blue', 'orange', 'purple', 'orange', 'burgundy']
colors.remove('orange')
# print(colors) # ['red', 'yellow', 'pink', 'blue', 'purple', 'orange', 'burgundy']

# removed_item = colors.remove('blue') # .remove() returns None after removing the item
# print(removed_item, colors) # None ['red', 'yellow', 'pink', 'purple', 'orange', 'burgundy']

# .pop(index) remove the item at the index and return it
removed_item = colors.pop(4)
# print(removed_item, colors) # purple ['red', 'yellow', 'pink', 'blue', 'orange', 'burgundy']

colors.sort() # sorts the list "in place"
# print(colors) # ['blue', 'burgundy', 'orange', 'pink', 'red', 'yellow']

colors.reverse() # same as .sort(reverse=True)
# print(colors) # ['yellow', 'red', 'pink', 'orange', 'burgundy', 'blue']

colors.sort(reverse=True) # sort the list in reverse (same effect as .reverse())
# print(colors) # ['yellow', 'red', 'pink', 'orange', 'burgundy', 'blue']

# --------------------------------------- #

# loops are code blocks that repeat until a certain condition is met

# For loops


# for item in sequence:
for color in colors:
    message = f'current color: {color}'
    # print(message)

# ------------------------------------------------------------ #

# print different things based on the current value of color
for color in colors:
    if color == 'green' or color == 'burgundy':
        message = f'I don\'t like the color {color}'
    else:
        message = f'I like the color {color}'
    # print(message)

# ------------------------------------------------------------ #

# strings are also sequences
word = 'hello'
for letter in word:
    print(letter * 2)

# ------------------------------------------------------------ #

# for x in range() - used to loop a certain number of times:

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    message = f'x: {x}, squared: {x ** 2}'
    # print(message)

# ------------------------------------------------------------ #

squares = [] # empty list to hold squares

# loop 0 - 10
for x in range(11):
    # calculate the square of x
    square = x ** 2
    
    # add the square to the list
    squares.append(square)
# print(squares)

# ------------------------------------------------------------ #​

# loop 5 times

for x in range(5):
    # add one additional ! each loop
    message = "You're doing a great job!" + ('!' * x)
    # print(message)
    
# ------------------------------------------------------------ #

# ask the user how many times they want to loop
loops = input('How many times would you like to loop?')

# convert to integer
loops = int(loops)

# use the user's input as the range limit
for x in range(loops):
    message = f'loop number {x}'
    # print(message)

# ------------------------------------------------------------ #

colors = ['red', 'yellow', 'pink', 'blue', 'orange', 'purple', 'orange', 'burgundy']

number_of_colors = len(colors) # find the number of items in the colors list
# print(number_of_colors) # 6

# use each number in the range (0 - length of colors list) as an index in a list
for index in range(number_of_colors):
    color = colors[index] # get the color at the current index
    message = f'index: {index}, color: {color}'

    # print(message)
