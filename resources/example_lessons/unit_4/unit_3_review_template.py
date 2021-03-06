'''
Programming 101
Unit 3 Review
'''

# datatype: boolean (bool)
# True / False

# booleans are Capitalized in Python

# ---------------------------------------------------------------------------------- #

# all datatypes have typecasting functions
# str(), int(), float()

# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# If an object has value, it will convert to True
# If an object has NO value, it will convert to False


# zero has no value
# 1 (or any number other than zero) has value

# blank string has no value
# string with at least one character has value

# blank list has no value
# list with at least one item has value

# print(bool(x), bool(y))
# -------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean
# all comparisons need two sides

# == equality
# != inequality

# < 'strictly' less than  
# <= less than or equal to  

# > 'strictly' greater than 
# >= greater than or equal to 

# ------------------------------------------------------------------------------------ #

# other datatypes can be compared

# avoid < and > with datatypes other than numbers (at least for now)
# checking for alphabetical order

# ---------------------------------------------------------------------------------- #

# Logical Operators - combine two comparisons and result in a single boolean
# and, or, not

# all logical statements needs two comparisons

# and - True only if BOTH comparisons are True
# or - True if at least ONE comparison is True

# ----------------------------------------------------------------------------------------- #

# not - flip a boolean

# 'not' works in front of any code that produces a boolean
# .isnumeric() - string method which returns a boolean indicating if the string is all numbers or not

# ----------------------------------------------------------------------------------------- #

# 'not' with Truthy/Falsey

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


# ----------------------------------------------------------------------------------- #

# 'nested conditionals' - conditionals within the code block of other conditionals
