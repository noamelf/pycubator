# Imports, Files and Stdlib
### Pycubator

---

### Imports

- Allow use of other python files and libraries
- Imports: `import math`
- Named imports: `import math as m`
- Specific imports: `from math import pow`
- Import all: `from math import *` (dangerous! used only in very specific cases)

---

# Files
<!-- .slide: data-background="img/files.jpg" -->
The National Archives UK

--
### Opening Files

- `open(name, mode)` returns a file-object
- `name` is the path of the file to open
- `mode`:
    - `'r'` (read): the file is open in read-only mode
    - `'w'` (write): the file is open in write-only mode, and is truncated.
    - `'a'` (append): like 'w' but appends to the file
    - `'x'`: like 'w' but the file must not exist already
- `open(name)` defaults to read: `open(name, 'rt')`

--
### Closing
- `f.close()`:
    - Release the file handles
    - Write the file object content to disk
- Can be done alternatively using the `with` statement:

        with open('example.txt') as f:
            print(f.read())

--
### Reading
- `f.read()` reads the whole file (up to `EOF`)
- `f.read(index)` reads the file until `index`
- `f.readline()` reads a line (up to `\n`)

--
### Writing
- `f.write(string)` writes string (without adding a newline)
- `f.writelines(sequence)` writes sequence content (without adding newlines)

--
###### Excercise #1
### Simple reader
Read a file one line at a time, and print the number of the line
(start with one) and the line content. For example, for this input:
```
Ami
Udi
Assaf
```

The output will be:
```
1 Ami
2 Udi
3 Assaf
```

--
###### Excercise #2
### Robot Position Tracker

-   A robot on an exploration mission receives command file in the following fashion:

        North 100
        East 200
        South 20
        East 50
        North 100
        West 30

--

-   Each command has a direction (North, East, South, West) and a distance (a number, in meters).
-   You have to write a program that remembers its position and returns its horizontal and vertical
distance from the base station (the starting point).
-   For example, for the commands above the result
will be (220,180).

--

-   Write a function that receives a filename, opens it, parses the commands and returns the distance
in x and y from home:

        def parse_commands(filename):
            x, y = 0, 0
            # --- WRITE YOUR CODE HERE --- #

            # ---------------------------- #
            return x, y

        result = parse_commands('journey.txt')
        print "Result:", result
        assert (220, 180) == result
