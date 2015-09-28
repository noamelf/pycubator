# Py...what?
<!-- .slide: data-background="img/puzzles.jpg" --> 

--

### About

*   Guido Van-Rossum side project in the late 1980's
*   Called after the Monty Python (comedy) group
*   Community-driven
*   Can be found on almost every platform and every field
*   Easy to extend using C and package system
*   2 main versions: Python2 and Python3
*   Beautiful

--

#### Java
```java
    public class Hello{
      public static void main(String[] args){
        System.out.println("Hello, world!");
      }
    }
```
--

#### C++
```c++
    #include <iostream>

    int main(){
      std::cout << "Hello World!" << std::endl;
      return 0;
    }
```
--

#### Python
```python
    print('Hello World!')
```

---

# Philosophy
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### The Zen of Python:
*   Beautiful is better than ugly
*   Explicit is better than implicit
*   Simple is better than complex
*   Complex is better than complicated
*   Readability Counts

--

### Other ideas
*   There should be one obvious way to do it
*   Clarity over speed
*   We are all consenting adults here

---

# The REPL
<!-- .slide: data-background="img/puzzles.jpg" -->
##### (Read Evaluate Print Loop)

--

``` python
$ python
Python 2.7.9 (default, Apr  2 2015, 15:33:21) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>print('hello world!')    
hello world!
```

--

### Try it yourself
``` python
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
```

--

### Why should I use it??

*   Quick!
*   Helps test Python behaviour
*   Get inforamtion with `help()`
*   But... does'nt play nice with multiline code (i.e. classes, functions)

---

# IPython
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### IPython
![](img/ipython-intro.png)

--

### Advantages over the REPL

*   Auto-completion
*   Magic functions
*   IPython notebook

--

### IPython installation
```bash
    $ sudo pip install ipython[all]
    $ ipython
```

---

# `.py` files
<!-- .slide: data-background="img/puzzles.jpg" -->

--
### `.py` files

*   Python source files
*   (No compilation needed)

--

### `.py` files

![](img/gedit-hello-world.png)

``` bash
$ python /tmp/example.py
hello world!
```

---

# Final words
<!-- .slide: data-background="img/puzzles.jpg" -->

--
### Python qualities

*   Compromise between shell script and C++/Java program
*   Intuitive syntax
*   Interpreted
*   Dynamically typed
*   High-level data types
*   Slower than lower level languages

--

### Interpreted?

*   What does it mean for a language to be "interpreted?"
*   Trick question - "interpreted" and "compiled" refer to implementations, not languages
*   The most common Python implementation (CPython) is a mix of both:
    *   Compiles source code to byte code (.pyc files)
    *   Then interprets the byte code directly, executing as it goes
    *   No need to compile to machine language
    *   Essentially, source code can be run directly

--

### Style overview

*   [PEP 8](https://www.python.org/dev/peps/pep-0008/) - <q cite="https://www.python.org/dev/peps/pep-0008/#id10">code is read much more often than it is written</q>
*   Blocks are denoted by whitespace
*   Use spaces, not tabs (or set the editor to insert spaces instead of tabs)
*   Single line comments are denoted with #
*   Multi-line comments are denoted with '''
*   Variable and function names should be lower case with underscores separating words
*   Use docstrings to document what a function does:

```python
    def add(x,y):
    """ Adds two numbers """
        return x + y                        
```