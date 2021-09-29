'''
Programming 101
Unit 1 Review
'''

'''
Comments

- organize code
- explain code
- exclude lines of code for testing
'''

# ------------------------------------------------------------------------------------- #

# a function is a named piece of code that performs a specific task

# print(data) - display the data in the terminal

# functions need parentheses after their name to be executed

# hello
# print blank line
# world

# print() can accept multiple, comma-separated items
# they will print with a space between each

# label some data

# -------------------------------------------------------------------------------------------- #

# Datatype: string (str)

# strings are sequences of textual characters surrounded by quotes


# ---------------------------------------------------------------------------------------- #

# type(object) - return the datatype of the object
# everything in Python is an object


# ------------------------------------------------------------------------------------------ #

# print a multi-line string


# ------------------------------------------------------------------------------------------- #

# concatenation - adding strings together to form a single string

# --------------------------------------------------------------------------------------------- #

# a "method" is a function that manipulates only the object to which it belongs
# an object's methods are accessed with a dot . after the object

# .upper() - return an uppercase version of the string

# .replace(old_str, new_str) - replace all occurrences of the old_str with the new_str

### THIS CAN BE SKIPPED, IF NEEDED
# methods can be chained
# each subsequent method will operate on the return value of the previous

# call .upper() on the string returned by .replace()

# -------------------------------------------------------------------------------------------- #

# Escape Characters

# denoted with a backslash \ before the character
# allow characters to be placed within a string that would normally cause errors
# allow formatting of strings
# other uses...

# Python uses quotation marks to begin and end strings
# "Hello "world"" # Error! Double quotes cancel each other

# Solution 1: use mismatched sets
# print("Hello "world"") # Hello "world"

# Solution 2: escape characters
# print("Hello "world"") # Hello "world"

# escape characters can also format strings
# print("ABC") # \n - new line character
# print("ABC") # \t - horizontal tab character