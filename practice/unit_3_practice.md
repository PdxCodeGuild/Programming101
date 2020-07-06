# **Unit 3 Practice**

## **Exercise 1**

Let's do a little geometry!

### **1.1**

- Create three variables `a`, `b` and `c`.

- Assign a number to each to represent the lengths of the sides of a **triangle**.

- Calculate the `perimeter` of the triangle

        a: 3
        b: 4
        c: 5

        output:
        A triangle with sides of 3, 4, and 5 has a perimeter of 12.

### **1.2**

- Create variables with numbers representing the `base` and `height` measurements of the **triangle**. Select `a`, `b` or `c` to represent the `base`.

- Calculate the `area` of the triangle.

        base: 5         
        height: 8       

        output:
        A triangle with a base of 5 and a height of 8 has an area of 20.0.      
        ---

        base: 2.8
        height: 2.02

        output:
        A triangle with a base of 2.8 and a height of 2.02 has an area of 3.08.

### **1.3**

- `import` the `math` module.

- Find the `hypotenuse` (`c`) of a **triangle** given sides `a` and `b`.

- Hint: The `math` module contains a method for calculating **square roots**.

- Assign a number to a variable torepresent the `radius` of a circle.
- Use the constant for `pi`contained within the `math` module and the `radius` *variable* to calculate the `circumference` and `area` of a ***circle***.

        output:
        
        Circle

        Radius: 5
        Circumference: 31.4159...
        Area: 78.5398...

### **1.4**

- Calculate the `volume` of a ***sphere*** with the same `radius`.

        output:

        Sphere

        Radius: 5
        Volume: 523.5987...

### **1.5**

- Assign a number to a variable to represent the `radius` of a **second** circle.
- Use the two radii to calculate the area of an  [annulus](https://www.google.com/search?q=annulus%20area).


### **Extra challenges**

### **1.6**

- Create two variables, `a` and `b` to represent the adjacent sides of a right triangle.

- Find the **hypotenuse** of a triangle using `a` and `b`. Assign the value to a variable `c`.

- Display the result to the user

      a: 65
      b: 72
      c: 97

      output:
      A triangle with sides of 65 and 72 has a hypotenuse of 97.

### **1.7**

Use the `random` module to generate **random integer** values for the circle and sphere's `radius` and the triangle's `base` and `height`.

### **1.8**

Have the user enter all number values used in previous versions. Don't forget that `input()` always returns a `string`.

## **Exercise 2**

### **2.1**

- Assign a letter to a variable to serve as the secret `answer`
- Ask the user to enter a `letter`, assign it to a variable
- `if` the user's `letter` is the same as the `answer`, inform the user they've guessed correctly. Otherwise, inform them they've erred and display the correct answer.

### **2.2**

- Ask the user for a `word`
- Ask the user for a `letter`
- Assign the `word` and the `letter` to variables
- Tell the user `if` the `letter` is `in` the `word`. Display the letter in uppercase
  
      Enter a word: umbrella
      Enter a letter: b

      output:
      The word "umbrella" contains the letter "B".

      -------------------
      Enter a word: umbrella
      Enter a letter: z

      output:
      The word "umbrella" does not contain the letter "Z".

### **2.3**

  If the word contains the letter, tell the user how many times the letter is in the word

      Enter a word: giraffe
      Enter a letter: f

      output:
      The word "giraffe" contains the letter "F" 2 times.

### **2.4**

  Using string methods, determine if the string the user entered contains only letters, no spaces, numbers or special characters.

  `if` the string contains characters **other than letters**, inform the user that those characters aren't allowed.

## **Exercise 3**

You've got a very important message to get out to all your followers on Twitter. Unfortunately, Twitter only allows **280** characters per Tweet. Your message is **over 1,000** characters long and you're wondering **how many** Tweets it will take to get your whole message out.

### **3.1**

Calculate the number of Tweets required, **rounding up** to the nearest integer.

### **3.2**

Ask the user for the `number of characters` in their message

- `if` the length of the message is **less than** the `max_length` allowed for a Tweet, output a `message` telling the user they only need one Tweet

- Otherwise, calculate the number of Tweets required, **rounding up** to the nearest integer and output a `message` telling the user the number of Tweets they will need.

### **3.3**

Display different messages to the user depending on how many Tweets their message requires.

## **Exercise 4**

### **4.1**

- Assign a `number` to a variable.

- Determine whether the number is within 10 of 100.

      number: 92
      output: 92 is within 10 of 100.

      number: 51
      output: 51 is not within 10 of 100.

### **4.2**

- Have the user enter values for `number_1` and `number_2`.

- Have the user choose the `limit` of how many numbers may be in between the two.

- Determine whether `number_1` and `number_2` are within the limit set by the user.

      number 1: 800
      number 2: 1200
      limit: 500

      output:
      800 is within 500 of 1200

      ---------
      number 1: 1575
      number 2: 1200
      limit: 500

      output:
      1575 is within 500 of 1200
      
      --------
      number 1: 1000
      number 2: 15
      limit: 3

      output:
      15 is not within 3 of 1000
