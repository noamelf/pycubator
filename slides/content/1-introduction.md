<!-- .slide: data-background="img/monty-python.jpg" -->
# Introduction

### Pycubator

---

# Py...what?
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### About

* Guido Van-Rossum side project in the late 1980's
* Called after the Monty Python (comedy) group
* Community-driven
* Can be found on almost every platform and every field
* Easy to extend using C and package system
* 2 main versions: Python2 and Python3
* Beautiful

--

### Java

    public class Hello{
      public static void main(String[] args){
        System.out.println("Hello, world!");
      }
    }

--

### C++

    #include <iostream>

    int main(){
      std::cout << "Hello World!" << std::endl;
      return 0;
    }
--

### Python

    print('Hello World!')


---

# Philosophy
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### The Zen of Python:
* Beautiful is better than ugly
* Explicit is better than implicit
* Simple is better than complex
* Complex is better than complicated
* Readability Counts

--

### Other ideas
* There should be one obvious way to do it
* Clarity over speed
* We are all consenting adults here

---

<!-- .slide: data-background="img/puzzles.jpg" -->
# The REPL
##### (Read Evaluate Print Loop)

--
### The REPL

    $ python
    Python 2.7.9 (default, Apr  2 2015, 15:33:21)
    [GCC 4.9.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>print('hello world!')
    hello world!

* To exit use `ctrl+d` on *nix, and `ctrl+z` on windows.

--

### Why should I use it??

* Quick!
* Helps test Python behaviour
* Get information with `help()`
* But... does'nt play nice with multiline code (i.e. classes, functions)

---

# IPython
### (REPL on steroids)
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### IPython
![ipython](img/ipython-intro.png)

--

### Cool features

* Use `tab` for autocomplete.
* Append a `?` to an end of a variable, a function, a class and more to get some help.
* `%magic` commands are really cool. Try `%history`, `%save` and `%pastebin` for example.

---

# .py files
<!-- .slide: data-background="img/puzzles.jpg" -->

--
### .py files

* Python source files
* (No compilation needed)

--

### .py files

![gedit](img/gedit-hello-world.png)

    $ python /tmp/example.py
    hello world!


---

# Let's play!
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### Python as a calculator

Try running this in your python shell:

    >>> 10 + 10
    20
    >>> 50 * 2
    100
    >>> 10 + 20 * 3
    70
    >>> (10 + 20) * 3
    90

* What does `**` do?
* What does `%` do?

--

### Integers

* What do you get when you run this:

        >>> 10 / 3

--

### Floats

Float values always include a decimal mark:

    >>> 10.0 / 4.0
    2.5

What happens when you divide an int by a float, a float by an int?

---

# Some more theory
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### Python qualities

* Compromise between shell script and C++/Java program
* Intuitive syntax
* Interpreted
* Dynamically typed
* High-level data types
* Slower than lower level languages

--

### Interpreted?

* What does it mean for a language to be "interpreted?"
* Trick question - "interpreted" and "compiled" refer to implementations, not languages
* The most common Python implementation (CPython) is a mix of both:
    * Compiles source code to byte code (.pyc files)
    * Then interprets the byte code directly, executing as it goes
    * No need to compile to machine language
    * Essentially, source code can be run directly


