# <a id="top"><a>Unit 03

[Back to Syllabus](../README.md)

## Table of Contents
- [Integers](#integers)
- [Operators](#operators)
- [Math Module](#math)
- [Datatype: boolean](#boolean)
- [Comparison Operators](#comparison)
- [Logical Operators](#logical)
- [Conditionals: if/else](#conditionals)

### <a id="integers"></a>integers

Integers are an integeral part of programming. In fact, the very first computer program (written by Ada Lovelace) was designed to calculate [Bernoulli numbers](https://en.wikipedia.org/wiki/Bernoulli_number)! I don't know about you but I wouldn't want to calculate _the sequence of rational numbers which occur frequently in number theory_. No, thank you. Which brings us back to integers.

An integer (int) can be a whole number. It can positive or negative. Let's use the example below to calculate how old we are this year.

```python
current_year = 2020
year_of_birth = 1988
age = current_year - year_of_birth

print(age)
```

- [integers code demo](https://repl.it/@pdxadmin/integers)
- [Back to top](#top)

### <a id="operators"></a>Operators

The example above snuck in some operators. Did you recognize it? It was addition! Let's do some operations in the example below.

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

-   [Boolean Overview (w3schools)](https://www.w3schools.com/python/python_booleans.asp)

A boolean can represent one of two values: `True` or `False`.

```python
a = True
b = False
```

## <a id="comparison"></a>Comparison Operators

-   [Comparison Operators Overview (w3schools)](https://www.w3schools.com/python/python_operators.asp)
    |Operator|Description|Example|
    |--------|-----------|-------|
    | == | Equal | x==y |
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

-   [Logical Operators Overview (w3schools)](https://www.w3schools.com/python/python_operators.asp)

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

-   [Conditionals: if/else Overview (w3schools)](https://www.w3schools.com/python/python_conditions.asp)

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

### Assignment

-   [Unit 3 Quiz](https://forms.gle/2F7BuDH5vRKUZCUB6)
-   [Lab 04: Grading](/labs/lab04_grading.md)

[Back to top](#top)
