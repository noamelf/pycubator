<!-- .slide: data-background="img/puzzles.jpg" -->
# Control structures

### Pycubator

---

# If and While

--
### Simple while

    while True:
        print("Enter your name (or nothing to exit)")
        name = input() # python2: raw_input()
        if not name:
            print("Bye!")
            break
        print("Hello {}!".format(name))

--
### Break and continue:

    SECRET = "xyzzy"

    while True:
        password = input("Please enter your password: ")
        if not password:
            continue
        if password == SECRET:
            break

        print "Wrong password!"


    print "Welcome!"

--
###### Exercise #1
### Simple calc

Ask the user to enter numbers.
Whenever the user enters an empty answer, show the sum of all entered numbers and quit.

    > 10
    > 45
    > 20
    > 90
    >
    Result: 165

--
###### Excersice #2
### Guessing game

-   Player 1 enters a secret number between 1 and 100 (player 2 looks aside).
-   The screen is cleared. (hint: `'\n' * 100`)
-   Player 2 tries to guess the number.
-   According to the input the program prints:
    -   "Your guess is too high, try again!"
    -   "Your guess is too low, try again!"
    -   "Your guess is correct!"
-   If the guess is correct, the program prints the number of attempts and the game is done.

--
###### Excersice #3
### Human Vs. Machine!

-   We continue to develop the guessing game, but this time your computer has to guess your secret number.
-   Choose a secret number between 1 and 100 , but don't tell it to the computer!
-   The computer will try to guess: "is your number x?". If you answer with y the game ends
    and the number of attempts is printed to screen.
-   Otherwise, the computer asks: "Is my guess higher than the secret number?"
    and you answer with y or n.
-   The computer asks again until she finds your number!


--
###### Excersice #4
### Fibonacci

Make a program that prints the [Fibonacci series][fibo] below 10,000:

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    ...

[fibo]: https://en.wikipedia.org/wiki/Fibonacci_number#List_of_Fibonacci_numbers

---

# For loops

--
### For on a string

    >>> for c in "Hello World!":
            print(c, end=' ')
    H e l l o   W o r l d !

--
### Using range()

    >>> for i in range(10):
            print(i, end=',')
    0,1,2,3,4,5,6,7,8,9,

    >>> for i in range(1, 11, 2):
            print(i, end=',')
    1,3,5,7,9,

    >>> for i in range(10, 0, -1):
            print(i, end=',')
    10,9,8,7,6,5,4,3,2,1,

--
### Range defenition

*   `range(n)` produces `[0, 1, ..., n-1]`
*   `range(i, j)` produces `[i, i+1, ..., j-1]`
*   `range(i, j, k)` produces `[i, i+k, ..., m]`

--
### Enumarate
    >>> for i, c in enumerate("Hello World!"):
            print(i, c)
    0 H
    1 e
    2 l
    3 l
    4 o
    5
    6 W
    7 o
    8 r
    9 l
    10 d
    11 !

--
###### Exercise #5
### Simple Square

Input a number (`n`), and print a square of `n*n` asterisks.
Input - an integer between 1 and 50. Sample Input:

    3

Sample Output:

    ***
    ***
    ***

--
###### Exercise #6
### Pyramid

Build a Pyramid!

Input - An integer between 1 and 20 Sample. Sample input:

    5

Sample Output:

        *
       ***
      *****
     *******
    *********

--
Sample Input:

    1

Sample Output:

    *

---

# Nested loops

--
### Nested loops

    for i in range(10):
        for j in range(10):
            print i, j

--
###### Excercise #7
###  Multiplication Table

Generate a multiplication table.

Input: An integer between 1 and 50

Sample Input:

    5

Sample Output:

    1 2 3 4 5
    2 4 6 8 10
    3 6 9 12 15
    4 8 12 16 20
    5 10 15 20 25

---

# Functions

--
### Defenition

    >>> def increment(x):
            return x + 1
    >>> increment(3)
    4

*   Colon (:) indicates start of a block
*   Following lines are indented
*   Function declaration doesnt specify return type
*   all functions return a value (None if not specified)
*   Parameter data types are not specified either

--
###### Excercise #8
###  Rotate a word

Create a function that rotates a word by 1 character to the right:

    def rotate(s):
        # ---- YOUR CODE HERE ---
        return "something"
        # -----------------------

    assert "dabc" == rotate("abcd")
    assert "hello world" == rotate("ello worldh")
    assert "x" == rotate("x")

--
###### Excercise #9
### Nachmanize

Create a function that returns a string nachmanized:

    assert nachmannize("abcd") == "a ab abc abcd"

