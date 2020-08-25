# Unit 4 Practice Solutions

## Exercise 3 - Flip the Numbers

### **3.1**

**Solution**

    import random

    #Use a loop to create a list of 10 random numbers between -100 and 100.

    # create empty list
    numbers = []
    # loop 10 times
    for i in range(10):
        # generate a random number between -100 and 100
        random_number = random.randint(-100,100)
        # add the random number to the list
        numbers.append(random_number)

    #Loop through the list of numbers and switch each number to its opposite sign.

    # create empty list
    flipped = []
    # loop through each number
    for number in numbers:
        # flip the sign of the number
        flipped_number = number * -1
        # add to the new list
        flipped.append(flipped_number)

    # display results
    print(f'numbers: {numbers}')
    print(f'flipped {flipped}')

Keep in mind that is is just one potential solution

## [< Exercise 3](../exercise_3.md)

---

### [<< Back to Unit 4 Practice](/practice/unit_4/)
