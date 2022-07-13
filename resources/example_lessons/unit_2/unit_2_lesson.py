'''
Programming 101
Unit 2
'''

# ------------------------------------Variables---------------------------------------- #

# EXPLAIN THATIF WE WANT TO PRINT THE COLOR 5 TIMES, 
# WE NEED TO CREATE 5 INDIVIDUAL STRINGS THE WAY WE'VE SEEN IT SO FAR
print('purple') # purple 
print('purple') # purple
print('purple') # purple
print('purple') # purple
print('purple') # purple

# SHOW THAT IF WE CHANGE ONE, IT DOESN'T CHANGE ALL THE REST
print('green') # green
print('purple') # purple
print('purple') # purple
print('purple') # purple
print('purple') # purple

# THIS IS WHY WE USE VARIABLES
color = 'purple'

# NOW WE CAN PRINT THE color VARIABLE 5 TIMES TO REFER BACK TO THE SAME STRING
print(color) # purple
print(color) # purple
print(color) # purple
print(color) # purple
print(color) # purple

# CHANGE THE VALUE OF color AND SHOW THE OUTPUT AGAIN
# ---------------------------------------------------------------------------- #

'''
Variables

- are used to store data that the program will use later
- can store objects of ANY datatype
- BECOME the datatype of the object they store
- can be given new values (be 'redefined')
'''

# = is the assignment operator
# it assigns the value on the right to the variable on the left

color = 'pink'
# print(color) # pink

# ------------------------------------------------------------------------------------- #

# variable 'color' IS a string because it CONTAINS a string
# print(type(color)) # <class 'str'>

# since 'color' contains a string, it can be used in string operations
# print(color.upper()) # PINK
# print(color) # pink

# redefine the value within 'color'
color = 'purple'
# print(color) # purple

# redefine the 'color' variable using the return value from .upper()
color = color.upper()
# print(color) # PURPLE

# ------------------------------------------------------------------------------------- #

first_name = 'Keegan'

# concatenate the values within the variables
output = 'My name is ' + first_name + ' and my favorite color is ' + color.lower() + '.'
# print(output) # My name is Keegan and my favorite color is purple.

# -------------------------------------------------------------------------------------- #

'''
Python Variable Names

- must start with a letter or underscore
- cannot start with number
- can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# user_name_1 = 'Athena' # valid variable name
# 1u$ern@me = 'Hades' # invalid variable name

# python_variable_and_function_names_use_snake_case
# all lowercase words separated with underscores

# variable names should aim to describe the data they contain
phone_number = '7654352647' # good
p = '8765678765' # bad

# -------------------------------------------------------------------------------------------- #

city = 'Portland'
temp = 70 # integer - int

# concatenation only works between strings
# other datatypes will need to be "typecast" as strings using str()
# str(object) - return a string representation of the object

# message = 'Welcome to ' + city + '! The temp today was ' + str(temp) + ' degrees!'
# print(message) # Welcome to Portland! The temp today was 70 degrees!

'''
f-string

- 'f' stands for 'formatted'
- begin with and 'f' before the opening quote
- Python expressions (code) can be placed within the f-string using curly brackets {}
- don't care about datatype
'''

message = f"Welcome to {city}! The temp today was {temp} degrees!"
# print(message) # Welcome to Portland! The temp today was 70 degrees!

# --------------------------------------------------------------------------------------- #

# input() - allow the user to interact with the code from the terminal

'''
user_string = input('prompt message')

- Print the 'prompt message' and wait for the user to hit Enter
- Once the user hits Enter, anything they typed in the terminal will be returned from input()
- The returned string can be stored in a variable such as 'user_string' above

'''



# color = input('Enter a color: ')
# print(f"Favorite color: {color}")

# ------------------------------------------------------------------------------------------------ #

'''
input() always returns a string

In order to use input() for datatypes other than strings,
the return value will need to be typecast

Integer (int) - whole numbers
Float (float) - decimal numbers

Typecasting functions
str(object) - return a string representation of the object, if possible
int(object) - return a integer representation of the object, if possible
float(object) - return a float representation of the object, if possible
'''

'''
number = input('Please enter a number: ')

print(number, type(number)) # 9 <class 'str'>
print(number + number) # '99'

# redefine the string number as a float
number = float(number)

print(number, type(number)) # 9.0 <class 'float'>
print(number + number) # 18.0
'''

# ---------------------------------------------------------------------------------- #

# Find the area of a rectangle with user-defined sides
"""
# have the user define the height and width of the rectangle
height = input('Enter the height of the rectangle: ')
width = input('Enter the width of the rectangle: ')

# convert the height and width from strings to floats
height = float(height)
width = float(width)

# calculate the area
area = height * width # * is multiplication

# display the result
result = f'''
Area of a Rectangle
-------------------
height ... {height}
width .... {width}

area ..... {area}'''

print(result)

"""

# -------------------------------------------------------------------------------------------- #

# arithmetic operators (math)

x = 5
y = 3

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication *
# print(x ** y) # exponentiation ** (x^y)

# print(x / y)  # 'regular' division / (results in a float)
# print(x // y) # 'floor' division // (always rounds down to the nearest integer)

# print(x % y)  # modulus % (remainder after division)

# ------------------------------------------------------------------------------------------ #

# // and % are compliments
# print(75 / 10) # 7.5
# print(75 // 10) # 7
# print(75 % 10) # 5
