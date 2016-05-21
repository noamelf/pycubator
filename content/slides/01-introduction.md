<!-- .slide: data-background="img/monty-python.jpg" -->
# Introduction

### Pycubator

---

## Python?

--

* Dynamically typed
* Multi-paradigm
* Intuitive syntax
* Interpreted
* High-level data types
* Compromise between a shell script and a C++/Java program ?!?

--

### Why learn Python?

* Easy and practical to learn (see [Python is Now the Most Popular Introductory Teaching
Language at Top U.S. Universities][usage])
* Industrial strength, used by: Google, Facebook(Instagram), Microsoft, Dropbox, etc.
* Utilized in many fields - web, data science, ops, automation, AI and much more.

[usage]: http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext

--

### Some History

--

![](img/guido.jpg)

That's Guido Van-Rossum, Python creator ^^

--

"Let me introduce myself. I'm a nerd, a geek. I'm probably somewhere on the autism spectrum.
I'm also a late bloomer. I graduated from college when I was 26. I was 45 when I got married.
I'm now 60 years old, with a 14 year old son... I'm no Steve Jobs or Mark Zuckerberg. But at age 35
I created a programming language that got a bit of a following. What happened next was pretty
amazing..."

Guido's, [king's day speech][speech]

[speech]: http://neopythonic.blogspot.co.il/2016/04/kings-day-speech.html

--

### How was/is Python made?
* Community of [volunteers][core-dev], aka core developers ([you can also be one][be-core-dev])
* Transparent flow through Python Enhancement Proposals ([PEPs][PEPs])

[PEPs]: https://www.python.org/dev/peps/
[core-dev]: https://hg.python.org/committers.txt
[be-core-dev]: https://docs.python.org/devguide/coredev.html

---

## The Zen of Python

--

* Beautiful is better than ugly
* Explicit is better than implicit
* Simple is better than complex
* Complex is better than complicated
* Readability Counts

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

--

### Other ideas
* There should be one obvious way to do it
* Clarity over speed
* We are all consenting adults here

---

## The great split
#### Python2 vs. Python3

--
### Time line

* December  1989:  Guido  Van  Rossum  starts   Python  implementation
* January  1994:  Version  1.0  released
* October  2000:  Version  2.0  released
* December  2008:  Version  3.0  released
* June  2009:  Version  3.1  released
* July  2010:  Version  2.7  released  with  backports
* May 2016:  current  Python versions  are  2.7.11  and  3.5.1

--

###  Why Python 3?
* Guido wanted to change some of the language design decisions (mainly string encoding)
* Financing was supplied by Google.
* A (somewhat) new language was born

--

### Python 3 is backwards incompatible!

* `print` and `exec` become functions 
* Massive usage of generators instead of lists 
* All text (str) is Unicode and encoded text is binary data (bytes)
* Other minor changes in std lib 

--

### So why use Python 3?

* Proper encoding
* Asynchronous programing (`async/await`)
* Standard library virtualenvs
* `__pycache__` directories
* Keyword-only arguments

And much, much more, but we'll get to that later...

---
## Coding tools

---

## The REPL
(Read Evaluate Print Loop)

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
* But... doesn't play nice with multiline code (i.e. classes, functions)

--

###### Exercise
### Python as a calculator

* Try running the following in your python shell:

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
* What does `import this` do?

---

## IPython
### (REPL on steroids)

--
```bash
$ ipython
Python 3.5.1 (default, Mar  3 2016, 09:29:07)
Type "copyright", "credits" or "license" for more information.

IPython 4.0.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: fr
from       frozenset
```

--

### Cool features

* Use `tab` for autocomplete.
* Append a `?` to an end of a variable, a function, a class and more to get some help.
* Execute regular shell commands from within Ipython: `!ls`
* `%magic` commands are really cool. Try `%history`, `%save` and `%pastebin` for example.


---

## .py files

--

* Python source files
* (No compilation needed)

--

### .py files

![gedit](img/gedit-hello-world.png)

    $ python /tmp/example.py
    hello world!

---

## IDE

--

### PyCharm

-   [PyCharm's website](https://www.jetbrains.com/pycharm/)
-   You can set up both python 2 and python 3 side by side.
-   A commercial and a community versions are available for download.

--

### Pycharm shortcuts
-   Use `Alt+Enter` for quick fixes, including *auto import* (which is very useful).
-   Use `Ctrl+Shift+A` to find any command or setting!
-   Use `Ctrl+Alt+L` to reformat your code.

--

-   Use `Ctrl+Shift+F10` to run the current file.
-   Use `Shift+F10` to run again the last file.
-   Use `Ctrl+Space` for method/variable autocomplete.

---

## Style guide

--

-   Python puts a strong emphasis on readability
-   Hence [PEP 8][pep8] was created.
-   It holds style guidelines for how Python code should **look**

[pep8]: https://www.python.org/dev/peps/pep-0008/


---

##### Advanced
## Some more theory

--

### Interpreted?

* What does it mean for a language to be "interpreted?"
* Trick question - "interpreted" and "compiled" refer to implementations, not languages
* The most common Python implementation (CPython) is a mix of both:
    * Compiles source code to byte code (.pyc files)
    * Then interprets the byte code directly, executing as it goes
    * No need to compile to machine language
    * Essentially, source code can be run directly
