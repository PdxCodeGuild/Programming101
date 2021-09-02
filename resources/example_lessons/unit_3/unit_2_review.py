'''
Programming 101
Unit 2 Review
'''

# variables are named storage spaces

# assign a value to a variable using =

fruit = 'apple' # assign the string 'apple' to the variable 'fruit'
# print(fruit) # apple


# --------------------------------------------------------------------------------- #

# variables become the datatype they store
# type(object) - return the datatype of the object
datatype = type(fruit)
# print(fruit, datatype) # apple <class 'str'>

# ------------------------------------------------------------------------------ #

# change the value within the variable 'fruit'
fruit = 'orange'
# print(fruit) # orange

# --------------------------------------------------------------------------------- #

# call a string method on the fruit variable and redefine the variable with the return value
fruit = fruit.upper()

# concatentate using the string within the variable
message = 'Favorite fruit: ' + fruit.title()
# print(message) # Favorite fruit: Orange

# ---------------------------------------------------------------------------------- #

'''
Python Variable Names
- must start with a letter or underscore character
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are three different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words separated with underscores

# ThisIsTitleOrPascalCase - used in Python for defining classes (custom datatypes)
# ALLCAPS - generally used for constant variables

# ----------------------------------------------------------------------------------- #

# f-string

# begin with an 'f' before the opening quote
# Python expressions can be placed within the string using curly brackets {}

# concatention only works with strings
# other datatypes will need to be typecast as string using str()

number = 99.5

# output = 'The number is ' + str(number) + '!'
# print(output) # The number is 99.5!

# f-strings don't care about datatype
output = f"The number is {number}!"
# print(output) # The number is 99.5!


# ------------------------------------------------------------------------------------- #

# input() - allows the user to interact with the code

'''
user_string = input(prompt_message)

Print the 'prompt_message' and wait for the user to hit Enter.
Once the user hits 'Enter', anything they typed in the terminal will be returned.
The returned string can be stored in a variable such as 'user_string' above

fruit = input('Enter a fruit: ')
print(f"Favorite fruit: {fruit}")
'''


# ---------------------------------------------------------------------------------- #

# input() always returns a string

# in order to user input() for numbers
# the return value will need to be typecast from string to integer/float
# int(object) - return a integer representation of the object, if possible
# float(object) - return a float representation of the object, if possible
'''
number = input('Enter a number: ')

print(number, type(number)) # 3 <class 'str'>
print(number * 10) # '3333333333'

# typecast the string number into a float
number = float(number)

print(number, type(number)) # 3.0 <class 'float'>
print(number * 10) # 30.0
'''
# ------------------------------------------------------------------------------------------- #

# value passed to int() and float() must LOOK like numbers
# int('fish') # ValueError: invalid literal for int() with base 10: 'fish'
# float('fish') # ValueError: could not convert string to float: 'fish'

# ----------------------------------------------------------------------------------------- #

# arithmetic operators

x = 5
y = 3

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication *
# print(x ** y) # exponentiation **

# print(x / y)  # regular division / (results in a float)
# print(x // y) # floor division // (always round down to the nearest integer)

# print(x % y) # modulus % (remainder after division)

# ------------------------------------------------------------------------------------ #

# % 2 to check even/odd

# print(75 % 2) # 1 - odd
# print(88 % 2) # 0 - even

# ------------------------------------------------------------------------------------ #

x = 3

x + 2 # uses x but doesn't change it
# print(x + 2) # 5 - uses x but doesn't change it
# print(x) # 3

# add 2 to 'x' and redefine the 'x' variable with the result
x = x + 2
# print(x) # 5


# ReAssignment Operators - combine the arithmetic and assignment operators

'''
### These don't all need to be shown. 
### Showing a few to establish the pattern is enough
x += 2 # x = x + 2
x -= 10 # x = x - 10
x *= 100 # x = x * 100
x **= 3 # x = x ** 3
x /= 15 # x = x / 15
x //= 5 # x = x // 5
x %= 2 # x = x % 2
'''


# ---------------------------------------------------------------------------------------- #