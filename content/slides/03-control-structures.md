<!-- .slide: data-background="img/puzzles.jpg" -->
# Control structures

### Pycubator

--
### Blocks

-   All control structures (if, while/for, functions) content must be in a block.
-   Block are determined by indentation.
-   The pep8 style guides set 4 spaces to be the standard indentation.
-   If you are using Tab to indent make sure your editor converts it to 4 spaces.

        if True:
            print('Yes it is')

---

# If and While

--
### Simple if

    x = int(input())  # Remember to use raw_input() in python2
    if x > 5:
        msg = 'Higher than five'
    elif x == 5:
        msg = 'Equels five'
    else:
        msg = 'Lower than five'
    print(msg)

--
### Ternary operator

    x = int(input())
    msg = 'Higher than five' if x > 5 else 'Equel or lower than five'
    print(msg)

--
### Simple while

    while True:
        name = input('Enter your name: ')
        print('Hello {}!'.format(name))

--
### Break and continue:

    SECRET = 'xyzzy'

    while True:
        password = input('Please enter your password: ')
        if not password:
            continue
        elif password == SECRET:
            break

        print('Wrong password!')


    print('Welcome!')

--
###### Exercises

`while` and `if` [exercises](http://lms.10x.org.il/item/12/)

---

# For loops

--
### For on a string

    # Make Python2 print compatibale with Python3
    from __future__ import print_function

    >>> for c in 'Hello World!':
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
### Range definition

*   `range(n)` produces `[0, 1, ..., n-1]`
*   `range(i, j)` produces `[i, i+1, ..., j-1]`
*   `range(i, j, k)` produces `[i, i+k, ..., m]`

--

### Nested loops

    for i in range(10):
        for j in range(10):
            print(i, j)

--
### Enumerate
    >>> for i, c in enumerate('Hello World!'):
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
###### Exercises
[for loops](http://lms.10x.org.il/item/15/)

---

# Functions

--
### Definition

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
###### Exercise

[Functions](http://lms.10x.org.il/item/145/)
(Progress bar, 2 exercises)
