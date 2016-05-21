# Object Orientation
<!-- .slide: data-background="img/3D-Object-Pictures.jpg" -->

--

### Class statement

    class Foo:        #python2 Foo(object):
        pass

- `class Foo` &srarr; `class Foo(object)`
- Classes are ways to define new objects
- Creates a new class object named Foo
- Class definitions create a new namespace (scope)
- Variables defined in the class body are *class attributes*
- Functions defined in the class body are *instance methods*

--
### Constructors

    class Circle:
        def __init__(self, radius):
            self.r = radius

- `__init__` initializes an instance of the class
- `x = Circle()`
    - Creates an object of type `Circle`
    - Calls `Circle.__init__(self)`
    - Binds self to the name x

--

### Instance methods

    class Circle:
        def __init__(self, radius=5):
            self.r = radius
        def get_perimter(self, a, b):
            return 2 * math.pi * self.r

-   Instance method definitions must use self as the first argument

--
### Private by convention

-   A leading `_` means use at your own risk
-   "We're all adults here": you can still access any variable that you want

        class Circle:
            _pi = 3.14
            ...

            def get_perimter(self):
                return 2 * self._pi * self.r

--
###### Exercise
[Python Classes](http://lms.10x.org.il/item/46/)

---

# Inheritance
<!-- .slide: data-background="img/William_Hogarth_Inheritance.jpg" -->
From William Hogarth's [A Rake's Progress](http://en.wikipedia.org/wiki/A_Rake%27s_Progress).
"The Young Heir Takes Possession Of The Miser's Effects".
--

## Single inheritance

    class Circle(Shape):
        def __init__(self):
            super().__init__()     # python2 super(Circle, self).__init__()
            self.new_var = default

- Super classes are arguments to the `class` statement
- `object` is the default base class
- `class Circle(Shape)`: inherits from Shape
- Make sure to call the `__init__` of the super class

--

##### advanced
## Multiple inheritance

    class Circle(Shape, Drawable):
        def __init__(self):
            super().__init__(self)

- You can inherit from multiple super classes
- Attributes will be resolved via the MRO (Method Resolution Order)
- `Circle.mro()`

--

###### Exercise
[Class inheritance](http://lms.10x.org.il/item/116/)

---

##### Advanced
# Python Magic! (methods)
<!-- .slide: data-background="img/magic_mist.jpg" -->

--
## Magic Methods

- *Syntactic sugar* is done with magic methods
- Methods of the form `__method_name__` are "magic"
- Things like `f()` and `seq[i]` are magic method calls

--

## __new__, __init__, __call__
- `x = C()` &srarr; `x = C.__init__(C.__new__())`
    - `__new__` creates a new object
    - `__init__` initializes it
- `x(arg,...)` &srarr; `x.__call__(arg,...)`

--

## __str__, __repr__
- `str(x)` &srarr; `x.__str__()`
    - Returns a human readable string
- `repr(x)` &srarr; `x.__repr__()`
    - Returns a complete description of object


--

## Comparisons
- `x < y` &srarr; `x.__lt__(y)`
- `x > y` &srarr; `x.__gt__(y)`
- `x <= y` &srarr; `x.__le__(y)`
- `x >= y` &srarr; `x.__ge__(y)`
- `x == y` &srarr; `x.__eq__(y)`
- `x != y` &srarr; `x.__ne__(y)`

--

## Arithmetic operations
- All the arithmetic operators have magic methods
- `__add__, __sub__, __mod__, __xor__, ...`
- Additional methods for += and others

--

## getattr
- `x.value` &srarr; `getattr(x, 'value')`
- Useful when the attribute name is defined at runtime
- `getattr(self, name)` calls `__getattribute__(self, name)` which falls back on `__getattr__(self, name)`
- Defining `__getattr__` is useful to specify default values
- `getattr(x, 'value', default)` lets you give a default if everything else fails


---

##### advanced
# Advanced topics

--
### Attribute Lookups
- `Foo.__dict__` is a dictionary storing class attributes
- `Foo.val` translates to `Foo.__dict__['val']`
- Given `x = Foo()` then `x.__dict__` is a dictionary storing instance attributes
- x.val translates to:
    - `x.__dict__['val']` if val is an instance attribute
    - `Foo.__dict__['val']` if there is no instance attribute named val but there is a class attribute named val

--

### Static methods

    class Circle:
        @staticmethod
        def radius_to_perimeter(r):
            return 2 * math.pi * r

-   Attach functions to classes (with similar context)
-   A static method doesn't receive a self argument
-   Static methods should not depend on class attributes

--

### Class methods

    class Circle:
        @classmethod
        def from_circumference(cls, circ):
            return cls(circ/(2 * math.pi))

- A class method gets the class object as self.
- Alternative constructor.
- Call the first argument cls.

--

### Private attributes

- `__`
    - A leading __ is used to prevent subclasses from accidentally overwriting stuff
    - It does so by triggering *name mangling*:
        - `__some_var` &srarr; `_classname__some_var`
        - classname is the name of the class which `__some_var` was defined in
    - If you know the classname and variable you can do the mangling yourself

--

## No getters and setters???
- Python's `@property` and `@attr.setter` replace the need for getters and setters
- Decorate method with `@property` to replace attribute getter
    - Gets called in `x.attr`
- Decorate with `@attr.setter` to replace attribute setter
    - Gets called in `x.attr = val`

--
## Super

- `super(cls, obj)` &srarr; `super(C, self)`
    - When wish to call super outside a class method you need to provide it with the class name and it's content.
    - Class that precedes cls in the MRO of obj
    - It's bound &srarr; obj gets inserted into method calls
- `super()`
    - when called in an instance method of a class, will call it's root class.
