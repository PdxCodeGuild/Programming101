# <a id="top"><a>Unit 03

[Back to Syllabus](../README.md)

## Table of Contents

- [<a id="top"><a>Unit 03](#a-idtopaunit-03)
  - [Table of Contents](#table-of-contents)
  - [<a id="operators"></a>Operators](#operators)
    - [Arithmetic Operators](#arithmetic-operators)
    - [Arithmetic Example](#arithmetic-example)
  - [<a id="math"> Math Module</a>](#-math-module)
  - [<a id="boolean"></a>Dataype: Boolean](#dataype-boolean)
  - [<a id="comparison"></a>Comparison Operators](#comparison-operators)
  - [<a id="logical"></a>Logical Operators](#logical-operators)
  - [<a id="conditionals"></a>Conditionals: if/else](#conditionals-ifelse)
    - [<a id="random"></a>Random Module](#random-module)
    - [Assignment](#assignment)

## <a id="operators"></a>Operators

### Arithmetic Operators

| Operator | Name           | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | x + y    |
| -        | Subtraction    | x - y    |
| \*       | Multiplication | x \* y   |
| /        | Division       | x / y    |
| //       | Floor Division | x // y   |
| \*\*     | Exponentiation | x \*\* y |
| %        | Modulus        | x % y    |

### Arithmetic Example

The adventure club you're in has decided to check out [Powell Butte Nature Park](https://www.portlandoregon.gov/parks/finder/index.cfm?action=ViewPark&PropertyID=528). When the idea comes up, 20 people are interested in going. On the day before the hike, 6 people drop out. Let's update the headcount.

```python
num_of_interested = 20
drop_outs = 6
num_of_attendees = num_of_interested - drop_outs

print(f"There were {num_of_interested} people who were interested in going hiking but {drop_outs} have changed their mind. The total number of people going is now {num_of_attendees}.")
```

- [operators code demo](https://repl.it/@pdxadmin/operators)

Great! Now let's figure out carpool. With 14 people, how many cars do we need? Let's do 4 people to 1 car. That way everyone can sit comfortably.

```python
num_of_interested = 20
drop_outs = 6
num_of_attendees = num_of_interested - drop_outs

print(f"There were {num_of_interested} people who were interested in going hiking but {drop_outs} have changed their mind. The total number of people going is now {num_of_attendees}.")

car_max = 4
num_of_cars = num_of_attendees / car_max
print(f"With {num_of_attendees} people, we will need {num_of_cars} cars.")
```

- [carpool code demo](https://repl.it/@pdxadmin/operators2)

## <a id="math"> Math Module</a>

Great! We figured out that we need 3.5 cars. But wait, 3.5 doesn't make sense! In real life, we would round up the number of cars. So let's do that.

Introducing the [Math module](https://docs.python.org/3/library/math.html)! Let's look at the ceiling function in the Math module.

```python
# import the math module
import math

# number of cars from last example
num_of_cars = 3.5

# use math.ceil() to round up
num_of_cars = math.ceil(num_of_cars)

print(num_of_cars) # outcome: 4
```

## <a id="boolean"></a>Dataype: Boolean

- [Boolean Overview (w3schools)](https://www.w3schools.com/python/python_booleans.asp)

A boolean can represent one of two values: `True` or `False`.

```python
a = True
b = False
```

## <a id="comparison"></a>Comparison Operators

- [Comparison Operators Overview (w3schools)](https://www.w3schools.com/python/python_operators.asp)
  |Operator|Description|Example|
  |--------|-----------|-------|
  | == | Equal | x == y |
  | != | Not Equal | x != y |
  | > | Greater than | x > y |
  | < | Less than | x < y |
  | >= | Greater than or equal to | x >= y |
  | <= | Less than or equal to | x <= y |

```python
x = 3
y = 4

x == 3 # True
x == y # False

x > y # False
x < y # True

x != y # True

x > 3 # False
x >= 3 # True

```

## <a id="logical"></a>Logical Operators

- [Logical Operators Overview (w3schools)](https://www.w3schools.com/python/python_operators.asp)

| Operator | Description                              | Example          |
| -------- | ---------------------------------------- | ---------------- |
| and      | Returns True if both statements are True | x < 5 and x < 10 |
| or       | Return True if one statement is True     | x < 4 or x > 6   |
| not      | Reverse the result, returns fals if True | not(x < 5)       |

---

| and   | True  | False |
| ----- | ----- | ----- |
| True  | True  | False |
| False | False | False |

---

| or    | True | False |
| ----- | ---- | ----- |
| True  | True | True  |
| False | True | False |

## <a id="conditionals"></a>Conditionals: if/else

- [Conditionals: if/else Overview (w3schools)](https://www.w3schools.com/python/python_conditions.asp)

We can use condtional statements to run code using our comparison operators

This can be achieved by using the `if` keyword

```python
x = 4
y = 10
if x < y:
    print("x is less than y")
```

Notice how the `print` statement is indented? Python relies on indentation to define blocks of code. Other languages my use { } to accomplish the same task.

We also have access to the keyword `elif`. This is pythons way of saying "if the previous condition was not True, then try this one"

```python
x = 4
y = 10

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

```

Lastly we have `else`. This will catch any case that was not caught by the preceding conditions

```python
x = 4
y = 10

if x > y:
    print("x is greater than y")
elif x == y :
    print("x is equal to y")
else:
    print("x is less than y")
```

Notice there is no conditional statement on `else`.

### <a id="random"></a>Random Module

Modules are a Python object that are sources of related code; think of if as a library of information. A code library, if you will! It is a file containing a set of functions you want to include in your application. ([For a list of all modules, you can check out the offical Python docs](https://docs.python.org/3/py-modindex.html)).

For this lesson, we will be looking at the [random module](https://pynative.com/python-random-module/). And specifically, we will be looking at the `randint()` function of the random module: [random.randint()](https://www.w3schools.com/python/ref_random_randint.asp). Please see the example below:

```python
# include the random module in our file
import random

# randint(bottom, top)
# generate a random integer between
# the bottom number and the top number
random_number = random.randint(1, 100)

print(f'Random number: {random_number}')

```

**Output**

    Random number: 56

    Random number: 13

    Random number: 98

- [random module code demo](https://repl.it/@pdxadmin/random)

### Assignment

- [Unit 3 Quiz](https://forms.gle/2F7BuDH5vRKUZCUB6)
- [Lab 04: Grading](/labs/grading.md)

[Back to top](#top)
