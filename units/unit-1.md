# <a id="top"></a>Unit 01

[Back to Syllabus](../README.md)

## Table of Contents

- [Comments](#comments)
- [The `print()` function](#print)
- [Datatype: Strings](#strings)
- [String Concatenation](#concatenating)
- [String Methods](#methods)
- [Escape Characters](#escape)
- [Unit 1 Lab](#lab)

## <a id="comments"></a>Comments

```python
# this is a comment
```

Comments are one of the most useful tools in programming. Comments can be used to:

### organize code

```python
# 10/07/2020
# ------------------ #
print('Welcome to Python!')

# --- say hello! --- #
print('Hello!')
```

### explain code

```python
# express an opinion about spam
print("I don't like spam!")
```

### exclude certain lines of code while testing

```python
print("Hello friends!")
# print("Hello nobody!") # this line is excluded using a comment
```

[Back to top](#top)

## <a id="print"></a>The `print()` function

```python
print("Hello! Welcome to my really cool app!")
```

`print()` is a built-in function in Python. Functions can be used to perform a variety of tasks. The parentheses are **required** in order for the function to work properly.

Data can be passed into the `print()` function's parentheses and that data will be displayed in the terminal. If no data is privided to `print()`, it displays a blank line.

```python
print('Hello world!') # Hello world!
print() # prints a blank line
print(4 + 4) # 8
```

[Back to top](#top)

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
# String: Hello, friends!
print("Hello, friends!")

# String: Welcome to PDX Code Guild!
print("Welcome to PDX Code Guild!")
```

We only use f
[Back to top](#top)

## <a id="strings"></a>String Concatenation

To concatenate, or combine, two strings you can use the **+** operator.

Strings will be printed **_exactly_** as they're written.

```python
print("PDX" + "Code" + "Guild") # PDXCodeGuild
```

If we want spaces between our strings, we have to include them ourselves.

```python
# spaces inside another string
print("PDX" + " Code " + "Guild") # PDX Code Guild

# spaces inside their own strings
print("PDX" + " " + "Code" + " " + "Guild") # PDX Code Guild
```

## <a id="methods"></a>Methods

Methods give datatypes more functionality. They allow you to work with Strings in a more useful way. You can learn more about [String methods here.](https://www.w3schools.com/python/python_ref_string.asp)

### Common string methods:

| method       | description                                               | example                    | result        |
| ------------ | --------------------------------------------------------- | -------------------------- | ------------- |
| capitalize() | Converts the first letter to uppercase                    | "hello world".capitalize() | "Hello world" |
| lower()      | Converts a string to lowercase                            | "Hello World".lower()      | "hello world" |
| strip()      | Removes whitespace from the beginning and end of a string | " Hello World ".strip()    | "Hello World" |
| title()      | Converts the first character of each word to uppercase    | "hello world".title()      | "Hello World" |
| upper()      | Converts a string to uppercase                            | "hello world".upper()      | "HELLO WORLD" |

## <a id="escape"></a>Escape Characters

Escape characters allow us to use special characters inside a string. They also allow us to use 'illegal' characters in a string, such as a double quote withing a string surrounded by double quotes.
An escape character is a `\` followed by the character you want to insert.
Below are a few examples:
|code|result|
|---|---|
|`\'`|Single Quote|
|`\"`|Double Quote|
|`\\`|Backslash|
|`\n`|New Line|
|`\t`|Tab|

To practice everything you learned in Unit 1, please complete the following lab:

## <a id="lab"></a> Lab 01: [Hello](/labs/hello.md)

[Back to top](#top)
