# Compound Data Types
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### Overview
- Data types that are compound of smaller pieces, example: a string is made up from smaller strings containg  a single character.
- Support similar methods, although each type has it's own unique qualities and will be effective in certain use cases (and not others).
- Types included are: string, tuple, list, dictionary, set.

---

# String
<!-- .slide: data-background="img/string.jpg" -->

--
## Basics
- Holds a string of charcters.
- `'x'` or `"x"` for single lines.
- `'''x'''` for multiple lines
- Immutable

--
## Slicing
- Index with square brackets: `s[1]`
- Negative indexing gets elements from the end of list: `s[-1]`
- Slices:
  - Basic syntax is `s[start:end]`: `s[1:4]`
  - Slicing from the beginning of the string: `s[:5]`
  - Slicing untill the end of the string: `s[3:]`
  - Negative indexes cam also be used in slices: `s[-3:-1]`

--
## Methods
- `s.split(sep)`: returns a list of substrings separated by sep
- `s.strip()`: strips whitespace from ends
- `s.strip('abc')`: specify non-whitespace chars to remove (each separtly)
- `s.isspace()`: returns True if all chars in s are whitespace
- `s.lower()`: converts all characters to lowercase

--
## Join
- `s.join(str_list)`: concatenates the strings in `str_list` with s as a separator.
- When s is empty string: efficient way to concatenate strings
- Use space as s to join words with spaces

--
## Find and replace
- `s.find(sub)`: finds the starting index of the first occurrence of sub in s
- `s.replace(old,new)`: replaces all occurrences of old in s with new

--
## Formating (1)
- `s.format(arg1,arg2)`: replaces `{}` in s with args
- `{name!conversion:format}` provides options on top of `{}`
- Use `{0}{1}...{n}` to refer to positional arguments
- Use `{name}` and then `s.format(name=arg)` for named args
- `{!s} {!r} {!a}` call `str()`, `repr()` or `ascii()` before substitution
- `{:4}{:7}` at least x number of chars
- `{:b}{:x}` formats number as binary or hex


