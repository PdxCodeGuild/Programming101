# Unit 5 Practice Solutions

## Exercise 1 - Count Sheep

### **1.1**

**Solution**

```python
import random

# Generate a random number between 1 and 10 to represent the number of sheep needed to fall asleep.
sheep_to_sleep = random.randint(1,10)

# you are still awake
awake = True

# count sheep until you fall asleep

# counter variable
sheep = 0

# count sheep
while awake: # same as awake == True
    print(f'{sheep + 1} sheep - baa!')

    # add one sheep_to_sleep
    sheep += 1

    # fall asleep
    if sheep == sheep_to_sleep:
        awake = False

# sweet dreams
print('\n...zZzZzZzZ...')
```

**Output**

    1 sheep - baa!
    2 sheep - baa!
    3 sheep - baa!
    4 sheep - baa!
    5 sheep - baa!
    6 sheep - baa!
    7 sheep - baa!
    8 sheep - baa!
    9 sheep - baa!

    ...zZzZzZzZ...

## [< Exercise 1](../exercise_1.md) | [Exercise 2 >](../exercise_2.md)

### [<< Back to Unit 5 Practice](/practice/unit_5/)
