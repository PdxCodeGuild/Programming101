
# Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

1. Greet the user and use a `for` loop to display their possible choices.   

```
Welcome to Rock, Paper, Scissors!

Your options are:

- Rock
- Paper
- Scissors

Enter your selection:  
```

2. The computer will ask the user for their choice (rock, paper, scissors). 
3. The computer will randomly choose rock, paper or scissors.
4. Compare the players' choices and determine who won and tell the user.

## Possible Combinations
| Human | Computer | Winner
|-|-|-|
|rock |rock | Tie
|rock |paper|Computer|
|rock |scissors|Human|
|paper |paper|Tie|
|paper |rock|Human|
|paper |scissors|Computer|
|scissors |scissors|Tie|
|scissors |rock|Computer|
|scissors |paper|Human|


## Extra Challenge 1

Catch all tie conditions using a single if conditional.

## Extra Challenge 2

Ask the user if they want to play again, using a while loop.

## Extra Challenge 3

Use a dictionary where each key is one of the choices, and the value associated with the key is a list containing the two other choices.

[//]: # (instructor note: write the tie case, the first case, have them write the others using elif)