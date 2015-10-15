<!-- .slide: data-background="img/puzzles.jpg" -->
# Control structures

### Pycubator

---

# If and While

--
### Simple if

    x = input()
    if x > 5:
        msg = 'Higher than five'
    elif x == 5:
        msg = 'Equels five'
    else:
        msg = 'Lower than five'

--
### Trinary operator

    x = input()
    msg = 'Higher than five' if x > 5 else 'Equel or lower than five'

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

See http://lms.10x.org.il/item/12/

--
###### Exersice #2
### Guessing game

See http://lms.10x.org.il/item/13/

---

# For loops

--
### For on a string

    from __future__ import print_function

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
###### Exercise #3
### Simple Square

See http://lms.10x.org.il/item/15/

---

# Nested loops

--
### Nested loops

    for i in range(10):
        for j in range(10):
            print i, j


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
*   All functions return a value (None if not specified)
*   Parameter data types are not specified either

--
###### Exercise #4
###  Rotate a word

See http://lms.10x.org.il/item/30/

--
###### Exercise #5
### Nachmanize

See http://lms.10x.org.il/item/26/

