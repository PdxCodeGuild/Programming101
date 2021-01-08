'''
Unit 5

- string module
- while loops
- using 'else' with loops
- continue
- break
'''
import string

lowercase = string.ascii_lowercase
# print(lowercase) # abcdefghijklmnopqrstuvwxyz

uppercase = string.ascii_uppercase
# print(uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ

all_letters = string.ascii_letters
# print(all_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

digits = string.digits
# print(digits) # '0123456789'

punctuation = string.punctuation
# print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ---------------------- #

# while loops

'''
while some_condition == True:
    # loop this code block
'''

counter = 0
while counter < 10:
    # print(counter)

    # count up until counter == 10
    counter += 1



'''
pattern = ''

count = 0
while count < 20:
  if count % 2 == 0:
    pattern += '*'
  
  else:
    pattern += '-'

  count += 1

print(pattern)
'''

'''
fruits = []

# ask the user to enter a fruit 5 times, then print the list
while len(fruits) < 5:
    fruit = input('Enter a fruit: ')

    # add the fruit to the list
    fruits.append(fruit)

    print(fruits)

print(fruits)
'''
# --------------------------- #
"""
counter = 0
while counter < 6:

    if counter % 2 == 0:
        print('skipping even')
        counter += 1 # increment to avoid infinite loop
        continue

    # if counter == 5:
    #     print('this loop was broken')
    #     break

    print(counter)
    counter += 1

else:
    # this block will only be executed if the loop ends NATURALLY
    # a loop ends "naturally" when its condition becomes False
    print("This loop ended NATURALLY")
"""

# else works with for loops too

'''
for letter in lowercase:
    print(letter)

    # if letter == 'q':
    #     break
else:
    print('end of alphabet')
'''

'''
pattern = ''

i = 0
while i < 20:
  if i % 2 == 0:
    pattern += '*'
  
  else:
    pattern += '-'

  i += 1

print(pattern)
'''