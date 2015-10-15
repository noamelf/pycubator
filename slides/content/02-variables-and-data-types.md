<!-- .slide: data-background="img/puzzles.jpg" -->
# Variables and data types

### Pycubator

---

# Variables and comparisions

--

### Assignment

Variables in python can hold values. This is done using the assignment operator:

    >>> a = 100
    >>> a
    100
    >>> b = 200
    200
    >>> c = a + b
    300

--

### Reassigning

You can modify the values in any variable by reassigning the value:

    >>> a = 10
    >>> a
    10
    >>> a = 20
    >>> a
    20
    >>> a = 5.5
    >>> a
    5.5

--

### Naming convention

According to Python conventions, variable names should be lowercase with words separated by underscores:

    # Good
    age = 12
    first_name = "Joe"
    x = 100

    # Bad!
    J = 5.5
    UserName = "itzik"
    numOfRetries = 5

--

### Name errors

-   What happens if you try to get the value of a variable that doesn't exist?

        >>> x = 100
        >>> x
        100
        >>> y
        NameError: name 'y' is not defined

-   In a python script, each variable must be assigned before it is accessed:

        print x  # This line raises NameError
        x = 1

--

###  Deleting names

Variables ("names") can be deleted with del:

    >>> x = 100
    >>> x
    100
    >>> del x
    >>> x
    NameError: name 'x' is not defined

--

### Augmented assignment

    >>> a = 50
    >>> a += 10
    >>> a
    60

-   This is the same as writing: `a = a + 10`
-   Try: `-=`, `*=`, `/=`, `//=`, `%=` and `**=`.

--
### Comparisons

-   Each data type has a specific behaviour when met with a comparison operator differently
-   We'll see more of that in the next slides but let's checkout some examples now:

        >>> 1 > 2
        True
        >>> 'abc' > 'abd'
        True

--

| Operation | Meaning                        |
| --------- | ------------------------------ |
| `<`       | strictly less than             |
| `<=`      | less than or equal             |
| `>`       | strictly greater than          |
| `>=`      | greater than or equal          |
| `==`      | equal                          |
| `!=`      | not equal                      |
| `is`      | object identity                |
| `is not`  | negated object identity        |

---

# Booleans

--

### Booleans

Python boolean types literals are `True` and `False`.
Let's run them through an "if" statement:

    >>> if True: print('Sure is')
    Sure is
    >>> if False: print('You shouldn't see me')


--

### Booleans and other types
-   The following act like `False`:
    -   `None`
    -   `0`
    -   `[]`(or any other empty sequence)
    -   `''` (empty string)
-   Everything else acts like `True`

--

### Boolean operations

| Operation | Result
| --------- | ---------------------------------------------
|`x or y`   | if `x` is `False`, then `y`, else `x`
|`x and y`  | if `x` is `False`, then `x`, else `y`
|`not x`    | if `x` is `False`, then `True`, else `False`

--

### Short circuit

-   The tables before shows that in Python `and` and `or` are **short-circuit** operators:

        >>> 1 or True
        1
        >>> True or 1
        True

-   What will be the result of `True and (2 + 2)`?
-   And what about `not 3`?

---

# Strings

--
### Strings literals

The following string literals are equivalent:

    "Hello World!"
    'Hello World!'
    """Hello World!"""
    '''Hello World!'''

Choose the quoting style that fits your needs:

    "It's a very nice day."
    'The sign says "Hello World!".'

--
### Multi-line strings

Triple quoting allows multi-line string in your code:

    """Shopping List:
    Cheese
    Apples
    Bread"""

    '''ABC
    DEF
    GHI'''

--
### String Literal Escape Squences

Notable escape sequences in string literals:

*    `\n`: new line
*    `\t`: tab
*    `\'` and `\"`: quote and double quote.
*    `\\`: slash
*    `\x68`: ASCII char 104 ("68" in hexadecimal is 104 in decimal)

--
### Example

    "I wrote: \"Hello!\".\nHe wrote: \"Goodbye!\"."

-   See [lexical analysis][lex] in Python docs for more information.

[lex]: http://docs.python.org/2/reference/lexical_analysis.html#string-literals

--
##### Extra
### Raw string literals

To disable escape sequences, raw string literals can be used:

    >>> print('c:\windows\newstuff\todo')  # OOPS!
    c:\windows
    ewstuff odo
    >>> print(r'c:\windows\newstuff\todo') # Better.
    c:\windows\newstuff\todo

---

# Common String Methods

--
### Checks
*   endswith, startswith

        'hello world'.startswith('he')  # -> True
*   isalnum, isalpha, isdigit, islower, isupper, isspace

        '123'.isdigit()  # -> True
        'Hello World'.islower()  # -> False

--
### Searches

*   count

        'hello world'.count('l')  # -> 3
*   find (index is the same as 'find' but raises exception if can't find the needle.)

        'hello world'.find('l')  # -> 2
        'hello world'.find('t')  # -> -1



--
### Manipulations

Be aware that `str` is an immutable type.
All the methods bellow return new string (there is no in place operations!).

--

*   lower, upper , title , capitalize , swapcase

        'hello world'.title()  # -> 'Hello World'
        'hello world'.capitalize()  # -> 'Hello world'

*   replace

        'hello world'.replace('world', 'john')  # -> 'hello john'

--

*   split, rsplit (what does rsplit do?)

        'hello world'.split()  # -> ['hello', 'world']

        'hello, and ,welcome'.split(',', maxsplit=1) # -> ['hello', ' and ,welcome']

*   splitlines - splits and leaves the `\n` out

        '''hi
        man'''.splitlines() # -> ['hi', 'man']

--

*   join

        ' '.join(['hello', 'world'])  # -> 'hello world'

        '<br >'.join(['first line', 'second line'])  # -> 'first line<br >second line'

*   strip, rstrip, lstrip - removes spaces and new lines from the ends of a string:

        '     hello!    \n'.strip() # -> 'hello!'

---

# Interactive Input and string formatting
<!-- .slide: data-background="img/input.png" -->

--
### Interactive Input

- `input()` will read up to a newline
- `input(prompt)` prints `str(prompt)` before reading input
- Python2 and Python3 difference:
    - Python3 `input()` is like Python2 `raw_input()`
    - Python2 `input()` actually does `eval(raw_input())`

--
### Basic formating

    name = 'Tom'

    # Bad style formatting
    print('hello ' + name)

    # old style formatting
    print('Hello %s!' % name)

    # new style formatting
    print('Hello {}!'.format(name))

--
### More formating
-   Named formatting

        >>> '{name} {age}'.format(age=5, name='Mike')
        mike 5

-   `{:4}{:7}` at least x number of chars
-   `{:b}{:x}` formats number as binary or hex
-   in short,`{name!conversion:format}` provides options on top of `{}`

--
### Resources
-   [Format Specification Mini-Language](https://docs.python.org/2/library/string.html#format-specification-mini-language).
-   [Examples](https://docs.python.org/2/library/string.html#format-examples)
-   [String Formatting Cookbook](http://ebeab.com/2012/10/10/python-string-format/)
-   [Common use cases](http://pyformat.info/)


--
###### Exercise #2

See string formatting at (part 1&2): http://lms.10x.org.il/item/123/