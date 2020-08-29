# Unit 4 Practice Solutions

## **Exercise 5 - More Number Lists**

### Pseudocode

    loop: i = 0 -> (length of list - 1)
        set 'swap' variable to False

        loop: j = 0 -> (length of list - 1)
            if list[j] is less than list[j+1]
                place list[j] in a 'temp' variable

                put list[j+1] at list[j]

                put temp at list[j+1]

                since a swap occured this loop,
                set swap to True
