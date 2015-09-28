# Dynamic typing
<small>image credits: Romul Nutiu - [blue dynamic universe](http://www.wikiart.org/en/romul-nutiu/blue-dynamic-universe)</small>
<!-- .slide: data-background="img/blue-dynamic-universe.jpg" --> 
--

## Dynamic typing

What does "dynamically typed" mean?

-   Variable types are not declared
-   Python figures the types out at runtime

--

## Dynamic typing

We can check types with our code:

```python
>>> type(x)
&lt;type 'int'&gt;
                
```

``` {.fragment}
>>> isinstance(x, int)
True
                
```

-   `isinstance` caters to inheritance and is more suitable for type
    check in production code
-   `type` is more suitable for fiddling and debugging

--

## Dynamic typing

Interpreter keeps track of all types and doesn’t allow you to do that
are incompatible with that type:

    >>> increment('3')
    TypeError: cannot concatenate 'str' and 'int' objects
    
--                 

## Duck typing

> "When I see a bird that walks like a duck and swims like a duck and
> quacks like a duck, I call that bird a duck."  
> James Whitcomb Riley

--

<!-- .slide: data-background="http://i.giphy.com/e2CIuhhEz7nJ6.gif" --> 

--
## Duck typing

```python
>>> def increment(x):
        try: 
            return x + 1
        except TypeError:
            return int(x) + 1
                
```

```python
>>> increment('3')
4
                
```

-   Duck typing is concerned with establishing the **suitability of an
    object for some purpose** rather than what type it is.
-   Very pythonic
