# <a id="top"></a>Unit 04
[Back to Syllabus](https://github.com/PdxCodeGuild/Programming101#top)

## Table of Contents
- [Datatype: Lists](#lists)
- [Modules](#modules)
- [for each](#each)
- [for x in range()](#range)
- [break](#break)
- [continue](#continue)

## <a id="lists"></a>Lists
- [List Overview](https://www.w3schools.com/python/python_lists.asp)
- [List Methods](https://www.w3schools.com/python/python_ref_list.asp)

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

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

## <a id="modules"></a>Modules
Modules are sources of code; similar to a library. It is a file containing a set of functions you want to include in your application. (For a list of all modules, you can check out the offical [Python docs](https://docs.python.org/3/py-modindex.html)). For this lesson, we will be looking at the [random module](https://pynative.com/python-random-module/). And specifically, we will be looking at the choice() function of the random module: [random.choice()](https://www.w3schools.com/python/ref_random_choice.asp). Please see the example below:

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
Let's practice random.choice() in the next lab.

#### Lab 03: [Magic 8 Ball](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab03-magic_8_ball.md)

## <a id="each"></a>Loops: for each

Do something to each item in a list.

```python
# initialize a list with student names and save to a variable, students
students = ["Al", "Anthony", "Lisa"]
# the student variable only exists in this for loop. you cannot use "student" anywhere else
# studentS is the list variable we created a bove
for student in students: # for each item in the list, do this:
  print(f"Hello {student}")
```

Outcome: each item of the list printed on a new line
```
Hello Al
Hello Anthony
Hello Lisa
```

Complete [Exercise 6](https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops3) of PYTHON Loops.

## <a id="range"></a>Loops: for x in range()

Do something for a set number of times.

```python
# x here is just a placeholder. it will do the counting for us
for x in range(3): # do the following 3 times
  print("Hello!")

# outcome: each item of the list on a new line
Hello
Hello
Hello
```

Complete [Exercise 5](https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops2) of PYTHON Loops.

## <a id="break"></a>Loops: break

The break keyword is used to break out a for loop, or a while loop.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  if i == 3: # on every loop, check if i == 3
    break # if it does, exit the while loop and stop counting
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
```

## <a id="continue"></a>Loops: continue

```python
# Skip the iteration if the variable i is 3, but continue with the next iteration:
for i in range(9):
  if i == 3:
    continue
  print(i)
```
Complete [Exercise 4](https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops1) of PYTHON Loops.

## Additional Resources
- Loops & Iteration
  - [article](https://www.py4e.com/html3/05-iterations)
  - [slides](https://www.py4e.com/lectures3/Pythonlearn-05-Iterations.pptx)
  - [video](https://www.youtube.com/watch?v=8DvywoWv6fI&t=8121s) (2:15:21 - 2:58:38)

[Back to top](#top)