'''
Unit 2

- variables
- f-strings
- input() function
- Integers (whole numbers)/ Floats (decimal numbers)
'''

'''
Variables

- Used to store data that the program will use later
- Store ANY datatype
- BECOME the datatype they store
- Data within a variable can change
'''

# store the value on the right in the variable on the left
color = 'blue' # store the string 'blue' in the variable 'color'

# color = 1 # now the color variable is an integer, 1

# since color contains a string, string methods can be used on it
# print(color.upper()) # BLUE

color = 'green'
# concatenate the value inside the color variable into a string
# print('My favorite color is ' + color)

first_name = 'Keegan'
# print('My name is ' + first_name + ' and my favorite color is ' + color + '!')

'''
Python variable names:

- must start with a letter or underscore character
- cannot start with a number
- can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _)
- are case sensitive (age, Age, AGE are THREE separate variables)
'''

# Python uses 'snake_case'

# snake_case_separates_lower_case_words_with_underscores # python best practice!
# camelCaseStartsWithALowerCaseLetterAndAllOtherAreCapitalized
# TitleCaseIsTheSameAsCamelButWithNoLowercaseBeginning

# Valid variable names
username = 'Athena' # ideal variable name format (all lowercase)
user_name = 'Dionysus' # also ideal format (underscore separated lowercase words)
_user_name = 'Aphrodite'
userName = 'Poseidon'
USERNAME = 'Hera'
username2 = 'Artemis'

# variable names should attempt to describe the data they represent

# INVALID variable names
# 2username = 'Nyx' # cannot start with a number
# user-name = 'Hades' # no hyphens
# u$ern@me = 'Cerberus' # no special characters other than underscores
# user name = 'Persephone' # no spaces

first_name = 'Keegan'
city = 'Portland'
weather = 'rainy'

# concatenate 3 strings into a larger output
message = 'Hello ' + first_name + '! Today in ' + city + ' it is ' + weather + '!'

# using concatenation is a bit cumbersome. We can use f-strings instead!
# f-string - 'f' stands for 'formatted'

# f-strings begin with an 'f' before the opening quote
# Expressions (Python code) are placed within the string using curly brackets {}

# same as line 70, except with f-string
message = f'Hello {first_name}! Today in {city} it is {weather}!'
# print(message)

name = 'keegan'
birth_year = 1988
current_year = 2020

# because birth_year is an integer, it cannot be concatenated
# into a string without being CAST as a string

# Typecasting is converting one type of data to another: int -> str, str -> int
# birth_year = str(birth_year) # str(data) will convert the data to a string representation of itself


# message = name + ' - born: ' + birth_year # birth_year must be a string to be printed
message = f'{name} - born: {birth_year}' # f-strings don't care about datatype for printing

# calculate the age
age = current_year - birth_year

message = f'{name.capitalize()} - born: {birth_year}. Age: {age}'
# print(message)


# ------------------------------------ #

# input(prompt_message) # display the prompt_message and WAIT for the use to hit ENTER

'''
# catch the return value (user's input) in a variable called first_name
first_name = input('Enter your name: ')

favorite_color = input(f'Hello, {first_name}! Enter your favorite color: ')

print(f'{first_name}\'s favorite color is {favorite_color}')
'''

'''
# REMEMBER!!! input() function ALWAYS ALWAYS returns a STRING
number = input('Enter a number: ')

print(type(number)) # <class 'str'>
print(number + number) # '23' + '23' -> '2323'
# print(number + 2) # ERROR cannot concatenate string to integer

# in order to use the result of an input()
# as a NUMBER, it must be typecast as a number
# number = int(number) # convert string to integer
# or
number = float(number) # convert string to a decimal

print(type(number)) # <class 'float'>
print(number + number) # add rather than concatenate
print(number + 2) # now it will add the numbers, rather than concatenate

'''
# if a string cannot be convert to the desired type, the code will break
# int('3.14') # cannot covert the string '3.14' to an INTEGER, must use FLOAT

# -------------------------- #

print('Band practice!')

player_1 = input('Enter the name of player 1: ')
instrument_1 = input(f'Enter {player_1}\'s instrument: ')

player_2 = input('Enter the name of player_2: ')
instrument_2 = input(f'Enter {player_2}\'s instrument: ')

# this can be cleaned up with a multi-line f-string
# print('Today\'s lineup:')
# print(f'{player_1} - {instrument_1}')
# print(f'{player_2} - {instrument_2}')

# multi-line f-string directly in the print()
'''
print(f"""
Today\'s lineup:
  {player_1} - {instrument_1}
  {player_2} - {instrument_2}
""")
'''

# store the multi-line f-string in a variable, then print the variable
output = f"""
Today\'s lineup:
  {player_1} - {instrument_1}
  {player_2} - {instrument_2}
"""

# print(output)

# ---------------------------- #


x = 17 # assignment operator
y = 6

# Arithmetic operators
# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # 'regular' division - returns a float
# print(x // y) # 'floor' division - always rounds down (cuts off the decimal)
# print(x ** y) # exponentiation - x^y
# print(x % y) # remainder after division

# modulus is good for finding even/odd
# print(562934937 % 2) # 1 - odd
# print(598394834 % 2) # 0 - even



num_of_interested = 20
drop_outs = 6
total_attendees = num_of_interested - drop_outs

attendance_rate = (total_attendees / num_of_interested) * 100

# print(f'''
# There were {num_of_interested} people interested in going hiking
# but {drop_outs} dropped out. Now there will be {total_attendees} people going hiking!
# That's an attendance rate of {attendance_rate}%.
# ''')

# ---------------------- #

x = 5
x + 3

# print(x + 3) # 8 - uses the value of x, but doesn't change it
# print(x) # 5 - x is still 5

x = x + 3 # overwrite the value of x with its previous value (5) + 3
# print(x) # 8

# re-assignment operators
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3
x %= 3 # x = x % 3

# ------------------------- #


x = 17 # assignment operator
y = 6

# Arithmetic operators
# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # 'regular' division - returns a float
# print(x // y) # 'floor' division - always rounds down (cuts off the decimal)
# print(x ** y) # exponentiation - x^y
# print(x % y) # remainder after division

# modulus is good for finding even/odd
# print(562934937 % 2) # 1 - odd
# print(598394834 % 2) # 0 - even



num_of_interested = 20
drop_outs = 6
total_attendees = num_of_interested - drop_outs

attendance_rate = (total_attendees / num_of_interested) * 100

# print(f'''
# There were {num_of_interested} people interested in going hiking
# but {drop_outs} dropped out. Now there will be {total_attendees} people going hiking!
# That's an attendance rate of {attendance_rate}%.
# ''')

# ---------------------- #

x = 5
x + 3

# print(x + 3) # 8 - uses the value of x, but doesn't change it
# print(x) # 5 - x is still 5

x = x + 3 # overwrite the value of x with its previous value (5) + 3
# print(x) # 8

# re-assignment operators
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3
x %= 3 # x = x % 3

# ------------------------- #