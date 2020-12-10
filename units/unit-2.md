# <a id="top"></a>Unit 02

[Back to Syllabus](../README.md)

## Table of Contents

- [variables](#variables)
- [f-strings](#fstring)
- [input()](#input)
- [Integers / Floats](#numbers)
- [Arithmetic Operators](#math-operators)

### <a id="variables"></a>Variables

Variables are used to store data that the program will use later.

```python
# a string, "Jim", is assigned to a variable called name
name = "Jim"
# we later use that variable in a print statement
print("Hello " + name + "!") # Hello Jim!
```

A variable's value can be changed after assignment.

```python
# a string, "Jim", is assigned to a variable called name
name = "Jim"

# a string, "Pam", is assigned to a variable called name which OVERWRITES the previous data
name = "Pam"

# the string, "Jim", no longer exists!
print("Hello " + name + "!") # Hello Pam!
```

### Variable names:

- must start with a letter or the underscore character
- cannot start with a number
- can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- are case-sensitive (age, Age and AGE are three different variables)

#### Valid variable names:

```python
username = 'Athena'
user_name = 'Dionysus'
username_2 = 'Artemis'
_user_name = 'Aphrodite'
userName = 'Poseidon'
USERNAME = 'Hera'
```

#### Invalid variable names:

```python
2username = 'Nyx'  # cannot begin with a number
user-name = 'Hades'  # no hyphens
u$ern&me = 'Cerberus'  # no special characters other than underscores
user name = 'Persephone'  # no spaces
```

[Back to top](#top)

---

### <a id="fstring"></a>f-strings

Let's say we want to print a message to the user with some information that we have about them:

```python
# Variables
name = "Lisa"
city = "Portland"

# print statement with the concatenation
print("Hello " + name + "! Today in " + city + ", it is warm and sunny!")  # Hello Lisa! Today in Portland, it is warm and sunny!
```

Doesn't that look cumbersome? An easier and cleaner way would be to use **f-strings**! We use f-strings to format Python expressions (bits of code) into our strings!

f-strings start with an `f` before the opening quotation mark and code can be placed into the string using curly brackets `{}`. Any code inside an f-string's curly brackets is evaluated and its result is used.

```python
# Variables
city = "Portland"
weather = "warm and sunny"

# print statement with an f-string
print(f"Today in {city}, it is {weather}!")  # Today in Portland, it is warm and sunny!
```

[Back to top](#top)

---

### <a id="input"></a>input()

Example 1:

```python
# this line has three actions!
user_name = input("What is your name?")
# prints a question to the user
# then allows the user to type an input
# saves user input to a variable


print(f"Hello {user_name}!")
# prints "Hello" with the user's name that they typed in!
# outcome: "Hello <user name>"
```

- [input() code demo](https://repl.it/@pdxadmin/input) (Type in your name after the programs asks you for it!)
- [read more here](https://www.w3schools.com/python/ref_func_input.asp)

---

### <a id="numbers"></a>Numbers

Integers are whole numbers. They can positive or negative.

Let's use the example below to calculate how old we are this year.

```python
current_year = 2020  # integer (int)
year_of_birth = 1988  # integer (int)
age = current_year - year_of_birth

print(age)  # 32
```

Floats are one way that Python represents decimal numbers. They can also be positive or negative, but will always contain a decimal.

### Addition:

```python
print(4 + 4)  # 8
```

### Subtraction:

```python
print(8 - 4)  # 4
```

### Multiplication:

```python
print(4 * 4)  # 16
```

### Division:

```python
print(16 / 4)  # 4.0
```

### Exponential:

```python
print(2 ** 3)  # 8
```

### Floor Division:

```python
print(16 // 4) # 4
```

### Error:

```python
# Error! Cannot concatenate string and integer
print(4 + "4")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

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

**Output**

    There were 20 people who were interested in going hiking but 6 have changed their mind. The total number of people going is now 14.

We can also calculate the attendance rate as a percentage

```python
num_of_interested = 20
drop_outs = 6
num_of_attendees = num_of_interested - drop_outs

attendance_rate = (num_of_attendees / num_of_interested) * 100

print(f"There were {num_of_interested} people who were interested in going hiking but {drop_outs} have changed their mind. The total number of people going is now {num_of_attendees}.")

print(f"That's an attendance rate of {attendance_rate}%")
```

**Output**

    There were 20 people who were interested in going hiking but 6 have changed their mind. The total number of people going is now 14.
    That's an attendance rate of 70.0%.

---

## <a id="lab"></a>Lab 02: [Mad Libs](https://github.com/PdxCodeGuild/Programming101/blob/master/labs/madlibs.md)

[Back to top](#top)
