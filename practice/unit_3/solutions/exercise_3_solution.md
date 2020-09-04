# Unit 3 Practice Solutions

## Exercise 3 - How many Tweets?

### **3.1**

**Solution**

```python
import math

# number of characters in message
num_characters = 1345

# Tweets are 280 characters max
max_per_tweet = 280

# calculate the number of Tweets needed, rounding up
# with math.ceil()
tweets_needed = math.ceil(num_characters/max_per_tweet)

# place commas in appropriate places in characters with :,
message = f'''A message containing {num_characters:,} characters will require {tweets_needed} Tweets.'''
```

**Output**

    A message containing 1,345 characters will require 5 Tweets.

---

### **3.2**

**Solution**

```python
import math

# ask the user for number of characters in message
num_characters = input("Enter the number of characters: ")

# convert to an integer to perform math operations and comparisons
num_characters = int(num_characters)

# Tweets are 280 characters max
max_per_tweet = 280

# the user's message has less than 280 characters,
# they only need one Tweet
if num_characters < max_per_tweet:
    message = f'A message with {num_characters} characters only requires one Tweet!'
else:
    # calculate the number of Tweets needed, rounding up
    # with math.ceil()
    tweets_needed = math.ceil(num_characters/max_per_tweet)


    # place commas in appropriate places in characters with :,
    message = f'''A message containing {num_characters:,} characters will require {tweets_needed} Tweets.'''

print(message)
```

**Output**

    Enter the number of characters: 12

    A message with 12 characters only requires one Tweet!
    ---

    Enter the number of characters: 12345

    A message containing 12,345 characters will require 45 Tweets.

---

### **3.3**

**Solution**

```python
import math

# ask the user for number of characters in message
num_characters = input("Enter the number of characters: ")

# convert to an integer to perform math operations and comparisons
num_characters = int(num_characters)

# Tweets are 280 characters max
max_per_tweet = 280

# the user's message has less than 280 characters,
# they only need one Tweet
if num_characters < max_per_tweet:
    message = f'A message with {num_characters} characters only requires one Tweet!'
else:
    # calculate the number of Tweets needed, rounding up
    # with math.ceil()
    tweets_needed = math.ceil(num_characters/max_per_tweet)


if tweets_needed < 3:
    comment = '\n\nThat should\'t take you too long!'
elif tweets_needed < 10:
    comment = '\n\nYou\'d better get typing!'
elif tweets_needed >= 10:
    comment = '\n\nMaybe you should find a different medium...'

# place commas in appropriate places in characters with :,
message = f'''A message containing {num_characters:,} characters will require {tweets_needed} Tweets.'''

# add the comment to the message
message += comment

print(message)
```

**Output**

    Enter the number of characters: 300

    A message containing 300 characters will require 2 Tweets.

    That should't take you too long!
    ---

    Enter the number of characters: 1000

    A message containing 1,000 characters will require 4 Tweets.

    You'd better get typing!
    ---

    Enter the number of characters: 10000

    A message containing 10,000 characters will require 36 Tweets.

    Maybe you should find a different medium...

## [< Exercise 3](../exercise_3.md)

### [<< Back to Unit 3 Practice](/practice/unit_3/)
