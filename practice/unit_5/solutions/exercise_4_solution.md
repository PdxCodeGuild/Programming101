# Unit 5 Practice Solutions

## Exercise 4 - Fibonacci / Tribonacci

### **1.1**

**Solution**

```python
# starting values
fibonacci = [0,1]

i = 0 # index counter

# while fibonacci list has less than ten elements
while len(fibonacci) < 10:

    # get the two previous numbers
    prev_1 = fibonacci[i]
    prev_2 = fibonacci[i+1]

    # sum of the two previous numbers
    n = prev_1 + prev_2

    # add n to the list
    fibonacci.append(n)

    # increase i
    i += 1

# display the result
output = f'First ten Fibonacci numbers:\n{fibonacci}'
print(output)
```

**Output**

    First ten Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

### **1.2**

**Solution**

```python
# starting values
tribonacci = [0,1,1]

i = 0 # index counter

# while fibonacci has less than ten elements
while len(tribonacci) < 10:

    # get the three previous numbers
    prev_1 = tribonacci[i]
    prev_2 = tribonacci[i+1]
    prev_3 = tribonacci[i+2]

    # sum of the three previous numbers
    n = prev_1 + prev_2 + prev_3

    # add n to the list
    tribonacci.append(n)

    # increase i
    i += 1

# display the result
output = f'First ten Tribonacci numbers:\n{tribonacci}'
print(output)
```

**Output**

    First ten Tribonacci numbers:
    [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]

### **1.3**

**Solution - Fibonacci**

```python
# no starting values
fibonacci = []

i = 0 # index counter

# while fibonacci has less than ten elements
while len(fibonacci) < 10:

  # get the first two elements
  if len(fibonacci) < 2:

    # len(fibonacci) with be either 0 or 1,
    # so the first two elements become [0,1]
    n = len(fibonacci)

  # calculate all other elements
  else:
    # get the twp previous numbers
    prev_1 = fibonacci[i]
    prev_2 = fibonacci[i+1]

    # add the sum of the three previous numbers to the list
    n = prev_1 + prev_2

    # increase i
    i += 1

  # add n to the list
  fibonacci.append(n)

# display the result
output = f'First ten Fibonacci numbers:\n{fibonacci}'
print(output)
```

**Solution - Tribonacci**

```python
# no starting values
tribonacci = []

i = 0 # index counter

# while tribonacci has less than ten elements
while len(tribonacci) < 10:
  # get the first two elements
  if len(tribonacci) < 2:
    # the first two elements become [0,1]
    # because the length is less than 2 (0 or 1)
    n = len(tribonacci)

  # get the third element
  elif len(tribonacci) == 2:
    n=1

  # calculate all other elements
  else:
    # get the three previous numbers
    prev_1 = tribonacci[i]
    prev_2 = tribonacci[i+1]
    prev_3 = tribonacci[i+2]

    # sum of the three previous numbers
    n = prev_1 + prev_2 + prev_3

    # increase i
    i += 1

  # add n to the list
  tribonacci.append(n)

# display the result
output = f'First ten Tribonacci numbers:\n{tribonacci}'
print(output)
```

### **1.4**

```python
# ask the user for the number of elements
limit = input("Enter the number of Fibonacci numbers you'd like to generate")

# convert the input to an integer
limit = int(limit)

# use the input value to set the loop
while len(fibonacci) < limit:
    # calculate Fibonacci numbers as above
    # ...
    # ...
```

## [< Exercise 4](../exercise_4.md) | [Exercise 5 >](../exercise_5.md)

### [<< Back to Unit 5 Practice](/practice/unit_5/)
