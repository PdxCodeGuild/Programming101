# Unit 3 Practice Solutions

## Exercise 3 - How many Tweets?

### **3.1**

**Solution**

    import math

    # ask the user for number of characters in message
    characters = 1345

    # Tweets are 280 characters max
    max_per_tweet = 280

    # calculate the number of Tweets needed, rounding up
    # with math.ceil()
    tweets_needed = math.ceil(characters/max_per_tweet)

    # place commas in appropriate places in characters with :,
    result = f'''A message containing {characters:,} characters will require {tweets_needed} Tweets.'''

**Output**

    A message containing 1,345 characters will require 5 Tweets.

---

### **3.2**

**Solution**

    

**Output**

    

---

### **3.3**

**Solution**

    


**Output**

    

## [< Exercise 2](../exercise_2.md)

### [<< Back to Unit 3 Practice](/practice/unit_3/)
