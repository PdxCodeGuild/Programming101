# Grading

### Quick Links
- [Back to Unit 3](https://github.com/PdxCodeGuild/Programming101/blob/master/units/unit-3.md)
- [Back to Syllabus](https://github.com/PdxCodeGuild/Programming101)

Let's convert a number grade to a letter grade, using `if` and `elif` statements and comparisons.

1. Have the user enter a number representing the grade (0-100)
2. Convert the number grade to a letter grade

## Numeric Ranges

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

## Advanced Version 1

Use `randint()` from the random module to determine the user's rival's score. Let the user know if they did better than their rival.

## Advanced Version 2

Use `%` to get the remainder of the grade when divided by ten, which is the same as the number in the ones digit. The number in the ones digit will determine whether they will get a '+' or a '-' appended to the end of their grade. For example, the grade `81` would be a 'B'. `81 % 10` would give you 1, which is a low number, so you would add a '-' to the end of the grade.