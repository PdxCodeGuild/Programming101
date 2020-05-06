
# Random Emoticon Generator

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

1. Define a list of eyes
2. Define a list of noses
3. Define a list of mouths
4. Randomly pick a set of eyes
5. Randomly pick a nose
6. Randomly pick a mouth
7. Assemble and display the emoticon

You can find examples of emoticons [here](https://en.wikipedia.org/wiki/List_of_emoticons)


```python
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
```

## Advanced Version 1

Use a `for` loop to generate 5 random emoticons.

## Advanced Version 2

In a while loop, ask the user if they want another emoticon

## Advanced Version 3

Ask the user if they want to choose each part of the face. If they do, let the user choose that part of the face. If they don't, randomly generate that part.

## Advanced Version 4

Let the user choose if they want to make one-line horizontal faces like `:-)`, one-line vertical faces like `o_O`, or multi-line vertical faces like:

```python
O O
 |
 ~
```