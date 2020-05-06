# <a id="top"><a>Unit 03

[Back to Syllabus](../README.md)

## Table of Contents

-   [Datatype: boolean](#boolean)
-   [Comparison Operators](#comparison)
-   [Logical Operators](#logical)
-   [Conditionals: if/else](#conditionals)

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

-   Complete [Exercise 3](https://learnpythonthehardway.org/python3/ex3.html) of Learn Python the Hard Way

-   [Lab 04: Grading](/labs/lab04_grading.md)

[Back to top](#top)
