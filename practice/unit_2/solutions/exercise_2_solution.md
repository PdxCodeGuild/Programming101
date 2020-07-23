# Unit 2 Practice Solutions

## Exercise 2

Use string methods to determine the number of times a `letter` occurs in a `word`

### **2.1**

**Solution**

    word = 'bookkeeper'
    letter = 'k'

    # use the .count() string method to count the occurrences of the letter in the word
    letter_count = word.count(letter)

    print(f"The letter '{letter}' occurs in the word '{word}' {letter_count} times.")

**Output**

    Output:
    The letter 'k' occurs 2 times in 'bookkeeper'

### **2.2**

In version 2.2, the user enters values for `word` and `letter` using `input()`.

**Solution**

    # get a word and a letter from the user
    word = input('Please enter a word: ')
    letter = input('Please enter a letter: ')

    # use the .count() string method to count the occurrences of the letter in the word
    letter_count = word.count(letter)

    print(f"The letter '{letter}' occurs in the word '{word}' {letter_count} times.")

**Output**

    Enter a word: hippopotamus
    Enter a letter to count: p

    The letter 'p' occurs 3 times in 'hippopotamus'


Keep in mind that this is just one potential solution.

## [< Exercise 2](../exercise_2.md)

### [<< Back to Unit 2 Practice](/practice/unit_2/)
