<!-- .slide: data-background="img/function.jpg" -->
# Functions and functional programing
### Pycubator

---

# Positional and Named Arguments
<!-- .slide: data-background="img/steen_argument_over_a_card_game.jpg" -->
<small>Jan Steen, Argument over a Card Game, Wikimedia Commons.</small>

--

### Positional Arguments

    def func(arg1, arg2, arg3):
        pass

    func(a, b, c)

-   `arg1`, `arg2` and `arg3` are positional arguments
-   When calling `func` exactly 3 arguments must be given, wrong number of args will
    result in a `TypeError`
-   The order in the call determines which arg they are bound to

--
### Named Arguments

    def say(arg1, named1, named2):
        print(arg1, named1, named2)

    say('make', named2='day', named1='my')

    # output
    make my day

-   Named arguments can be given out of order


--

### Default Arguments

    def func(arg1, named1=val1, named2=val2):
        pass

    func(a, named2=b, named1=c)

-   After the regular args, default args are allowed
-   `val1` and `val2` are default values for those variables.
-   Omitting named arguments in a call uses the default value

--
##### advanced
### Default Arguments gotcha

-   Default arguments are evaluated when the function is defined
-   In all calls, the object that the expression evaluated to will be used.
-   If the default is mutable, updates in one call effect following calls
-   `def func(a=[])` Will mutate the default on each call
-   Use None as the default to avoid mutation

        def func(a=None):
            a = a or []

--
##### advanced
### Memoization

-   Memoization is an optimization technique that stores results of
function calls
-   The previously computed answers can be looked up on later calls
-   Use a dictionary default arg to store answers
-   `def func(arg, cache={}):`
-   Store answers in `cache[arg] = ans`
-   Check for arg in cache before doing any work

---

# Args and KWArgs
<!-- .slide: data-background="img/argument-shadows.jpg" -->

--

### *args

     def func(arg1, *args):
        print(args)
     func(1, 2, 3, 4)

     # output:
    (2, 3, 4)

-   A variable number of positional arguments can be specified
-   Could use any identifier but `args` is conventional
-   `args` is a tuple of 0 or more objects

--
###### Exercise
### List students

-   Implement the `list_students` function

        expected_result = '''0 Tim
        1 Tom
        2 Tal'''

        assert expected_result == list_students('tal', 'tom', 'tim')


--
### **kwargs

    def foo(arg1, **kwargs):
        print(kwargs)

    foo(1,two=2, three=3)

    # output
    {'two': 2, 'three': 3}

-   Use `**kwargs` at the end
-   Could use any identifier but `kwargs` is conventional
-   kwargs is a dictionary of strings to values
-   The keys of kwargs are the names of the keyword args

--
###### exercise

-   implement the `inventory_str` function

        expected_result = '''The following Toyota models are availble:
        Corola - 7
        Auris - 5
        Camary - 10'''

        result = inventory_str('toyota', camary=10, auris=5, corola=7)
        assert  result == expected_result

--
##### advanced
### iterator expansion

    a, *the_rest = range(4)
    print(the_rest)

    # output
    (1, 2, 3)


-   Only works on Python3
-   `a,*var_name = range(5)`: `var_name` is list taking 0 or more values

--

### `*` in Function Call

    def bar(arg1, arg2, arg3):
        print(arg1+arg2+arg3)

    l = [1, 2, 3]
    bar(*l)

    # output
    6

- `l` is an iterable
- It gets unpacked as the positional arguments of `bar`

--
### `**` in Function Call

    def print_person(name, age):
        print('{} is {} years old'.format(name, age))

    person = {'name': 'Mike', 'age': 28}
    print_person(**person)

    # output
    Mike is 28 years old


- `person` must be a dictionary of form `{'string': val, ...}`
- It gets unpacked as the keyword arguments of `print_person`


--
##### advanced
### Required Keyword Args

-   Python3 only
-   Any args after `*args` are keyword args
-   If there is no default value specified, they are required keyword args
-   `def func(*args, named):`
    - `named` is a required keyword arg
-   To specify required keyword args without allowing variable positional args use `*`
-   `def func(arg1, *, named)`
    - named is a required kwarg
    - func must take exactly one pos arg and one kwarg


--
##### advanced
### Annotations

    def func(name: str, hight: float = 1.90)-> int:
        pass

