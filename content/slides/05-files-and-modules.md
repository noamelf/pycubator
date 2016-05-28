# Files and Modules 
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
###### Exercises

[Working with files](http://lms.10x.org.il/item/35/)

---

# Modules and packages

--
### The import statement

- Allow use of other python files and libraries
- Imports: `import math`
- Named imports: `import math as m`
- Specific imports: `from math import pow`
- Import all: `from math import *` (dangerous! used only in very specific cases)

--

### Modules

    # utensils.py
    def eat_soup():
        return 'spoon'

    # main.py (option 1)
    import utensils
    print(utensils.eat_soup())

    # main.py (option 2)
    from utensils import eat_soup
    print(eat_soup())

--
### Packages

-   Packages are namespaces which contain multiple packages and modules themselves.
-   Packages are simply directories, but there is a twist: each package/directory
    MUST contain a special file called `__init__.py`
-   Not putting an `__init__.py` file in a Python3 package will work but that's
    [another story](https://www.python.org/dev/peps/pep-0420/)

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
        print(greeting())

--
##### advanced
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

