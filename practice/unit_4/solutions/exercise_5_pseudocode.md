# Unit 4 Practice Solutions

## **Exercise 5 - More Number Lists**

### Pseudocode

    loop: i = 0 -> (length of list - 1)
        set 'swap' variable to False

        loop: j = 0 -> (length of list - 1)
            if list[j] is less than list[j+1]
                place list[j] in a 'bubble' variable

                put list[j+1] at list[j]

                put bubble at list[j+1]

                since a swap occured this loop,
                set swap to True

        if no swap occured, break the outer loop

### Exercise 5 [solution](./exercise_5_solution.md)

---

## [< Exercise 5](../exercise_5.md)
