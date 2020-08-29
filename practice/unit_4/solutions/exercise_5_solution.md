# Unit 4 Practice Solutions

## **Exercise 5 - More Number Lists**

Use a loop and `random.randint()` to generate a list of ten `random_numbers` between 1 and 100.

### **5.1**

Count the even numbers

**Solution**

import random

    # generate 10 random numbers between 1 and 100
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1,100))

    # count the even numbers in the list
    # create empty list for evens
    evens = []

    # loop through the numbers
    for number in numbers:
        # check if the number is even
        if number % 2 == 0:
            # add it to the evens list
            evens.append(number)

    # calculate the number of evens
    evens_count = len(evens)

    # display result
    result = f'''Numbers: {numbers}
    There are {evens_count} evens: {evens}'''

    print(result)

**Output**

    Numbers: [64, 3, 55, 94, 40, 56, 40, 69, 54, 3]

    There are 6 evens: [64, 94, 40, 56, 40, 54]

### **5.2**

Reverse the list using a loop and without any methods or built-in functions

**Solution**

    import random

    # generate 10 random numbers between 1 and 100
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1,100))

    # calculate the length of the numbers list
    numbers_length = len(numbers)

    # blank list for reverse
    numbers_reversed = []
    # loop backwards over one less than the length
    for index in range(numbers_length - 1, -1, -1):
        # get the current number
        number = numbers[index]

        # add it to the reversed list
        numbers_reversed.append(number)

    # display result
    result = f'''numbers: {numbers}
    reversed: {numbers_reversed}'''

    print(result)

**Output**

    numbers: [62, 23, 56, 30, 55, 60, 31, 91, 93, 45]
    reversed: [45, 93, 91, 31, 60, 55, 30, 56, 23, 62]

### **5.3**

Sort the list of numbers in ascending order without using methods or built-in functions.

**Solution**

Keep in mind that is is just one potential solution

## [< Exercise 5](../exercise_5.md)

---

### [<< Back to Unit 4 Practice](/practice/unit_4/)