--
## formating (2)
- Lots of other stuff in [Format Specification Mini-Language](https://docs.python.org/2/library/string.html#format-specification-mini-language).
- [More examples](https://docs.python.org/2/library/string.html#format-examples)

---
# Tuple
<!-- .slide: data-background="img/tulips.jpg" -->
--
## Overview
- Tuples are used for grouping ordered data
- Support indexing and slicing syntax
- Immutable
- Powerful assigment feature (packing/unpacking)

--
## Basics
- Syntax `(1, 2, 'hi')` or just `1, 2, 'hi'` (be careful)
- `tuple()` construct a tuple from other iteratables
- Supports nested tuples `((1, 2), (3, 4))`
- Concatenating two tuples with + creates a new tuple.
- Accessed with `t[1]` or `t[1][2]` if nested
- Multiplying a tuple adds it to itself.

--
## Iterating correctly
- Iterate with `for x in tup`, then use x in the loop
- Never do `for i in range(len(tup))`, then use `tup[i]` in the loop
- Index and value with `for i,x in enumerate(tup)`
- Useful if you sometimes want `tup[2*i]` or `tup[i]`

--
## Powerful assigments
- `x = 1,`
- `x, y = 'hi', 'man'`
- `x, y = y, x`
- `return x,y`

---
# List
<!-- .slide: data-background="img/list.jpg" -->
--
## Basics
- An ordered collection of values
- Support most of the features that tuple supports
- Adds moflifing functionality since it is mutable
- Creation is slower than tuple
- `list()` and `[]` are both new empty lists

--
## modlfying
- `lst[i] = v`: Change an element or slice by assigning to it
- `lst.append(v)`: Add an element
- `lst.extend(vs)`: Add an iterable
- `lst.remove(v)`:remove a specific value
- `del lst[i]`: remove a specific index or range
- `lst.insert(i,v)`: insert before a certain index with
- `lst.pop(i)` remove and return index
- `lst.sort()`: in place sort

--
## Multiplication and Copies
- The component lists are not copies, they're the same object
- Shallow copy a list with `lst[:]`
- Use the copy module for deep copy: `copy.deepcopy(lst)`

---
# Dictionary
<!-- .slide: data-background="img/dictionary.jpg" -->

--
## Basics
- A dictionary is a hash map:
  - It hashes the keys to lookup values
  - Keys must be immutable so that the hash doesn't change
- `dict()` and `{}` are empty dictionaries
- `dict(((k1, v1), (k2, v2)))` or `{k1:v1, k2:v2}`
- `dict(zip(key_lst, val_lst))`: create a dict from to lists
- `d[k]` accesses the value mapped to `k`
- `d[k] = v` updates the value mapped to `k`

--
## Methods
- `len()`, `in`, and `del` work like lists
- `d.keys()` and `d.values()` return corresponding lists of the dict keys and values.
- `d.items()` prdouces a list of tuples `(k,v)`
- `d.get(k,x)` looks up the value of `k`. Returns `x` if `k not in d`
- `d.setdefault(k,x)` same as `d.get(k,x)`
- `d[k] = x` creates a key or changes that existing key value
- `d.pop(k,x)` return and remove value at `k`. Returns `x` as default

--
## Switch Statement Replacement
- Python doesn’t have a `switch(x)`, dictionaries do the job
- Replace long `if x = a: elif x = b: elif...` with a dictionary lookup

---
## Set
<!-- .slide: data-background="img/set.png" -->

--
## Basics
- No order, no duplicates
- Hash Set: elements must be immutable
- Empty set: `set()` not `{}` (empty dict)
- `{1, 'blah', 5, -1}`
- Can de-duplicate a list: `list(set(lst))`

--
## Methods
- `s.add(v)`: adds a value to set
- `s.remove(v)`: removes v. will raise an error if v not in s
- `s.discard(v)`: removes v. will not raise error
- `s.difference(s2)` -> s - s2: elements in s but not s2
- `s.union(s2)` -> s | s2: elements in s or s2
- `s.intersection(s2)` -> s & s2: elements in s and s2
- `s.update(s2)` -> s = s | s2

--
## Frozen Sets
- `frozenset({x, y, z})`
- Immutable version of set
- Can be used as dictionary keys and elements of other frozensets
- Same operations as sets except any that mutate (add, update)


---
# More On Sequences
<!-- .slide: data-background="img/sequences.jpg" -->

--
## Builtins
- `len(x)`: gives the number of elements
- `sum(x)`: adds up elements
- `a in x`: checks presence
- `all(x)/any(x)`: return True is any/all in lst are True
- `max(x)/min(x)`: biggest/smallest element
- `reversed(x)`: iterator of elements in reverse order (doesn't work for sets, why?)
- `zip(x,x)`: list of tuples with one element from each list
- `sorted(x)`: returns new sorted list

--
## List Comprehensions
- Compile a list with a one-liner.
- `[expr for v in iter]`
- `[expr for v in iter if cond]`
- This:
```python
res = []
for v1, v2 in lst:
    if v1 > v2:
        res.append(v1 * v2)
```
- Becomes that:
```python
res = [v1 * v2 for v1, v2 in lst if v1 > v2]
```

--
## Nested List Comprehensions
- This:
```python
res = []
for y in lst2:
    inter = []
    for x in lst1:
        inter.append(x)
```
- Becomes that:
```python
[[x for x in lst1] for y in lst2]
```

--
## Dictionary Comprehensions
- Like lists but swap `[]` for `{}`
- This:
```python
d = dict()
for k, v in lst:
    d[k] = v
```
- Becomes that:
```python
{k: v for k,v in lst}
```

--
## Set Comprehensions
- Like dictionaries but no `:`
- This:

```python
s = set()
for x in lst:
    s.add(x)

```
- Becomes that:

```python
{x for x in lst}
```

--
## Tuple Comprehensions?
```python
tup = (x for x in lst)
type(tup)
<class 'generator'>
```
- We'll cover generators later