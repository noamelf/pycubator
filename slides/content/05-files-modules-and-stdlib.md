# Files, modules and the stdlib
### Pycubator

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

        # Prints each line of the file.
        with open('example.txt') as f:
            for l in f:
                print(l)

--
### Writing
- `f.write(string)` writes string (without adding `\n`)
- `f.writelines(sequence)` writes sequence content (also without adding `\n`)

        fruits = ['Bannana', 'Melon', 'Peach']
        with open('example.txt', 'w') as f:
            f.writelines(fruits)

--
###### Exercise #1
### Simple reader
-   Read a file one line at a time, and print the number of the line (start with one) and
    the line content.
-   For example, for this input:

        Ami
        Udi
        Assaf

-   The output will be:

        1 Ami
        2 Udi
        3 Assaf

--
###### Exercise #2
### Robot Position Tracker

See http://lms.10x.org.il/item/35/

---

# Modules and packeges

--
### The import statement

- Allow use of other python files and libraries
- Imports: `import math`
- Named imports: `import math as m`
- Specific imports: `from math import pow`
- Import all: `from math import *` (dangerous! used only in very specific cases)

--

### Modules

    # tags.py
    def ul(items):
        return tag('ul', "".join([li(x) for x in items])

    # main.py (option 1)
    import tags
    print tags.ul('One', 'Two', 'Three')

    # main.py (option 2)
    from tags import ul
    print ul('One', 'Two', 'Three')

--
### Packages

-   Packages are namespaces which contain multiple packages and modules themselves.
-   Packages are simply directories, but in python2 there is a twist: each package/directory
    MUST contain a special file called `__init__.py`

--

    # fruits/__init__.py
    # -- empty -- nothing here -- really nothing -- just a lonely, empty file

    # fruits/apple.py
    def say_in_hebglish(): print('Tapuach')

    # main.py
    from fruits import apple
    apple.say_in_hebglish()

--

-   If a folder contains an `__init__.py` file, it can be imported as the name of the package itself.

        # foo/__init__.py
        def greeting():
            return "Hello World!"

        # main.py
        from foo import greeting
        print greeting()

--
##### Extra
### Modules are singeltones

    # stuff.py
    fruits = ['Pineapple']

    # module_a.py
    import stuff
    def foo():
        stuff.fruits.append('Apple')

    # module_b.py
    import stuff
    def foo():
        stuff.fruits.append('Banana')

--

    # program.py
    import module_a, module_b, stuff
    module_a.foo()
    module_b.foo()
    print(stuff.fruits)

    # output
    ['Pineapple', 'Apple', 'Banana']

---


# The Standard Library

--

### Time
-   `time.time` return the time in seconds since the epoch as a floating point number.

        import time
        t0 = time.time()
        for i in range(10000000):
            pass
        t1 = time.time()
        print(t1 - t0)

        # output:
        1.1572110652923584

--

-   `time.sleep` Suspend execution for the given number of seconds.

        import time
        print('Processing, please wait, ...')
        time.sleep(2)
        print('Done.')

        # output:
        Processing, please wait, ...
        Done.

--

### Logging

-   In large and long running programs we need more sophisticated printing.
-   The logging package enables us to easily log the current state and timestamp of our program

--

-   Basic usage:

        logging.debug('Alltems operational')
        logging.info('Airspeed knots')
        logging.warn('Lowfuel')
        logging.error('Nol. Trying to glide.')
        logging.critical('Glide attempt failed. About to crash.')

        # output:
        WARNING:root:Lowfuel
        ERROR:root:Nol. Trying to glide.
        CRITICAL:root:Glide attempt failed. About to crash.

-   Why can't we see the `debug` and `warning` messages?

--

-   We can determine the varbosity of the log with `setLevel`

        logging.root.setLevel(logging.DEBUG)
        logging.debug('Alltems operational')
        logging.info('Airspeed knots')

        # output
        DEBUG:root:Alltems operational
        INFO:root:Airspeed knots

--

-   With `basicConfig` we can create customisations that fits our needs.
-   For example make our logs more informative:

        logging.basicConfig(format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d]  %(message)s',
                            level=logging.DEBUG)
        logging.debug("you'll see a lot more information now...")

        # output
        [DEBUG 2015-07-14 22:59:59,160 <ipython-input-60-8bd2b8d57226>:5]  you'll see a lot more information now...

--

-   Or logging to a file:

        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('This message should go to the log file')

--

-   Resources:
    -   [Logging module docs](https://docs.python.org/3.5/library/logging.html)
    -   [Logging howto](https://docs.python.org/3.5/howto/logging.html)
    -   [Become a Logging Expert in 30 Minutes](https://youtu.be/24_4WWkSmNo), Gavin M. Roy, PyCon 2013

--

### OS

-   `os.listdir` return a list containing the names of the entries in the directory given by path:

        import os

        for filename in os.listdir('.'):
            print(filename)

        # output
        The-standard-library.ipynb
        example.log
        unit-tests.ipynb

--

-   `os.path.join` concatenate paths (according to OS):

        import os

        home = '/home/user'
        os.path.join(home, 'Downloads')

        # output
        '/home/user/Downloads'

-   `os.path.splitext` splits the file into root, extension:

        os.path.splitext('/home/noam/Downloads/xom.csv')

        # output
        ('/home/noam/Downloads/xom', '.csv')

--

-   `os.path.getsize`

        os.path.getsize('The-standard-library.ipynb')

        # output
        8440



-   `os.path.isdir`

        os.path.isdir('The-standard-library.ipynb')

        # output
        False

--

### Sys
- `sys.argv[0]` contains file name
- `sys.argv[1:]` contains arguments (if any)

--

#### Example
-   test.py:

        import sys

        def main(argv):
            a = int(argv[1])
            b = int(argv[2])
            return a + b

        if __name__ == '__main__':
            print(main(sys.argv))

-   cmdline:

        $ python test.py 5 10
        15

--

### argparse
-   A standard library solution for parsing script arguments
-   Generates help messages
-   Robust and clear
-   learn more at [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
--

## argparse example
-   test.py:

        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("square",
                            help="display a square of a given number",
                            type=int)
        args = parser.parse_args()
        print(args.square**2)

-   cmdline:

        $ python3 test.py 4
        16


--

###### Exercise #3
### File Information by Extension

See http://lms.10x.org.il/item/91/