-   Function arguments and return values can be annotated
-   Python does not enforce any meaning to annotations
-   Read further on [PEP 3107](https://www.python.org/dev/peps/pep-3107/) and [PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

##### advanced
# Closures, Global and Non-Local
<!-- .slide: data-background="img/global.jpeg" -->

--

### Closures

    def list_fruits():
        fruits = ['bannana', 'apple']
        def show():
            print(fruits)

        return show

    fruit_list = list_fruits()
    fruit_list()

    # output:
    ['bannana', 'apple']


--

-   A function that knows about variable defined outside it's scope.
-   `show()` is a closure because it knows about `fruits`
-   Closures are read-only: adding `fruits += ['kiwi']` inside `show()` will result
    in `UnboundLocalError` exception.

--

### Global

    a = 42
    def func():
        global a
        a += 1

-   Changing global state can be dangerous, so Python requires you to declare it explicitly
-   `global` can circumvent read-only closures
-   the `global` keyword declares certain variables in the current code block to reference the global scope
-   Variables following global do not need to be bound already

--

### Nonlocal

    def outer():
        a = 42
        def func():
            nonlocal a
            print(a)
            a += 1
        func()

-   Python3 only.
-   `nonlocal` declares certain variables in the current code block to reference the nearest enclosing scope.
-   If the nearest scope is the global scope then nonlocal raises a `SyntaxError`
-   See [PEP 3104](https://www.python.org/dev/peps/pep-3104/)


---

##### advanced
#Functional Programming
<!-- .slide: data-background="img/lambda.jpg" -->
--

### Background (1)

-   Functional programming started with lambda(&Lambda;) calculus
-   Alternative to Turning machines for exploring computability
-   Expresses programs as functions operating on other functions
-   Functional programming attempts to make it easier to reason about program behavior
-   No data states allows for easier multi threaded programing

--

### Background (2)
-   Python data is mutable and allows side-effects
-   Has some functional concepts
-   Not an ideal functional programming environment

--

### First Class Functions
-   A **higher order function** is a function that does at least one of the following:
    - Takes a function as one of its inputs
    - Outputs a function

-   You can use functions anywhere you would use a value
-   Functions are immutable so you can use them as dictionary keys
-   Functions can be the return value of another function

--

### &lambda; (lambda) Functions

    f = lambda x: x + 1

-   Anonymous functions are function objects without a name
-   lambdas can have the same arguments as regular functions:
`lambda arg, *args, named=val, **kwargs: ret`
-   lambdas must be one-liners and do not support annotations
-   'syntactic sugar' to pass short functions to other functions.

--

### Higher Order Functions
-   The most common are `map` and `filter`
-   `map(f, seq)` returns an iterator containing each element of `seq` but with `f` applied
-   `filter(f, seq)` returns an iterator of the elements of seq where `bool(f(seq[i]))` is `True`


--

### Functions as Keyword Args

-   Many functions will accept another function as a kwarg `sorted(seq, key=f)`
-   `sorted` will call `f` on the elements to determine order
-   The elements in the resulting list will be the same objects in seq
-   Have the key return a tuple to sort multiple fields
-   `min(seq, key=f)` and `max(seq, key=f)` behave similarly
-   This is a good spot for lambda

--

### Partial Application

    from functools import partial
    def add(x, y):
        return x + y

    add_3 = partial(add, 3)

-   Partial application creates a new function by supplying an existing function with some of its arguments

---

##### advanced
# Decorators
<!-- .slide: data-background="img/decorators.jpg" -->

--

### Decorators

-   Decorators are transformations on functions
-   A function that takes in a function and returns a modified function

        @dec
        def func(arg1, arg2, ...):
            pass

-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = dec(func)


--

### Decorator Arguments

-   A decorator can take arguments

        @decmaker(argA, argB, ...)
        def func(arg1, arg2, ...):
            pass

-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = decmaker(argA, argB, ...)(func)

--
### Decorator example

    import urllib
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def get_pep(num):
        'Retrieve text of a Python Enhancement Proposal'
        resource = 'http://www.python.org/dev/peps/pep-{:04d}'.format(num)
        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return 'Not Found'

--

### Multiple Decorators

    @dec1
    @dec2
    def func(arg1, arg2, ...):
        pass


-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = dec1(dec2(func))

