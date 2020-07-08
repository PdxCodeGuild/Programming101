# <a id="top"></a>Unit 02

[Back to Syllabus](../README.md)

## Table of Contents

- [variables](#variables)
- [f-strings](#fstring)
- [input()](#input)
- [Integers](#integers)

### <a id="variables"></a>Variables

Variables are used to store data that the program will use later.

```python
# a string, "Lisa", is assigned to a variable called name
name = "Lisa"
# we later use that variable in a print statement
print("Hello " + name + "!")
# result: Hello Lisa!
```

A variable's value can be changed after assignment.

```python
# a string, "Lisa", is assigned to a variable called name
name = "Lisa"
# a string, "Anthony", is assigned to a variable called name which OVERWRITES the previous data
# the string, "Lisa", no longers exist!
name = "Anthony"
print("Hello " + name + "!")
# result: Hello Anthony!
```

#### Variable names:
    
- must start with a letter or the underscore character
- cannot start with a number
- can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- are case-sensitive (age, Age and AGE are three different variables)

**Valid variable names:**

    username = 'Athena'
    user_name = 'Dionysus'
    _user_name = 'Aphrodite'
    userName = 'Poseidon'
    USERNAME = 'Hera'
    username2 = 'Artemis'
    
**Invalid variable names:**

    2username = 'Nyx'        # cannot begin with a number
    user-name = 'Hades'      # no hyphens
    u$ern&me = 'Cerberus'    # no special characters other than underscores
    user name = 'Persephone' # no spaces


- [variable code demo](https://repl.it/@pdxadmin/variables)
- [read more here](https://www.w3schools.com/python/python_variables.asp)
- Complete [Exercise 4](https://learnpythonthehardway.org/python3/ex4.html) of Learn Python the Hard Way
  [Back to top](#top)
---
### <a id="fstring">f-strings</a>

Let's say we want to print a message to the user with some information that we have about them:

```python
# Variables
name = "Lisa"
city = "Portland"

# print statement with the concatenation method
print("Hello " + name + "! Today in " + city + ", it is warm and sunny!")
# result: Hello Lisa! Today in Portland, it is warm and sunny!
```

Doesn't that look cumbersome? An easier and cleaner way would be to use f-strings! We use f-strings to format our strings! See below:

```python
# Variables
name = "Lisa"
city = "Portland"

# print statement with the concatenation method
print(f"Hello {name}! Today in {city}, it is warm and sunny!")
# result: Hello Lisa! Today in Portland, it is warm and sunny!
```

- [fstring code demo](https://repl.it/@pdxadmin/fstrings)
- [read more here](https://www.w3schools.com/python/ref_func_print.asp)
- Complete [Exercise 5](https://learnpythonthehardway.org/python3/ex5.html) of Learn Python the Hard Way
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
### <a id="integers"></a>Integers

Integers are an integeral part of programming. In fact, the very first computer program (written by Ada Lovelace) was designed to calculate [Bernoulli numbers](https://en.wikipedia.org/wiki/Bernoulli_number)! I don't know about you but I wouldn't want to calculate _the sequence of rational numbers which occur frequently in number theory_. No, thank you. Which brings us back to integers.

An integer (int) can be a whole number. It can positive or negative. Let's use the example below to calculate how old we are this year.

```python
current_year = 2020
year_of_birth = 1988
age = current_year - year_of_birth

print(age)
```

> 32

### Addition:

```python
print(4 + 4)
```

> 8

### Subtraction:

```python
print(8 - 4)
```

> 4

### Multiplication:

```python
print(4 * 4)
```

> 16

### Division:

```python
print(16 / 4)
```

> 4.0

### Exponential:

```python
print(2 ** 3)
```

> 8

### Floor Division:

```python
print(16 // 4)
```

> 4

### Error:

```python
print(4 + "4")
```

> TypeError: unsupported operand type(s) for +: 'int' and 'str'

- [integers code demo](https://repl.it/@pdxadmin/integers)

#### Lab 03: [Mad Libs](https://github.com/PdxCodeGuild/Programming101/blob/master/labs/madlibs.md)

- [Back to top](#top)
