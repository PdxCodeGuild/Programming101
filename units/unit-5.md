# <a id="top"></a>Unit 05
[Back to Syllabus](../README.md)

## Table of Contents
- [String Module](#string)
- [while loop](#while)
- [else](#else)

## <a id="string"></a>String Module
- [official docs](https://docs.python.org/3/library/string.html)

```python
# including the string module in our file
import string

# string.ascii_letters returns all upper and lower capital letters
letters = string.ascii_letters

print(letters)
# outcome: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
```
#### Lab 08: [Password Generator](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab08-password_generator.md)

## <a id="while"></a>Loops: while
Do something while statement is true.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
```

Complete [Exercise 1](https://www.w3schools.com/python/exercise.asp?filename=exercise_while_loops1) of PYTHON Loops.

## <a id="else"></a>Loops: else
Do something while statement is true. When it is no longer true, do something else.

Complete [Exercise 2](https://www.w3schools.com/python/exercise.asp?filename=exercise_while_loops2) of PYTHON Loops.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
else: # the moment, i is 6, the while statement goes from True to False
  print("i is no longer less than 6") # this will now print
```

Complete [Exercise 3](https://www.w3schools.com/python/exercise.asp?filename=exercise_while_loops3) of PYTHON Loops.

[Back to top](#top)