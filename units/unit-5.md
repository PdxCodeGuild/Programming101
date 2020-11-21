# <a id="top"></a>Unit 05

[Back to Syllabus](../README.md)

## Table of Contents

- [String Module](#string)
- [while loop](#while)
- [break](#break)
- [continue](#continue)
- [else](#else)

## <a id="string"></a>String Module

The String module contains tools for working with strings. You can read the official docs [here](https://docs.python.org/3/library/string.html).

```python
# Including the String module
import string

# string module constants
print(string.ascii_letters)
# result: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
# result: abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
# result: ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
# result: 0123456789
print(string.hexdigits)
# result: 0123456789abcdefABCDEF
print(string.whitespace)
# result:
print(string.punctuation)
# result: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## <a id="while"></a>Loops: while

Do something while statement is `True`.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
```

## <a id="break"></a>Loops: break

The break keyword is used to break out of a loop.

```python
for i in range(10): # for each number 0-9, run the following
  if i == 3: # on every loop, check if i == 3
    print('skip 3')

    # return to the top of the loop
    continue

  if i == 7:
    print('Goodbye!')

    # exit the loop
    break

  print(i) # print the current value of i
```

## <a id="continue"></a>Loops: continue

```python
# Skip the iteration if the variable i is 3, but continue with the next iteration:
for i in range(9):
  if i == 3:
    continue
  print(i)
```

## <a id="else"></a>Loops: else

Do something while statement is `True`. When it is no longer `True`, do something `else`. The `else` code block will only be triggered if a loop ends "naturally", when its condition becomes `False`. It will not be triggered if a loop is broken with `break`.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
else: # the moment, i is 6, the while statement goes from True to False
  print("i is no longer less than 6") # this will now print
```

## Lab 5 - [Password Generator](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab08-password_generator.md)

[Back to top](#top)
