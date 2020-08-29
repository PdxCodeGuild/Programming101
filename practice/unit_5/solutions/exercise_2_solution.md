# Unit 3 Practice Solutions

## Exercise 1 - Geometry

**Solution**

    # loop 100 times
    j = 0
    while j < 100:

    # if multiple of 3 and 5
    if j % 3 == 0 and j % 5 == 0:
        output = 'FizzBuzz'

    # if multiple of 3
    elif j % 3 == 0:
        output = 'Fizz'

    # if multiple of 5
    elif j % 5 == 0:
        output = 'Buzz'

    # if not a multiple of 3 or 5
    else:
        output = j

    print(output)

    j += 1
