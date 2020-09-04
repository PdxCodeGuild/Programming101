# Unit 3 Practice Solutions

## Exercise 1 - Geometry

### **1.1**

**Solution**

```python
# Create three variables a, b and c
# Assign a number to each to represent the lengths of the sides of a triangle
a = 3
b = 4
c = 5

# Calculate the perimeter of the triangle
perimeter = a + b + c

# print using an f-string
print(f'A triangle with sides of {a}, {b}, and {c} has a perimeter of {perimeter}.')
```

**Output**

    A triangle with sides of 3, 4, and 5 has a perimeter of 12.

---

### **1.2**

**Solution**

```python
# Create three variables a, b and c
# Assign a number to each to represent the lengths of the sides of a triangle
a = 3
b = 4
c = 5

# Select a, b or c to represent the base
base = c
# Create variables representing the height
height = 8


# Calculate the area
area = .5 * (base * height)

# print using an f-string
print(f'A triangle with a base of {base} and a height of {height} has an area of {area}.')
```

**Output**

    A triangle with a base of 5 and a height of 8 has an area of 20.0.

---

### **1.3**

**Solution**

```python
import math # for pi constant

#Assign a number to a variable torepresent the radius of a circle.
radius = 5

# calculate the circumference and area
circumference = 2 * math.pi * radius

area = math.pi * (radius ** 2)

print(f'''
Circle

Radius: {radius}
Circumference: {circumference}
Area: {area}
''')
```

**Output**

    Circle

    Radius: 5
    Circumference: 31.41592653589793
    Area: 78.53981633974483

---

### **1.4**

**Solution**

```python
import math # for pi constant

#Assign a number to a variable torepresent the radius of a sphere.
radius = 5

# calculate spherical volume

volume = (4/3) * math.pi * (radius ** 3)

print(f'''
Sphere

Radius: {radius}
Volume: {volume}
''')
```

**Output**

    Sphere

    Radius: 5
    Volume: 523.5987755982989

---

### **1.5**

**Solution**

```python
import math # for pi constant

# outer and inner radii
outer_radius = 5
inner_radius = 3

# calculate the area
annulus_area = math.pi * (outer_radius ** 2 - inner_radius ** 2)

print(f'''
Annulus

Outer radius: {outer_radius}
Inner radius: {inner_radius}

Area: {annulus_area}
''')
```

**Output**

    Annulus

    Outer Radius: 5
    Inner Radius: 3
    Area: 50.26548245743669

---

### **1.6**

**Solution**

```python
import math # for the square root function sqrt()

# Assign a number to each to represent two sides adjacent sides of a triangle
a = 3
b = 4

# calculate the hypotenuse with Pythagorean Theorem
hypotenuse = math.sqrt(a**2 + b**2)

# print using an f-string
print(f'A triangle adjacent sides of {a} and {b} has a hypotenuse of {hypotenuse}.')
```

**Output**

    A triangle adjacent sides of 3 and 4 has a hypotenuse of 5.0.

---

### **1.7**

The solution will be the same except with all numbers fulfilled by `random.randint()`

### **1.8**

The solution will be the same except with all numbers collected from the user using `input()`. You can then convert the number to an integer using `int()` or a float using `float()`.

Keep in mind that this is just one potential solution.

## [< Exercise 1](../exercise_1.md)

### [<< Back to Unit 3 Practice](/practice/unit_3/)
