# Unit 4 Practice Solutions

## Exercise 1 - Number Lists

### **1.1**

```python
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


# display the result
print(f'numbers: {numbers}')
print(f'less than five: {result}')
```

**Output**

    numbers: [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]
    less than five: [3, 3, 4, 2]

### **1.2**

```python
# Create a list of 10 numbers between 1 and 10.
numbers = [4, 9, 3, 9, 5, 7, 2, 5, 1, 7]

# determine how many 5s
fives = numbers.count(5)

# display the result
print(f'numbers: {numbers}')
print(f'The number 5 occurs {numbers.count(5)} times')
```

**Output**

    numbers: [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]
    The number 5 occurs 3 times.

### **1.3**

```python
# numbers list
numbers = [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]

# display numbers before transformation
print(f'numbers: {numbers}')

# get the length of the numbers list
numbers_length = len(numbers)
# loop the length of the list
for i in range(numbers_length):
    # using i as the index for the current number,
    # change the value at i to the itself squared
    numbers[i] = numbers[i] ** 2

# display the result
print(f'squares: {numbers}')
```

**Output**

    numbers: [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]
    squares: [9, 9, 100, 25, 16, 25, 36, 25, 49, 4]

Keep in mind that is is just one potential solution

## [< Exercise 1](../exercise_1.md)
