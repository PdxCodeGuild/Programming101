# Unit 2 Practice Solutions

## Exercise 1

### **1.1**

    # display a welcome message to the user, for some context
    print("Welcome! Please enter your address:")

    # collect address fields
    street = input("Street number: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input('Zip: ')

    # format address using an f-string
    print(f'''
    {street}
    {city}, {state}
    {zip_code}
    ''')

### **1.2**

Using string methods, ensure that the address will be properly capitalized, no matter how it's entered.

**Solution 1**

    street = input("Street number: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input('Zip: ')

    street = street.lower().title()
    city = street.lower().title()
    
    # format address using an f-string
    print(f'''
    {street}
    {city}, {state}
    {zip_code}
    ''')


## [< Exercise 1](exercise_1.md)

### [<< Back to Unit 1 Practice](/practice/unit_1/)
