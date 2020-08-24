# Unit 4 Practice Solutions

## Exercise 1 - Number Lists

### **1.1**

    # Create a list of 10 numbers between 1 and 10.
    numbers = [4, 9, 3, 9, 5, 7, 2, 5, 1, 7]

    #Print all the number in the list that are less than or equal to 5.

    # empty string for result
    result = []

    # loop through the numbers
    for number in numbers:
        # if the current number is less than 5,
        if number <= 5:
            # convert the number to a string
            number = str(number)

            # add it to the list
            result.append(number)

    # create a string from the list,
    # separating each element with a comma and space
    result = ', '.join(result)

    # display the result
    print(f'less than five: {result}')

## [< Exercise 1](../exercise_1.md)
