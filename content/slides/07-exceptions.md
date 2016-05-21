# Exceptions
<!-- .slide: data-background="img/puzzles.jpg" -->

---

# Catching Exceptions 

--

### Python handles all errors with exceptions.

An exception is a signal that an error or other unusual condition has occurred.

--
### Catching an exception

    try:
        execute_some_code()
    except SomeException:
        handle_gracefully()

--

### Catching all exceptions

    try:
        execute_some_code()
    except:
        handle_gracefully()


--

-   Don't do it.
-   Catching too broad exceptions is potentially dangerous.
-   Among others, this "wildcard" handler will catch:
    -   system exit triggers
    -   memory errors
    -   typos
    -   anything else you might not have considered

--
###### Exercise
### Divide by zero

-   Try to divide `1/0`. What happens?
-   Catch the exception and tell the user he cannot divide by zero.

--
### Catching multiple exceptions

Handling them all the same way

    try:
        execute_some_code()
    except (SomeException, AnotherException):
        handle_gracefully()


--

Handling them separately

    try:
        execute_some_code()
    except SomeException:
        handle_gracefully()
    except AnotherException:
        do_another_thing()

---

# LBYL vs. EAFP

--
### LBYL

Look Before You Leap

> \[...\] explicitly tests for pre-conditions before making calls or
lookups. This style contrasts with the EAFP approach and is
characterized by the presence of many if statements.

--

### EAFP
Easier to Ask for Forgiveness than Permission
> \[...\] assumes the existence of valid keys or attributes and catches
exceptions if the assumption proves false. This clean and fast style
is characterized by the presence of many try and except
statements. The technique contrasts with the LBYL style common
to many other languages such as C.

--

### Examples
-   LBYL:

        import os
        if os.path.exists('tmp.txt'):
            with open('tmp.txt'):
                pass

-   EAFP:

        try:
            with open('tmp.txt'):
                pass
        except IOError as e:
            print(e)

--

### When to use
>"All errors are exceptions, but not all exceptions are errors"

Use exception handling to gracefully recover from application errors.
But: It's perfectly allowed, and sometimes necessary, to utilize
exception handling for general application control flow. EOFError, for example.

---

# Raising, Accessing and Propagating 

--

### Raising exceptions

Exceptions can be raised using `raise <exception>` with optional arguments.

    raise RuntimeError()
    raise RuntimeError("error message")

--

### Accessing the exception

Use "as" to access the exception object

    try:
        raise RuntimeError("o hai")
    except RuntimeError as e:
        print(e)


--

### Propagating exceptions

Try-blocks can be nested;
All exceptions propagate to the top-level "root exception handler" if uncaught.

    try:
        try:
            raise Exception
        except Exception:
            print('Inner')
    except Exception:
        print('Outer')


The (default) root exception handler terminates the Python process.

--

### Propagating exceptions

Propagation can be forced by using raise without arguments,
this re-raises the most recent exception.

    try:
        try:
            raise Exception
        except Exception:
            print('Inner')
            raise
    except Exception:
        print('Outer')


This is useful for e.g. exception logging.

--
### Practice

-   Read this [numbers.txt](misc/numbers.txt) file (don't use the `with` statement).
-   Add the integers in the file together, and print the sum at the end.
-   You need to except the following exceptions and let the user know the problem:
    - `IOError`: if there is a problem opening the file.
    - `ValueError`: if the line read is not an integer.
    - All other types: if any other exception arise, catch it and say 'unexpected error occurred'

---

# Finally and Else

--
### Finally
Code in the `finally` block will always be executed (unless Python crashes completely).

    try:
        open_file()
    except IOError:
        print('Exception caught')
    finally:
        close_file()

--

### Else
Code in the `else` block will be executed when no exception is raised

    try:
        open_file()
    except IOError:
        print('Exception caught')
    else:
        print('Everything went according to plan')

---

# Writing exceptions

--
### Inheritance
-   Exceptions are matched by superclass relationships.
    -   RuntimeError
    -   StandardError
    -   Exception
    -   BaseException

--

### Exception matching
- exception hierarchies can be designed.
- For example, `OverflowError`, `ZeroDivisionError` and `FloatingPointError`
are all subclasses of `ArithmeticError`.
- Just write a handler for `ArithmeticError` to catch any of them.

--

### Writing your own
It's as simple as

    class MyException(Exception):
        pass

--
###### Exercise
### Write your own exception!
-   Create a function called `guess_my_name` that:
    -   Takes user input.
    -   Checks if the user guessed your name correctly
    -   Throws an exception `NotMyName` if not.

-   Call that function:
    -   In a while loop, call that function,
    -   if `NotMyName` exception is caught stay in the loop.
    -   else exit and print 'success!'
