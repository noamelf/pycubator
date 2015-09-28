### About

*   Guido Van-Rossum side project in the late 1980's
*   Called after the Monty Python (comedy) group
*   Community-driven
*   Can be found on almost every platform and every field
*   Easy to extend using C and package system
*   2 main versions: Python2 and Python3
*   Beautiful

---

#### Java

    public class Hello{
      public static void main(String[] args){
        System.out.println("Hello, world!");
      }
    }

---

#### C++

    #include <iostream>

    int main(){
      std::cout << "Hello World!" << std::endl;
      return 0;
    }

---

#### Python

    print('Hello World!')

---

### Philosophy

*   The Zen of Python:
    *   Beautiful is better than ugly
    *   Explicit is better than implicit
    *   Simple is better than complex
    *   Complex is better than complicated
    *   Readability Counts
*   Other ideas
    *   There should be one obvious way to do it
    *   Clarity over speed
    *   We’re all consenting adults here

---

## Python qualities

*   Compromise between shell script and C++/Java program
*   Intuitive syntax
*   Interpreted
*   Dynamically typed
*   High-level data types
*   Slower than lower level languages

---

## Interpreted?

*   What does it mean for a language to be “interpreted?”
*   Trick question – “interpreted” and “compiled” refer to implementations, not languages
*   The most common Python implementation (CPython) is a mix of both:
    *   Compiles source code to byte code (.pyc files)
    *   Then interprets the byte code directly, executing as it goes
    *   No need to compile to machine language
    *   Essentially, source code can be run directly

---

### The REPL

*   Read Evaluate Print Loop

    $ python
    Python 2.7.9 (default, Apr  2 2015, 15:33:21) 
    [GCC 4.9.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>print('hello world!')    
    hello world!

*   Quick!
*   Helps test Python behaviour
*   Get inforamtion with `help()`
*   Bad for multiline code (i.e. classes, functions)

---

### Running Python - IPython

![](img/ipython-intro.png)

*   Auto-completion
*   Magic functions
*   IPython notebook

    $ sudo pip install ipython[all]
    $ ipython

---

### Running Python - .py files

*   Python source files
*   (No compiliation)

    $ gedit /tmp/example.py

![](img/gedit-hello-world.png)

    $ python /tmp/example.py
    hello world!

---

### Play with the interpeter

    >>> 1 + 1
    2
    >>> print('hello world')
    hello world
    >>> x = 1
    >>> y = 2
    >>> x + y
    3
    >>> print(x)
    1

---

### Objects

*   Everything is an object in Python
*   `id()` - unique object id
*   `type()` - object type

---

### Binding

![](img/binding1.png)---

### Binding

![](img/binding2.png)---

### Binding

![](img/binding3.png)---

### Style overview

*   [PEP 8](https://www.python.org/dev/peps/pep-0008/) - <q cite="https://www.python.org/dev/peps/pep-0008/#id10">code is read much more often than it is written</q>
*   Blocks are denoted by whitespace
*   Use spaces, not tabs (or set the editor to insert spaces instead of tabs)
*   Single line comments are denoted with #
*   Multi-line comments are denoted with '''
*   Variable and function names should be lower case with underscores separating words
*   Use docstrings to document what a function does:

    def add(x,y):
    ''' Adds two numbers '''
        return x + y                        

<aside class="notes">

PEP - Python Enhancment Proposal

</aside>

---

### Datatypes overview

*   None
*   Booleans (True, False)
*   Integers, Floats
*   Sequences

*   Lists
*   Tuples
*   Strings
*   Dictionaries

*   Classes and class instances
*   Modules and packages

---

### Booleans

*   Booleans: `True, False`
*   The following act like `False`:

*   `None`
*   `0`
*   `[]`(Empty sequences)

*   Everything else acts like `True`

---

### Boolean operations

These are the Boolean operations, ordered by ascending priority:

<table class="fragment">

<thead valign="bottom">

<tr>

<th class="head">Operation</th>

<th class="head">Result</th>

</tr>

</thead>

<tbody valign="top">

<tr>

<td>`x or y`</td>

<td>if _x_ is false, then _y_, else _x_</td>

</tr>

<tr>

<td>`x and y`</td>

<td>if _x_ is false, then _x_, else _y_</td>

</tr>

<tr>

<td>`not x`</td>

<td>if _x_ is false, then _True_, else _False_</td>

</tr>

</tbody>

</table>

<small>*and, or are short-circuit operators</small>

---

### Boolean examples

    >>> not True
    False

    >>> True or False
    True

    >>> False and True
    False

    >>> (1 + 1) or True
    2

    >>> True and (2 + 2)
    4

    >>> not 0
    True

Go to socrative quiz!

---

### Integers and floats

*   Numeric operators: `+ - * / // % **`
*   No i++ or ++i, but we do have += and -=
*   Int and Float:

    >>> type(2)                        
    int

    >>> type(2.5)
    float

    >>> 5/2 #python3
    2.5
    >>> 5/2 #python2
    2
    >>> 5/2.0 #python2
    2.5

---

### Assignments

    >>> a = b = 0
    >>> a, b = 3, 5                    

Super cool:

    >>> a, b = b, a
    >>> a
    5
    >>> b
    3                                       

---

### Comparisons

    >>> 5 == 5
    True

    >>> 'hello' == 'hello'
    True                

    >>> 1 != 2
    True                

    >>> 5 > 3
    True                

    >>> 'b' > 'a'
    True                

---

### Quiz!

*   It's anonymous
*   Check collective understanding
*   If you want to cheat, it's pretty easy, you can just type the questions in the REPL (but that will defeat the purpose of this quiz...)
*   Go to <a herf="m.socrative.com">m.socrative.com</a> and insert KCTGHQ43 as teacher room

<aside class="notes">I'm going to <a herf="t.socrative.com" target="_blank">t.socrative.com</a></aside>

---

### If Statements

    if a == 0:
        print 'a is 0'
    elif a == 1:
        print 'a is 1'
    else:
        print 'a is something else'

---

### For Loops

    >>> range(5)
    [0, 1, 2, 3, 4]

    for i in range(5):
        print(i, end=' ')

    0 1 2 3 4

---

### Break and Continue

    for i in range(10):
        if i == 3:
            continue
        elif i == 8:
            break
        print(i, end=' ')

    0 1 2 4 5 6 7              

---

### While Loops

    i = 0
    while i <= 3:
        print(i, end=' ')
        i += 1

    0 1 2 3

---

### Ranges

*   range(n) produces [0, 1, ..., n-1]*   range(i, j) produces [i, i+1, ..., j-1]*   range(i, j, k) produces [i, i+k, ..., m]

    >>> range(5, 25, 3)
    [5, 8, 11, 14, 17, 20, 23]

---

### Functions

    >>> def increment(x):
            return x + 1                    
    >>> increment(3) 
    4

*   Colon (:) indicates start of a block
*   Following lines are indented
*   Function declaration doesn’t specify return type
*   all functions return a value (None if not specified)
*   Parameter datatypes are not specified either