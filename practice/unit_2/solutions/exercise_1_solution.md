# Unit 2 Practice Solutions

## Exercise 1 - Mailing Address

### **1.1**

**Solution**

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

**Output**

    Enter street: 231 Faux Ave.
    Enter city: Portland
    Enter state: Oregon
    Enter zip code: 97211

    231 Faux Ave.
    Portland, Oregon
    97211

### **1.2**

Using string methods, ensure that the address will be properly capitalized, no matter how it's entered.

    street = input("Street number: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input('Zip: ')

    street = street.title()
    city = street.title()
    
    # format address using an f-string
    print(f'''
    {street}
    {city}, {state}
    {zip_code}
    ''')
    
**Output**

    Enter address: 231 fAUx aVE.
    Enter city: poRtlANd
    Enter state: orEGOn
    Enter zip code: 97211

    231 Faux Ave.
    Portland, Oregon
    97211

Keep in mind that this is just one potential solution.

## [< Exercise 1](../exercise_1.md)

### [<< Back to Unit 2 Practice](/practice/unit_2/)
