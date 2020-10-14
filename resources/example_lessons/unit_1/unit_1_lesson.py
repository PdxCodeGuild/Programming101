# Programming 101 - Unit 1

'''
Comments

- explain code
- organize code
- exclude code for testing
'''

# single-line comments start with a pound sign '#'

# multiple
# single line
# comments

'''
Multi-line
comment
with single quotes
'''

"""
Multi-line
comment with
double quotes
"""

# A function is a named section of code that performs a specific task. Python comes with many built in functions.

# print(content) will display the content (within the parentheses) to the terminal

# print('hello world!') # hello world!
# print("I don't like spam!") # I don't like spam!

# Datatype: strings

# Strings are textual data. Strings are sequences of 
# characters surrounded by quotes

# strings:
'cat'
"dog"
'123456789'
"3.141592654"
"" # 'blank' string
'' # 'blank' string
"593jhAHAHAH01-10293894$%#$%#$&jekj" # big ol' string

# print("593jhAHAHAH01-10293894$%#$%#$&jekj") # 593jhAHAHAH01-10293894$%#$%#$&jekj

# multiline comments are also multi-line strings
"""
print('''This
is a
multi-line
string
''')
"""

# --------------------- #

# Concatenation - adding strings together
# print('Hello' + 'world') # Helloworld
# print('hello ' + 'world') # hello world
# print('hello' + ' world') # hello world

# print('hello' + ' ' + 'world') # keeping the space in its own string

# print('Welcome,' + ' ' + 'to' + ' ' + 'PDX' + ' ' + 'Code' + ' ' + 'Guild' + '!') # Welcome to PDX Code Guild

# ----------------------- #

# Datatype Methods
# A method is a function (needs parentheses after) that 
# manipulates the piece of data to which it is attached with a dot .

# print('giraffe'.upper()) # GIRAFFE
# print('abcdefg'.upper()) # ABCDEFG

# print('HIJKLMN'.lower()) # hijklmn

# print('pDx CoDe GuIlD'.title()) #  - Pdx Code Guild - capitalize the first letter of each word

#print('pDx'.upper() + ' cOdE gUiLd'.title()) # - PDX Code Guild

# OOPS! Forgot parentheses after the method name! 
# print('giraffe'.upper) # <built-in method upper of str object at 0x00000200CDB73C30>

# ----------------------------- #

# Escape characters
# Allow us to use special in strings which would normally be illegal. 
# Also allow us to format strings for output


# Printing quotes within quotes:
# print("Hello "World"") # ERROR! double quotes within double quotes cancel each other
# print('Hello 'World'') # ERROR! single quotes within single quotes cancel each other

# print('Hello "world"') # Hello "world" - double quotes are allowed within single quotes
# print("Hello 'world'") # Hello 'world' - single quotes are allowed within double quotes

# print("I don't like spam!") # printing single quotes within double
# print('I don\'t like spam!') # printing single quotes within single with an escape character

# print("hello \"world\"") # hello "world" \" to print double quote within double quotes

# print('Hello\nworld') # \n is a 'new line' character

# print('hello\tworld') # \t is a 'horizontal tab'

# print("\\") # print a backslash with \\
# print("/\/\/\\") # /\/\/\
