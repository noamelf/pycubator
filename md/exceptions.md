## LBYL vs EAFP

Look Before You Leap
  
>[...] explicitly tests for pre-conditions before making calls or
lookups. This style contrasts with the EAFP approach and is
characterized by the presence of many if statements.

--

## LBYL vs EAFP
Easier to Ask for Forgiveness than Permission  
>[...] assumes the existence of valid keys or attributes and catches
exceptions if the assumption proves false. This clean and fast style
is characterized by the presence of many try and except
statements. The technique contrasts with the LBYL style common
to many other languages such as C.

--

## Examples
LBYL:
```python
import os
if os.path.exists('tmp.txt'):
    with open('tmp.txt'):
        pass
```
EAFP:
```python
try:
    with open('tmp.txt'):
        pass
except IOError as e:
    print(e)
```

--

## When to use
>"All errors are exceptions, but not all exceptions are errors"
  
Use exception handling to gracefully recover from application errors.
But: It's perfectly allowed, and sometimes necessary, to utilize
exception handling for general application control flow. EOFError, for example.

---
## Catch all exceptions

```python
try:
    execute_some_code()
except:
    handle_gracefully()
```

Don't do it. Catching too broad exceptions is potentially dangerous. 
Among others, this "wildcard" handler will catch:

- system exit triggers
- memory errors
- typos
- anything else you might not have considered

--

## Better:

Catching specific exceptions
```python
try:
    execute_some_code()
except SomeException:
    handle_gracefully()
```

--

## Catching multiple exceptions
Handling them all the same way
```python
try:
    execute_some_code()
except (SomeException, AnotherException):
    handle_gracefully()
```

--

## Catching multiple exceptions

Handling them separately
```python
try:
    execute_some_code()
except SomeException:
    handle_gracefully()
except AnotherException:
    do_another_thing()
```

---

## Raising exceptions

Exceptions can be raised using `raise <exception>` with optional arguments.

```python
raise RuntimeError()
raise RuntimeError("error message")
```

--

## Accessing the exception
Use "as" to access the exception object
```python
try:
    raise RuntimeError("o hai")
except RuntimeError as e:
    print(e)
```

--

## Propagating exceptions

Try-blocks can be nested;
All exceptions propagate to the top-level "root exception handler" if uncaught.
```python
try:
    try:
        raise Exception
    except Exception:
        print('Inner')
except Exception:
    print('Outer')
```

The (default) root exception handler terminates the Python process.

--

## Propagating exceptions
Propagation can be forced by using raise without arguments.
this re-raises the most recent exception.
```python
try:
    try:
        raise Exception
    except Exception:
        print('Inner')
        raise
except Exception:
    print('Outer')
```

This is useful for e.g. exception logging.

--


## More cool stuff
Code in the `finally` block will always be executed (unless Python crashes completely).

```python
try:
    open_file()
except IOError:
    print('Exception caught')
finally:
    close_file()
```

--

## More cool stuff
Code in the `else` block will be executed when no exception is raised

```python
try:
    open_file()
except IOError:
    print('Exception caught')
else:
    print('Everything went according to plan')
```

---

## Exception matching
Exceptions are matched by superclass relationships.

- RuntimeError
- StandardError
- Exception
- BaseException

```python
try:
    raise RuntimeError
except Exception as e:
    print(e.__class__)
```

--

## Exception matching
- Exceptions are matched by superclass relationships. 
- exception hierarchies can be designed.
- For example, `OverflowError`, `ZeroDivisionError` and `FloatingPointError` 
are all subclasses of `ArithmeticError`.
- Just write a handler for `ArithmeticError` to catch any of them.

--

## Writing your own
It's as simple as

```python
class MyException(Exception):
    pass
```