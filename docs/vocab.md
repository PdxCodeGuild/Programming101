# Programming Vocab

<a href="#"></a>

## Argument

- An object passed to a function to fill one of its parameters

- When a function is called, arguments are passed to fill the functions parameters

## Class

- A data structure which acts as a blueprint for creating objects.

- All Python datatypes are created with classes.

- When we create an object, we're creating an 'instance' of a pre-defined class which shares all the attributes of the class but can have properties unique to each instance

- Classes have attributes which can be functions or variables

## Code Block

- A section of code that executes together

- In Python, code blocks are defined using horizontal indentation.

- The first line of code in a code block determines its indentation and all subsequent lines in that block must match that indentation.

## Concatenation
- Adding two strings together with a plus sign (`+`) to form a single string

## Docstring

- A multi-line string at the beginning of a function's code block that provides documentation about the function, its parameters and its return value

## Function

- A named code block that performs a specific task.

- Functions reduce repetition in our code by allowing us to write code in a generic way and use it with multiple values.

- Functions are executed with parentheses after their name. (e.g. `print()`)

## Immutable (Unchangeable)
If an object is immutable, it cannot be given a new value directly. Instead, a new copy of the object will need to be created with the desired changes applied.

See "Mutable"

## Index

- An item's position in a sequence (list, string, etc.)

- Indices are always integers and must correspond to an existing item in the sequence, otherwise an `IndexError` will be raised.

## Loop

- A code block that repeats until a certain condition is met.

- With a `for` loop, the condition is that there are more items left in the `sequence`

- With a `while` loop, we define the condition directly.

## Method

- A function that only manipulates the object to which it belongs

## Module
A Python file containing code that can be imported into another Python file to be used. 

All the code in the global scope of a module is run when that module is 

## Mutable (Changeable)
If an object is mutable, it has the ability to be given a new value without needing to create a new instance of the object.

See "Immutable"

## Object

- A collection of variables and methods that act on those variables. 

- A class is a blueprint for an object.

- The variables and methods contained in an object are called its 'attributes'

- An object's attributes are accessed with dot notation (e.g. `'abc'.upper()`) 

## Operand

- A piece of data being used to perform an operation

## Operation

- Any process that manipulates data (operands)

## Operator

- A symbol or word that performs an operation on one or more pieces of data (operands)

## Ordered Sequence

- A sequence whose items can be retrieved using their position in the sequence

- An item's position in a sequence is called its 'index'. 

- Lists (`list`) and Strings (`str`) are examples of ordered sequences. 

- Python Sets (`set`) are an example of an *un*-ordered sequence.

## Parameter
An empty variable in the definition of a function which will hold the values which are to be used in the function.

When a function is called, values are passed through the parentheses in the function call and those values are assigned to the parameters and then passed into the function's code block.

Parameters can also be given default values that will be used if no value is passed for that parameter.

```python
# 'a' and 'b' are parameters
# 'b' has a default value of 1
def add(a, b=1): 
    '''return the sum of two numbers, 'a' and 'b''''
    return a + b
```


## Return Value
The value that is sent back from a function to the location where the function was called. 

The return value takes the place of the function call as the code is evaluated. 

## Scope
Four levels in which variables exist in any Python file. Data in outer scopes are available to inner scopes, but data in inner scopes isn't available to outer scopes. 

Data can be returned from functions to make it available to outer scopes.

### Levels of scope
**Built-in** - Everything included behind-the-scenes in a Python file

**Global** - Everything created in the Python file

**Enclosed** - Everything defined within the code block of a global function

**Local** - Everything within the code block of an enclosed function

## Sequence
A collection of items. Sequences can be ordered (e.g. lists and strings) or unordered (e.g. sets and dictionaries)

If a sequence is ordered, its items can be retrieved using their positions in the list.

## Subscriptable
The quality of being able to use an index or key to retrieve a value from an object.


## Typecasting
The process of converting one type of data to another.
## Variable
- A named storage space for data. 

- Variables can store objects of any datatype and can be used in operations involving that datatype.

- Variables can be re-defined with new values at any time.






