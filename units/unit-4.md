# <a id="top"></a>Unit 04

[Back to Syllabus](../README.md)

## Table of Contents

- [Datatype: Lists](#lists)
- [Modules](#modules)
- [for item in sequence](#each)
- [for x in range()](#range)

## <a id="lists"></a>Datatype: Lists

A list is a collection of items which are ordered and changeable. In Python lists are written with square brackets.

```python
fruits = [] # empty list
fruits = ["apple", "banana", "cherry"] # initialized list with three items
print(fruits) #outcome: ["apple", "banana", "cherry"]

# print the item at this index position
print(fruits[0]) #outcome: "apple"
print(fruits[1]) #outcome: "banana"
print(fruits[2]) #outcome: "cherry"

# for each item in the fruit list, print the item and its index
for fruit in fruits:
  print(f"{fruit} has an index of {fruits.index(fruit)}")
```

- [List code demo](https://repl.it/@pdxadmin/lists)
- [List Overview](https://www.w3schools.com/python/python_lists.asp)
- [List Methods](https://www.w3schools.com/python/python_ref_list.asp)

## <a id="modules"></a>Modules

Modules are sources of code; similar to a library. It is a file containing a set of functions you want to include in your application. (For a list of all modules, you can check out the offical [Python docs](https://docs.python.org/3/py-modindex.html)). For this lesson, we will be looking at the [random module](https://pynative.com/python-random-module/). And specifically, we will be looking at the `choice()` function of the random module: [random.choice()](https://www.w3schools.com/python/ref_random_choice.asp). Please see the example below:

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

[Back to top](#top)

## <a id="each"></a>Loops: for item in sequence

Do something to each item in a list.

```python
# initialize a list with student names and save to a variable, students
students = ["Al", "Anthony", "Lisa"]

# the student variable will hold each subsequent student as we pass through the students list
for student in students: # for each item in the list, do this:
  print(f"Hello {student}")
```

Outcome: each item of the list printed on a new line:

```bash
Hello Al
Hello Anthony
Hello Lisa
```

## <a id="range"></a>Loops: for x in range()

Do something for a set number of times.

```python
# the x below is a counter. it will keep track of what number loop we are on
for x in range(3): # do the following 3 times
  print("Hello!") # this is done 3 times
```

Outcome: each item of the list is printed on a new line

```bash
Hello
Hello
Hello
```

#### Lab 06: [Rock, Paper, Scissors](/labs/rps.md)

[Back to top](#top)
