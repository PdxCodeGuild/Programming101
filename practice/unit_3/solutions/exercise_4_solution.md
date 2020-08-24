# Unit 3 Practice Solutions

## Exercise 4 - Number Proximity

### **4.1**

**Solution**

    #Assign a number to a variable.
    number = 95

    #Determine whether the number is within 10 of 100.
    if number >= 90 and number <= 110:
        message = f'{number} is within 10 of 100.'
    else:
        message = f'{number} is not within 10 of 100.'

    print(message)

**Output**

    number: 92
    output: 92 is within 10 of 100.

    number: 108
    output: 108 is within 10 of 100.

    number: 51
    output: 51 is not within 10 of 100.

---

### **4.2**

**Solution**

    # Ask the user for two numbers, convert them to integers

    number_1 = input('Enter the first number: ')
    number_1 = int(number_1)

    number_2 = input('Enter the second number: ')
    number_2 = int(number_2)

    # check to see which number is larger,
    # then subtract one from the other. Check if the
    # result is less than or equal to 10
    if number_1 >= number_2:
        if number_1 - number_2 <= 10:
            message = f'{number_1} is within 10 of {number_2}.'
        else:
            message = f'{number_1} is not within 10 of {number_2}'
    elif number_2 >= number_1:
        if number_2 - number_1 <= 10:
            message = f'{number_1} is within 10 of {number_2}.'
        else:
            message = f'{number_1} is not within 10 of {number_2}'


    print(message)

**Output**

    Enter the first number: 4
    Enter the second number: 12

    4 is within 10 of 12.
    ----

    Enter the first number: 66
    Enter the second number: 57

    66 is within 10 of 57.
    ----

    Enter the first number: 36
    Enter the second number: 245

    36 is not within 10 of 245.

---

### **4.3**

This solution uses Python's built-in `abs()` function to find the **absolute value** of the subtraction of `number_2` from `number_1`. The **absolute value** is then used to determine if the numbers are within a certain value of each other.

Alternatively, the solution from **4.2** can be used and 10 can be replaced with the user's value for how far apart the numbers are allowed to be.

**Solution**

    # Ask the user for two numbers, and how far apart they're allowed to be. # convert to integers
    number_1 = input('Enter the first number: ')
    number_1 = int(number_1)

    number_2 = input('Enter the second number: ')
    number_2 = int(number_2)

    threshold = input('Enter how far apart the numbers are allowed to be: ')
    threshold = int(threshold)

    # use abs() to find the absolute value,
    # check if the absolute value is within the threshold
    if abs(number_1 - number_2) <= threshold:
        message = f'{number_1} is within {threshold} of {number_2}.'
    else:
        message = f'{number_1} is not within {threshold} of {number_2}.'

    print(message)

**Output**

    Enter the first number: 235
    Enter the second number: 555
    Enter how far apart the numbers are allowed to be: 1000

    235 is within 1000 of 555.
    ---

    Enter the first number: 66
    Enter the second number: 62
    Enter how far apart the numbers are allowed to be: 5

    66 is within 5 of 62.
    ---

    Enter the first number: 34
    Enter the second number: 101
    Enter how far apart the numbers are allowed to be: 20

    34 is not within 20 of 101.

## [< Exercise 4](../exercise_4.md)

### [<< Back to Unit 3 Practice](/practice/unit_3/)
