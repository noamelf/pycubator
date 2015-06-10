# Object orientation
<!-- .slide: data-background="img/3D-Object-Pictures.jpg" --> 

--

## Class statement
```python
class Foo:
    statement1
    statement2 
```
- Classes are ways to define new objects
- Creates a new class object named Foo
- Class definitions create a new namespace (scope)
- Variables defined in the class body are *class attributes*
- Functions defined in the class body are *instance methods*

--
## Constructors
```python
class Circle:
    def __init__(self, radius):
        self.r = radius
```
- `__init__` initializes an instance of the class
- `x = Circle()`
    - Creates an object of type `Foo` 
    - Calls `Circle.__init__(self)`
    - Binds self to the name x
    
-- 

## Attribute Lookups
- `Foo.__dict__` is a dictionary storing class attributes
- `Foo.val` translates to `Foo.__dict__['val']`
- Given `x = Foo()` then `x.__dict__` is a dictionary storing instance attributes
- x.val translates to:
    - `x.__dict__['val']` if val is an instance attribute
    - `Foo.__dict__['val']` if there is no instance attribute named val but there is a class attribute named val

--

## Instance methods
```python
class Foo:
    def no_arg(self):
        pass
    def two_args(self, a, b):
        return (a, b)
```
- Instance method definitions must use self as the first argument
- Given `x = Foo()`
    - `x.no_arg()` &srarr; `Foo.__dict__['no_arg'](x)`
    - `x.two_args(1, 2)` &srarr; `Foo.__dict__['two_args'](x, 1, 2)`

--

## Static methods
```python
class Circle:
    @staticmethod
    def radius_to_perimeter(r):
        return 2 * math.pi * r 
```
- Attach functions to classes (with similar context)
- A static method doesn't receive a self argument
- Static methods should not depend on class attributes

--

## Class methods
```python
class Circle:
    @classmethod
    def from_circumference(cls, circ):
        return cls(circ/(2 * math.pi)) 
```
- A class method gets the class object as self.
- Alternative constructor.
- Call the first argument cls.

--

## Private attributes
- \_
    - A leading _ means use at your own risk
    - `from mod import *` will not import names with a leading _
- \_\_
    - A leading __ is used to prevent subclasses from accidentally overwriting stuff
    - It does so by triggering *name mangling*:
        - `__some_var` &srarr; `_classname__some_var`
        - classname is the name of the class which `__some_var` was defined in

-- 

## We're all adults here
- You can still access any variable that you want
- If you know the classname and variable you can do the mangling yourself

--

## No getters and setters???
- Python's `@property` and `@attr.setter` replace the need for getters and setters
- Decorate method with `@property` to replace attribute getter
    - Gets called in `x.attr`  
- Decorate with `@attr.setter` to replace attribute setter
    - Gets called in `x.attr = val`

---

# Inheritance
<!-- .slide: data-background="img/William_Hogarth_Inheritance.jpg" --> 
<small> From William Hogarth's [A Rake's Progress](http://en.wikipedia.org/wiki/A_Rake%27s_Progress). 
"The Young Heir Takes Possession Of The Miser's Effects".</small>
--

## Single inheritance 
```python
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.new_var = default
```
- Super classes are arguments to the `class` statement
- `object` is the default base class
- `class Foo` &srarr; `class Foo(object)`
- `class Circle(Shape)` &srarr; inherits from Shape
- Make sure to call the `__init__` of the super class

--

## Multiple inheritance
```python
class Circle(Shape, Drawable):
    def __init__(self):
        super().__init__(self)
```
- You can inherit from multiple super classes
- Attributes will be resolved via the MRO (Method Resolution Order)
- `Circle.mro()`

-- 

## Super
- `super()` 
    - when called in an instance method of a class, will call it's root class.
- `super(cls, obj)` &srarr; `super(C, self)`  
    - When wish to call super outside a class method you need to provide it with the class name and it's content.
    - Class that precedes cls in the MRO of obj
    - It's bound &srarr; obj gets inserted into method calls


---

# Python Magic! (methods)
<!-- .slide: data-background="img/magic_mist.jpg" --> 

--
## Magic Methods

- *Syntactic sugar* is done with magic methods
- Methods of the form `__method_name__` are "magic"
- Things like `f()` and `seq[i]` are magic method calls

-- 

## __new__, __init__, __del__, __call__
- `x = C()` &srarr; `x = C.__init__(C.__new__())`
    - `__new__` creates a new object
    - `__init__` initializes it
- `del x` removes the binding of `x` in the current scope
    - If `x` was the last reference to an object then `obj.__del__()` is called
- `x(arg,...)` &srarr; `x.__call__(arg,...)`

-- 

## __str__, __repr__, __format__
- `str(x)` &srarr; `x.__str__()`
    - Returns a human readable string
- `repr(x)` &srarr; `x.__repr__()`
    - Returns a complete description of object    
- `'{f_str}'.format(x)` &srarr; `x.__format__(f_str)`
    - Formats x according to f_str

-- 

## Comparisons
- `x < y` &srarr; `x.__lt__(y)`
- `x > y` &srarr; `x.__gt__(y)`
- `x <= y` &srarr; `x.__le__(y)`
- `x >= y` &srarr; `x.__ge__(y)`
- `x == y` &srarr; `x.__eq__(y)`
- `x != y` &srarr; `x.__ne__(y)`

-- 

## \_\_hash\_\_ and \_\_eq\_\_
- Hashing is used in dictionaries and sets
- If `__hash__` is not explicitly defined calling it will return the object id (`id()`) 
- User defined objects default to reference equality
- If you define `__eq__` but not `__hash__` the object is unhashable

-- 

## getattr
- `x.value` &srarr; `getattr(x, 'value')`
- Useful when the attribute name is defined at runtime 
- `getattr(self, name)` calls `__getattribute__(self, name)` which falls back on `__getattr__(self, name)`
- Defining `__getattr__` is useful to specify default values
- `getattr(x, 'value', default)` lets you give a default if everything else fails

-- 

## Containers
- `len(x)` &srarr; `x.__len__()`
- `x[i]` &srarr; `x.__getitem__(i)`
- `x[i] = y` &srarr; `x.__setitem__(i, y)`
- `x[start:stop:step]` &srarr; `x.__getitem__(slice(start, stop, step))`
- `k in x` &srarr; `x.__contains__(k)`

-- 

## Numeric Types
- All the arithmetic operators have magic methods
- `__add__, __sub__, __mod__, __xor__, ...`
- Additional methods for += and others
