# <a id="top"></a>Unit 02
[Back to Syllabus](../README.md)

## Table of Contents
- [variables](#variables)
- [f-strings](#fstring)
- [input()](#input)
- [Random Module](#random)
- [Integers](#integers)
- [Operators](#operators)

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
- [variable code demo](https://repl.it/@pdxadmin/variables)
- [read more here](https://www.w3schools.com/python/python_variables.asp)
- Complete [Exercise 4](https://learnpythonthehardway.org/python3/ex4.html) of Learn Python the Hard Way
[Back to top](#top)

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
print(f"Hello ${name}! Today in ${city}, it is warm and sunny!")
# result: Hello Lisa! Today in Portland, it is warm and sunny!
```

- [fstring code demo](https://repl.it/@pdxadmin/fstrings)
- [read more here](https://www.w3schools.com/python/ref_func_print.asp)
- Complete [Exercise 5](https://learnpythonthehardway.org/python3/ex5.html) of Learn Python the Hard Way
[Back to top](#top)

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

#### Lab 03: [Mad Libs](https://github.com/PdxCodeGuild/Programming101/blob/master/labs/lab03_madlibs.md)

[Back to top](#top)

### <a id="random"></a>Random Module

Modules are a Python object that are sources of related code; think of if as a library of information. A code library, if you will! It is a file containing a set of functions you want to include in your application. (For a list of all modules, you can check out the offical [Python docs](https://docs.python.org/3/py-modindex.html)). For this lesson, we will be looking at the [random module](https://pynative.com/python-random-module/). And specifically, we will be looking at the choice() function of the random module: [random.choice()](https://www.w3schools.com/python/ref_random_choice.asp). Please see the example below:

```python
# include the random module in our file
import random

# a list of fruits
fruits = ["apple", "banana", "cherry"]

# randomly choose a fruit and save it to a variable, chosen_fruit
# choice() is a function inside the random module. we use it by writing random.choice()
# the list in which you want the program to choose from, needs to go inside the parenthesis of choice()
chosen_fruit = random.choice(fruits)

# print the value of variable chosen_fruit
print(chosen_fruit)
```
- [random module code demo](https://repl.it/@pdxadmin/random)
- [Back to top](#top)

### <a id="integers"></a>integers

[Back to top](#top)

### <a id="operators"></a>Operators

[Back to top](#top)
