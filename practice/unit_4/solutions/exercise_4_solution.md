# Unit 4 Practice Solutions

## **w**

### **4.1**

Using a for loop, ask the user for the name of three items (animals, colors, fruits, or whatever you'd like).

**Solution**

```python
# empty list
animals = []

for i in range(3):
    # ask the user for an animal
    animal = input("Enter an animal: ")
    # add it to the list
    animals.append(animal)

print(f'animals: {animals}')
```

**Output**

    Enter an animal: lynx
    Enter an animal: ocelot
    Enter an animal: jaguar

    animals: ['lynx', 'ocelot', 'puma']

### **4.2**

Loop through the user's list and with iteration, print both the item and all the letters in the item

**Solution**

```python
# empty list
animals = []

# ask the user for three animals
for i in range(3):
    # ask the user for an animal
    animal = input("Enter an animal: ")
    # add it to the list
    animals.append(animal)

# loop through the animals
for animal in animals:
    # print the current animal name
    print(animal)

# loop through the letters in the animal name
for letter in animal:
    # print the current letter
    print(letter)
```

**Output**

    Enter an animal: lynx
    Enter an animal: ocelot
    Enter an animal: puma

    lynx
    l
    y
    n
    x
    ocelot
    o
    c
    e
    l
    o
    t
    puma
    p
    u
    m
    a

### **4.3**

**Solution**

```python
# empty list
animals = []

# ask the user for three animals
for i in range(3):
    # ask the user for an animal
    animal = input("Enter an animal: ")
    # add it to the list
    animals.append(animal)

# empty list
letters_used = []

# loop through the animals
for animal in animals:

    # loop through the letters in the animal name
    for letter in animal:

        # if the letter isn't in the characters list,
        if letter not in letters_used:
            # add it
            letters_used.append(letter)

# display result
print(f'letters used: {letters_used}')
```

**Output**

    Enter an animal: lynx
    Enter an animal: ocelot
    Enter an animal: puma

    Letters used:
    ['l', 'y', 'n', 'x', 'o', 'c', 'e', 't', 'p', 'u', 'm', 'a']

Keep in mind that is is just one potential solution

## [< Exercise 4](../exercise_4.md)

---

### [<< Back to Unit 4 Practice](/practice/unit_4/)
