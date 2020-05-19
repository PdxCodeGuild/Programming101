# <a id="top"></a>Unit 01
[Back to Syllabus](../README.md)

## Table of Contents
- [Comments](#comments)
- [print()](#print)
- [Datatype: Strings](#strings)
- [String Concatenation](#concatenating)

## <a id="comments"></a>Comments

```python
# this is a comment
```

Comments are one of the most useful tools in programming.  Comments can be used to:

- organize code
- explain code
- exclude certain lines of code while testing

### Organizing Code
If you're anything like me, you love, LOVE to organize. From my closet to my kitchen, no item is left unturned. So imagine how excited I was to find that there was a method to organizing your code! Check out the example below.

_You might not understand every single line of code. Don't worry about that for now._

```python
# filename: roll_the_dice.py
# author: lisa of PDX Code Guild

# Modules (modules are libraries we can borrow methods from)
import random

# Logic
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

result = dice1 + dice2

# Result
print(f"You rolled {result}!")
```

### Explain Code

Now the example above is well organized but it could be better! I could use comments to explain what each line is doing. Check out the same example below but with comments explaining the code.

```python
# filename: roll_the_dice.py
# author: lisa of PDX Code Guild

# Modules
# import random so we can use the randint function which chooses a random number between two integers
import random

# Logic
# randomly choose a number between 1 and 6
# then save it to dice1
dice1 = random.randint(1,6)
# do the same as above but save the second number to dice2
dice2 = random.randint(1,6)

# add the value of dice1 and dice2 together; save to a new variable called result
result = dice1 + dice2

# Result
# print the value of the variable result
print(f"You rolled {result}!")
```
Don't the comments make it easier to understand the code? Moving foward, you should add comments to explain your code!

### Exclude code while testing
Below are two print() statements. We use print() when we want to print a message to the screen.

Because there is a hash symbol at the beginning of the second line, _"Hello Pluto!"_ will not run and we will not see it printed to the screen!

```python
print("Hello World!")
# print("Hello Pluto!")
```

#### Assignment
Complete <a href="https://learnpythonthehardway.org/python3/" target="_blank">Exercise 2 of Learn Python the Hard Way</a>.

#### Quiz
Complete this short <a href="https://forms.gle/UkKbHrbnS2ttCSSNA" target="_blank">quiz</a> to test your knowledge.

[Back to top](#top)

## <a id="print"></a>print()

```python
print("Hello! Welcome to my really cool app!")
```

print() is a built-in function in Python. What that means is that it does all the work for you! As long as you have the correct syntax, anything you write in the parenthesis will display on the screen!

#### Assignment
Complete <a href="https://learnpythonthehardway.org/python3/ex5.html" target="_blank">Exercise 5 of Learn Python the Hard Way</a>. You can check out other built-in functions <a href="https://www.w3schools.com/python/python_ref_functions.asp" target="_blank">here</a>.

## <a id="strings"></a>Datatype: Strings
There are many different datatypes in Python. The first one we will explore are Strings. String literals represent textual data.

```python
# Single quotes:
'allows embedded "double" quotes'

# Double quotes:
"allows embedded 'single' quotes".

#Triple quoted:
'''Three single quotes''', """Three double quotes"""
```

Triple quoted strings may **span multiple lines**. All associated whitespace will be included in the string literal.

Some examples of Strings:

```python
# String: Hello Mars!
print("Hello Mars!")

# String: Bucky is my favorite dog!
dog_name = "Bucky"
print(f"{dog_name} is my favorite dog!")
# dog_name is variable where it's dataype is a String.
```
We only use fstrings (format string) when we are embedding the value of a variable in a string when priting. We will learn more about this in <a href="https://github.com/PdxCodeGuild/Programming101/blob/master/units/unit-2.md" target="_blank">Unit 2</a>,

#### Assignment
Complete <a href="https://learnpythonthehardway.org/python3/ex6.html" target="_blank">Exercise 6 of Learn Python the Hard Way</a>

[Back to top](#top)

## <a id="strings"></a>String Concatenation
To concatenate, or combine, two strings you can use the **+** operator.

Example 1:
```python
a = "Hello"
b = "World"
c = a + b
print(c) # outcome: "HelloWorld"
```

Example 2:
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c) # outcome: "Hello World"
```

To practice everythin you learned in Unit 1, please complete Lab 01.
#### Lab 02: [Hello](/labs/hello.md)

[Back to top](#top)
