'''
Programming 101
Unit 5
'''

# string module
import string
import random

letters = string.ascii_letters
# print(letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

digits = string.digits
# print(digits) # '0123456789'

punctuation = string.punctuation
# print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

all_characters = letters + digits + punctuation
# print(all_characters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ------------------------------------------------------------------------------------------ #

# while loop

'''
while some_condition == True:
    # loop this code block
    # until 'some_condition' becomes False
'''

# ----------------------------------------------------------------------------------- #

# for x in range(10) - with a while loop

x = 0
while x < 10: # False when x == 10
    # print(x)

    # change x to eventually make the loop's condition False
    x += 1

# --------------------------------------------------------------------------------- #

# generate a list of 10 random numbers between 1 and 100
numbers = []

while len(numbers) < 10:
    # add a random integer to the list
    numbers.append(random.randint(1, 100))

    # print(numbers)

# print(numbers)

# ------------------------------------------------------------------------------ # 

# string pattern builder - run a loop to create an alternating pattern of string characters

# blank string to hold the pattern
pattern = ''

while len(pattern) <= 10:
    # if the pattern's length is even
    if len(pattern) % 2 == 0:
        pattern += '*'

    # if the pattern's length is odd
    elif len(pattern) % 2 == 1:
        pattern += '-'

# print(pattern) # *-*-*-*-*-*

# ----------------------------------------------------------------------------------------- #

# remove on number at a time from the list until the list is empty

print(numbers) # from the loop on line 48

# remove on number at a time from the list until the list is empty

while numbers != []:
    # remove on item from the end of the list
    number = numbers.pop()

    # print(number, numbers)

# -------------------------------------------------------------------------------------- #

# loop controls
# else, continue, break

for x in range(10):

    # if x == 1 or x == 3 or x == 5 or x == 7:
    if x in [1, 3, 5, 7]:
        print('.' * x)
        continue # skip the rest of this iteration and begin the next

    if x == 8:
        print("Goodbye!")
        break # end the loop immediately

    print(x)

else:
    # if the loop's condition becomes False
    # else will be triggered
    print("The loop made it all the way through!")