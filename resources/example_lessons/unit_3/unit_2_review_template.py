'''
Programming 101
Unit 2 Review
'''

# variables are named storage spaces

# assign a value to a variable using =

# --------------------------------------------------------------------------------- #

# variables become the datatype they store
# type(object) - return the datatype of the object

# ------------------------------------------------------------------------------ #

# change the value within the variable 'fruit'

# --------------------------------------------------------------------------------- #

# call a string method on the fruit variable and redefine the variable with the return value

# concatentate using the string within the variable

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

# f-strings don't care about datatype

# ------------------------------------------------------------------------------------- #

# input() - allows the user to interact with the code

'''
user_string = input(prompt_message)

Print the 'prompt_message' and wait for the user to hit Enter.
Once the user hits 'Enter', anything they typed in the terminal will be returned.
The returned string can be stored in a variable such as 'user_string' above
'''


# ---------------------------------------------------------------------------------- #

# input() always returns a string

# in order to user input() for numbers
# the return value will need to be typecast from string to integer/float
# int(object) - return a integer representation of the object, if possible
# float(object) - return a float representation of the object, if possible

# ------------------------------------------------------------------------------------------- #

# value passed to int() and float() must LOOK like numbers

### USE PREVIOUS EXAMPLE'S input() TO PRODUCE ERROR ###

# ----------------------------------------------------------------------------------------- #

# arithmetic operators

# addition +
# subtraction -

# multiplication *
# exponentiation **

# regular division / (results in a float)
# floor division // (always round down to the nearest integer)

# modulus % (remainder after division)

# ------------------------------------------------------------------------------------ #

# % 2 to check even/odd

# ------------------------------------------------------------------------------------ #

# ReAssignment Operators - combine the arithmetic and assignment operators

# x = 4

### SHOW HOW x + 2 DOESN'T CHANGE x
### SHOW HOW WE NEED TO DO x + 2 AND THEN USE THE RESULT TO REDEFINE x

# ---------------------------------------------------------------------------------------- #