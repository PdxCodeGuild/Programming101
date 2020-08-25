# Unit 4 Practice Solutions

## Exercise 2 - Sum, Mean, Mode

### **2.1**

Find the sum of the list of numbers

**Solution**

    import random

    # Use a loop to create a list of 10 random numbers between 1 and 10.

    # create empty list
    numbers = []
    # loop ten times
    for i in range(10):
        # generate random number between 1 and 10
        random_number = random.randint(1, 10)
        # add the number to the list
        numbers.append(random_number)

    # Loop through the list of numbers and calculate the sum
    # set the total to zero
    total = 0
    # loop through the numbers
    for number in numbers:
        # add the number to the total
        total += number

    # display the result
    print(f'numbers: {numbers}')
    print(f'sum: {total}')

**Output**

    numbers: [1, 4, 6, 4, 6, 4, 5, 9]
    sum: 39

### **2.2**

Find the mean (average) of the list of numbers

**Solution**

    import random

    # Use a loop to create a list of 10 random numbers between 1 and 10.

    # create empty list
    numbers = []
    # loop ten times
    for i in range(10):
    # generate random number between 1 and 10
    random_number = random.randint(1, 10)
    # add the number to the list
    numbers.append(random_number)

    # Loop through the list of numbers and calculate the sum
    # set the total to zero
    total = 0
    # loop through the numbers
    for number in numbers:
        # add the number to the total
        total += number

    # calculate the average
    average = total / len(numbers)

    # display the result
    print(f'numbers: {numbers}')
    print(f'average: {average}')

**Output**

    numbers: [1, 4, 6, 4, 6, 4, 5, 9]
    average: 4.875

### **2.3**

Find the mode

**Solution**

    import random

    # Use a loop to create a list of 20 random numbers between 1 and 10.

    # create empty list
    numbers = []
    # loop twenty times
    for i in range(20):
        # generate random number between 1 and 10
        random_number = random.randint(1, 10)
        # add the number to the list
        numbers.append(random_number)

    # Loop through the list of numbers and calculate the mode

    # set the first element as the default mode
    mode = numbers[0]
    # number of occurances of the mode
    mode_count = numbers.count(mode)

    # loop through the list of numbers
    for number in numbers:
        # calculate the number of times the old mode appears
        old_count = numbers.count(mode)

        # calculate the number of times the current number appears
        new_count = numbers.count(number)

        # if the current number occurs more times than the previous mode
        if new_count > old_count:
            # set the mode to the current number
            mode = number
            # count the occurances of the new mode
            mode_count = new_count

    # display the result
    result = f'''
    numbers: {numbers}
    mode: {mode}
    The number {mode} appears {mode_count} times.
    '''

    print(result)

Keep in mind that is is just one potential solution

## [< Exercise 2](../exercise_2.md)
