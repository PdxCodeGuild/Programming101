# Unit 3 Practice Solutions

## Exercise 2 - String Comparisons

### **2.1**

**Solution**

```python
#Assign a letter to a variable to serve as the secret answer
secret = 'a'

# Ask the user to enter a letter, assign it to a variable
guess = input('Please guess a letter a-z: ')

# if the user's letter is the same as the answer, inform the user they've guessed correctly. Otherwise, inform them they've erred and display the correct answer.
if guess == secret:
message = f"You guessed the secret letter '{secret}'!"
else:
message = f"Your guess of '{guess}' was incorrect."

print(message)
```

**Output**

    Please guess a letter a-z: a
    You guessed the secret letter 'a'!
    ---

    Please guess a letter a-z: z
    Your guess of 'z' was incorrect.

---

### **2.2**

**Solution**

```python
#Ask the user for a word
word = input("Enter a word: ")

# Ask the user for a letter
letter = input("Enter a letter: ")

# Use the keyword in to determine if the letter is in the word
# Tell the user if the letter is in the word. Display the letter in uppercase

if letter in word:
    message = f'The letter "{letter.upper()}" is in the word {word}.'
else:
    message = f'The letter "{letter.upper()}" is not in the word {word}.'


print(message)
```

**Output**

    Enter a word: umbrella
    Enter a letter: b

    The word "umbrella" contains the letter "B".
    -------------------

    Enter a word: umbrella
    Enter a letter: z

    The word "umbrella" does not contain the letter "Z".

---

### **2.3**

**Solution**

```python
#Ask the user for a word
word = input("Enter a word: ")

# Ask the user for a letter
letter = input("Enter a letter: ")

# Use the keyword in to determine if the letter is in the word
# Tell the user if the letter is in the word. Display the letter in uppercase

if letter in word:

    # count the occurances of the letter in the word
    letter_count = word.count(letter)

    message = f'The word "{word}" contains the letter "{letter.upper()}" {letter_count} times.'
else:
    message = f'The letter "{letter.upper()}" is not in the word {word}.'

print(message)
```

**Output**

    Enter a word: giraffe
    Enter a letter: f

    The word "giraffe" contains the letter "F" 2 times.
    ---

    Enter a word: hippopotamus
    Enter a letter: f

    The word "hippopotamus" does not contain the letter "F".

## [< Exercise 2](../exercise_2.md)

### [<< Back to Unit 3 Practice](/practice/unit_3/)
