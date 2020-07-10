# Unit 4 Practice

- count letters in a word using loops
- Loop over a list of numbers. Find:
  - sum
  - mean
  - median
  - mode



## **Exercise 1**

You've got things to do every day this week and need to plan for the weather. 

### **1.1**
Let's take this one day at a time, for now.

Create variables for:
  - `temperature` - A number representing the outside temperature (35, 78, 99)
  - `heat_item` - A useful item on a hot day
  - `mild_item` - A useful item on a mild day
  - `cold_item` - A useful item on a cold day

Decide what temperatures constitute hot, mild and cold days. Then, using the `temperature`, determine which `item` you need to bring with you. 

        temperature: 88

        output:
        Temperature: 88 degrees
        Item to bring: waterbottle

### **1.2**

Create a few more variables:
  - `precipitation` - The weather condition for the day ('none','clouds', 'rain', 'sleet', 'snow')
  - `sun_item` - A useful item in the sun
  - `rain_item` - A useful item in the rain
  - `snow_item` - A useful item in the snow

Now, let's also check the `precipitation` for the day and tell the user which additional `item` they might need.

      temperature: 96
      precipitation: none

      output: 
      Temperature: 96 degrees
      Precipitation: None
      Items to bring: waterbottle, sunscreen

      -----
      temperature: 80
      precipitation: rain

      output:
      Temperature: 80
      Precipitation: Rain
      Items to bring: waterbottle, umbrella


      -----
      temperature: 35
      precipitation: snow

      output: 
      Temperature: 35 degrees
      Precipitation: Snow
      Items to bring: jacket, snow boots

### **1.3**

Now we're ready to plan out our week. 

Create lists of:
- The seven `days_of_the_week`.
- The `temperatures` for each day
- The `precipiation` for each day

**Loop** over the lists and display the same output as above for each day of the week.

Hint: Since all the lists are the same **length**, a single loop can be used.


## **Exercise 2**



### **3.1**

Calculate the number of Tweets required, **rounding up** to the nearest integer.

### **3.2**

Ask the user for the `number of characters` in their message

- `if` the length of the message is **less than** the `max_length` allowed for a Tweet, output a `message` telling the user they only need one Tweet

- Otherwise, calculate the number of Tweets required, **rounding up** to the nearest integer and output a `message` telling the user the number of Tweets they will need.

### **3.3**

Display different messages to the user depending on how many Tweets their message requires.
