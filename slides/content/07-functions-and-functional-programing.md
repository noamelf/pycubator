<!-- .slide: data-background="img/function.jpg" -->
# Functions and functional programing
#### Pycubator

---

# Positional and Named Arguments
<!-- .slide: data-background="img/steen_argument_over_a_card_game.jpg" -->
<small>Jan Steen, Argument over a Card Game, Wikimedia Commons.</small>

--

#### Positional Arguments

    def func(arg1, arg2, arg3):
        pass

    func(a, b, c)

-   `arg1`, `arg2` and `arg3` are positional arguments
-   When calling func exactly 3 arguments must be given, wrong number of args will
    result in a `TypeError`
-   The order in the call determines which arg they are bound to
-   The expressions (`a, b, c`) are evaluated before the call
-   The value of `a` is bound to `arg1` in the body of func and so forth


--

#### Named Arguments

    def func(arg1, named1=val1, named2=val2):

    func(a, named2=b, named1=c)
        pass

-   After the positional args, named args are allowed
-   `val1` and `val2` are default values for those variables.
-   Omitting named arguments in a call uses the default value
-   Named arguments can be given out of order:
    - `func(a, named2=b)`
    - The default value, val1 will be bound to named1

--

#### Default Arguments

-   Default arguments are evaluated when the function is defined
-   In all calls, the object that the expression evaluated to will be used.
-   If the default is mutable, updates in one call effect following calls
-   `def func(a=[])` Will mutate the default on each call
-   Use None as the default to avoid mutation

        def func(a=None):
            a = a or []


--

#### Memoization

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

-   A variable number of positional arguments can be specified
-   Could use any identifier but args is conventional
-   `args` is a tuple of 0 or more objects


--
### **kwargs

    def func(arg1, *args, **kwargs):
        pass

-   Use `**kwargs` at the end
-   Could use any identifier but kwargs is conventional
-   kwargs is a dictionary of strings to values
-   The keys of kwargs are the names of the keyword args

--
### \*/\*\* in Function Definition or Assignment

-   `def(*args)`: args is a tuple that can take 0 or more values
-   `def(**kwargs)`: kwargs is a dictionary that can take 0 or more
key-value pairs
-   `a,*var_name = range(5)`: `var_name` is list taking 0 or more
values


--

### \*/\*\* in Function Call

-   `func(*expr)`
    - `expr` is an iterable
    - It gets unpacked as the positional arguments of `func`
    - Equivalently:
    ``` python
    seq = list(expr)
    func(seq[0], seq[1], ...)
    ```
--
-   `func(**expr)`
    - expr is a dictionary of form `{'string': val, ...}`
    - It gets unpacked as the keyword arguments of `func`
    - Equivalently
    ```python
    func(string=val, ...)
    ```

--
##### Extra
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
##### Extra
### Annotations
```python
def func(name: str, hight: float = 1.90)-> int:
    pass
```
-   Function arguments and return values can be annotated
-   Python does not enforce any meaning to annotations
-   Read further on [PEP 3107](https://www.python.org/dev/peps/pep-3107/) and [PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

# Global variables
<!-- .slide: data-background="img/global.jpeg" -->

--

### Closures
```python
a = 42
def func():
    print(a)
```
-   A function that knows about variable defined outside the function
-   `func` is a closure because it knows about `a`
-   Closures are read-only: adding `a += 1` inside `func()` will result in `UnboundLocalError` exception

--

### Global
```python
a = 42
def func():
    global a
    a += 1
```
-   Changing global state can be dengerous, so Python requires you to declare it explictly
-   `global` can circumvent read-only closures
-   the `global` keyword declares certain variables in the current code block to reference the global scope
-   Variables following global do not need to be bound already

--

### Nonlocal
```python
def outer():
    a = 42
    def func():
        nonlocal a
        print(a)
        a += 1
    func()
```

-   `nonlocal` declares certain variables in the current code block to reference the nearest enclosing scope.
-   If the nearest scope is the global scope then nonlocal raises a `SyntaxError`
-   See [PEP 3104](https://www.python.org/dev/peps/pep-3104/)


---
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
```python
f = lambda x: x + 1
```
-   Anonymous functions are function objects without a name
-   lambdas can have the same arguments as regular functions:
`lambda arg, *args, named=val, **kwargs: ret`
-   lambdas must be one-liners and do not support annotations
-   'syntatic suger' to pass short functions to other functions.

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
```python
from functools import partial
def add(x, y):
    return x + y

add_3 = partial(add, 3)
```

-   Partial application creates a new function by supplying an existing function with some of its arguments

---

#decorators
<!-- .slide: data-background="img/decorators.jpg" -->

--

### Decorators

-   Decorators are transformations on functions
-   A function that takes in a function and returns a modified function
```python
@dec
def func(arg1, arg2, ...):
    pass
```
-   Is equivalent to:

```python
def func(arg1, arg2, ...):
    pass
func = dec(func)
```

--

### Decorator Arguments

-   A decorator can take arguments

```python
@decmaker(argA, argB, ...)
def func(arg1, arg2, ...):
    pass
```
-   Is equivalent to:

```python
def func(arg1, arg2, ...):
    pass
func = decmaker(argA, argB, ...)(func)
```
--
### Deorator example
```python
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
```
--

### Multiple Decorators
```python
@dec1
@dec2
def func(arg1, arg2, ...):
    pass
```

-   Is equivalent to:

```python
def func(arg1, arg2, ...):
    pass
func = dec1(dec2(func))
```
