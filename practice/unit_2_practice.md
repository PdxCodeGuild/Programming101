**Unit 2 Practice**
===================

**Exercise 1**
---------
### **1.1**
- Ask the user to enter a mailing address
  - Street
  - City
  - State
  - Zip Code
  
- Assign the value of each field to a variable
  
- Display the address back to the user using an `f-string`

      Enter street: 231 Faux Ave.
      Enter city: Portland
      Enter state: Oregon
      Enter zip code: 97211

      Output:
      231 Faux Ave.
      Portland, Oregon
      97211

### **1.2**
  Using string methods, ensure that the
address will be properly capitalized, no matter how
it's entered. 

        Enter address: 231 fAUx aVE.
        Enter city: poRtlANd
        Enter state: orEGOn
        Enter zip code: 97211

        Output:
        231 Faux Ave.
        Portland, Oregon
        97211



**Excercise 2**
--------------
### **2.1** 
Use string methods to determine the number of times
a letter occurs in a word

        word: bookkeeper
        letter: k
        
        output: 2

### **2.2**
  
  - Ask the user for a `word` 
  - Ask the user for a `letter`
  - Assign the `word` and the `letter` to variables
  - Determine how many times the `letter` occurs in the `word`  
  
    
    
        Enter a word: hippopotamus
        Enter a letter to count: p

        Output:
        The letter 'p' occurs 3 times in 'hippopotamus'


**Exercise 3**
--------------

Have the user enter a word or phrase. Print out the word or phrase
with the cases of all the letters swapped

      Enter a word or phrase: HeLlO wOrLd
      
      output:
      hElLo WoRlD

      -------------------------------------------------------
      Enter a word or phrase: UPPER lower
      
      output: 
      upper LOWER

      -------------------------------------------------------
      Enter a word or phrase: supERCaliFRagIliSticEXpiAliDoCIOus
      
      output: 
      SUPercALIfrAGiLIsTICexPIaLIdOcioUS


**Exercise 4**
--------------

### **4.1**
  - Store a number in variable to represent the `radius` of a circle
  - Store the value of pi (`3.141592654`) in another variable
  - Use the two *variables* to calculate the `circumference` and `area` of the circle

        output:
        
        Circle

        Radius: 5
        Circumference: 31.4159...
        Area: 78.5398...


### **4.2** 
  - Use the same two variables to calculate the `volume` of a *sphere* with the same `radius`
        
        output:

        Sphere

        Radius: 5
        Volume: 523.5987...


### **4.3** 
  - Store numbers representing the `base` and `height` measurements of a triangle.
  - Calculate the `area` of the triangle

        base: 5         
        height: 8       

        output:
        A triangle with a base of 5 and a height of 8 has an area of 20.0.      
        ---

        base: 2.8
        height: 2.02

        output:
        A triangle with a base of 2.8 and a height of 2.02 has an area of 3.08.

### **Extra challenge**  
  - Have the user enter all values
  - Don't forget that `input()` always returns a `string`


