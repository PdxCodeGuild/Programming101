'''
Programming 101
Unit 2
'''

'''
Variables

- named storage spaces
- used to store data that the program will use later
- can store ANY datatype
- BECOME the datatype they store
- can be given new values (be 'redefined')
'''

# = is the assignment operator
# it assigns the value on the right to the variable on the left

# assign the string 'purple' to the variable 'color'

color = 'yellow'
# print(color) # yellow

# ------------------------------------------------------------------------------------ #

# variable 'color' IS a string because it CONTAINS a string
# print(type(color)) # <class 'str'>

# since 'color' contains a string, string operations can be performed using it
# print(color.upper()) #  YELLOW

# redefine the color variable
color = 'green'
# print(color) # green

# redefine the 'color' variable with the return value from .upper()
color = color.upper()
# print(color) # GREEN

# --------------------------------------------------------------------------------------- #

first_name = "Keegan"

# concatenate the values within the variables
output = 'My name is ' + first_name + '! My favorite color is ' + color.lower() + '!'
# print(output) # My name is Keegan! My favorite color is green!

# ---------------------------------------------------------------------------------------- #

'''
Python Variable Names

- must start with a letter or underscore character
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are three different variables)
'''

# user_name = 'Athena' # valid variable name
# u$ern@me = 'Hades' # invalid variable name

# python_variable_and_function_names_use_snake_case
# all lowercase words, separated with underscores

# variable names should aim to describe the data they contain

# phone_number = '7685947362' # describe the phone number inside the variable
# p = '7685947362' # can't tell what this data is right away

# -------------------------------------------------------------------------------- #

city = "Portland"
temp = 1000 # integer (int)

# concatenation only works between strings
# other datatypes will need to be "typecast" as strings using str()
# str(object) - return a string representation of the object

output = "Welcome to " + city + '! The temperature is ' + str(temp) + ' degrees!'
# print(output) # Welcome to Portland! The temperature is 1000 degrees!


# f-string
# 'f' stands for 'formatted'
# f-strings begin with an 'f' before the opening quote
# Python expressions (code) are placed within the string using curly brackets {}

# f-strings don't care about datatype
output = f"Welcome to {city}! The temperature is {temp} degrees!"
# print(output) # Welcome to Portland! The temperature is 1000 degrees!

# ------------------------------------------------------------------------------------ #

# input() - allow the user to interact with the code in the terminal

'''
user_string = input(prompt_message)

Print the 'prompt_message' and wait for the user to hit Enter.
Once the user hits 'Enter', anything they typed in the terminal will be returned.
The returned string can be stored in a variable such as 'user_string' above

color = input("Enter a color: ")
print(f"Favorite color: {color}")
'''

# -------------------------------------------------------------------------------------- #

# input() ALWAYS returns a string

# in order for input() to be used for numbers (or any other datatype)
# the return value will need to be typecast as integer or float

# integer (int) - whole numbers
# float (float) - decimal numbers

# typecasting functions
# str(object) - return a string representation of the object, if possible
# int(object) - return a integer representation of the object, if possible
# float(object) - return a float representation of the object, if possible

"""

number = input("Please enter a number: ")

print(number, type(number)) # 3 <class 'str'>
print(number + number) # '33'

# convert the number from string to float
number = float(number)

print(number, type(number)) # 3.0 <class 'float'>
print(number + number) # 6.0

"""
# ------------------------------------------------------------------------------------- #
'''
# find the area of a rectangle with user-defined sides

# ask the user for the height and width of a rectangle
height = input("Enter the height of the rectangle: ")
width = input("Enter the width of the rectangle: ")

# convert the height and width to numbers
height = float(height)
width = float(width)

# calculate the area of the rectangle
area = height * width # asterisk is multiplication

# display the results
results = f"""
Area of a rectangle
-------------------
height ... {height}
width .... {width}

area ..... {area}
"""

print(results)

'''

# ------------------------------------------------------------------------------------- #

# arithmetic operators

x = 5
y = 3

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication *
# print(x ** y) # exponentiation ** (x^y)

# print(x / y)  # 'regular' division / (results in a float)
# print(x // y) # 'floor' division // (always rounds down to the nearest integer)

# print(x % y)  # modulus % (remainder after division)

# --------------------------------------------------------------------------------------- #

# // and % are compliments
# print(75 / 10) # 7.5
# print(75 // 10) # 7
# print(75 % 10) # 5

# --------------------------------------------------------------------------------------- #

# % 2 can be used to find even vs odd
# print(6 % 2) # 0 - even
# print(7 % 2) # 1 - odd

# ---------------------------------------------------------------------------------------- #