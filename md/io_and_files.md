# Interactive Input
<!-- .slide: data-background="img/input.png" --> 
--
## Interactive Input

- `input()` will read up to a newline
- `input(prompt)` prints `str(prompt)` before reading input
- Python2 and Python3 difference:
    - Python3 `input()` is like Python2 `raw_input()`
    - Python2 `input()` actually does `eval(raw_input())`

--
## Practice 
Read line from user and print them to screen. Stop when user types 'end'.    
For example, if the user types:  
```
hi
noam
end
```

Screen will show:
```
hi
noam
```
---

# Files
<!-- .slide: data-background="img/files.jpg" --> 
<small> A corridor of files at The National Archives UK. wikimedia commons. <small>
--
## Opening Files

- `open(name, mode)` returns a file-object
- `name` is the path of the file to open
- `mode`:
    - `'r'` (read): the file is open in read-only mode
    - `'w'` (write): the file is open in write-only mode, and is truncated.
    - `'a'` (append): like 'w' but appends to the file
    - `'x'`: like 'w' but the file must not exist already
- `open(name)` defaults to read: `open(name, 'rt')`

--

## Closing
- `f.close()`:
    - Release the file handles 
    - Write the file object content to disk 
- Can be done alternatively using the `with` statement:
```python
with open('example.txt') as f:
    print(f.read())
```

--
## moving
- `f.seek(index)` move cursor to index 
- `f.tell()` returns cursor current index

--

## Reading
- `f.read()` reads the whole file (up to `EOF`)
- `f.read(index)` reads the file until `index` 
- `f.readline()` reads a line (up to `\n`)

--

## Writing
- `f.write(string)` writes string (without adding a newline)
- `f.writelines(sequence)` writes sequence content (without adding newlines)

--

## Other
- `f.flush()` flushes the write buffers
- `f.mode` read/write mode.
- `f.name` file name

--

## The `+`
- Supplying `'+'` after one of `'rwa'` is for reading and writing,
 but differ in the position in the file:
    - `'r+'` The stream is positioned at the beginning of the file.
    - `'w+'` The file is created if it does not exist, otherwise it is truncated. 
    The stream is positioned at the beginning of the file.
    - `'a+'` The stream is positioned at the end of the file.
      
--

![](img/open-diagram.jpg)

--
## Practice
Read a file one line at a time, and print the number of the line 
(start with one) and the line content.  
For example, for this input:
```
Ami
Udi
Assaf
```

The output will be:
```
1 Ami
2 Udi
3 Assaf
```

---

# stdin / stdout / stderror
<!-- .slide: data-background="img/stdin.png" --> 
--

## Definitions
- `stdin`: standard input
- `stdout`: standard output
- `stderr`: standard error

--
## stdin
- File like object
- test.py:

```python
import sys
print(sys.stdin.read())
```
- cmdline:

```bash 
$ echo 'hi' | python3 test.py
hi
```

-- 

## stdout, stderr
- `stdout` receives all 'regular' output.
- `stderr` receives all 'error' output.
- What if we want to redirect this output?

-- 

## Redirecting script(1)
test.py:    
```python
import sys
saveout, saverr = sys.stdout,sys.stderr
sys.stdout = open('/tmp/out.txt', 'w')
sys.stderr = open('/tmp/err.txt', 'w')
print('Hello')
printa('Hello')
sys.stdout, sys.stderr = saveout, saverr
```
--

## Redirecting script(2)
cmdline:
  
```bash 
$ python3 stdouterr.py
$ cat /tmp/out.txt
Hello
$ cat /tmp/err.txt
Traceback (most recent call last):
  File "stdouterr.py", line 6, in <module>
    printa('Hello')
NameError: name 'printa' is not defined
```

---

# Command line arguments
<!-- .slide: data-background="img/cmdline.png" --> 
--
## argv
- `sys.argv[0]` contains file name
- `sys.argv[1:]` contains arguments (if any)

--

## argv example 1
test.py:  
```python
import sys
for arg in sys.argv:
    print(arg)
```  
cmdline:  
```bash
$ python test.py
test.py
$ python args.py abc ijk
test.py
abc
ijk
```

--

## argv example 2
test.py:  
```python
import sys

def main(argv):
    a = int(argv[1])
    b = int(argv[2])
    return a + b

if __name__ == '__main__':
    print(main(sys.argv))
```

cmdline:  
```bash
prompt% python test.py 5 10
15
```
--

## argparse
- A standard library solution for parsing script arguments
- Generates help messages 
- Robust and clear
- learn more at [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
--

## argparse example
test.py:    
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", 
                    help="display a square of a given number", 
                    type=int)
args = parser.parse_args()
print(args.square**2)
```
cmdline:  
```bash
$ python3 test.py 4
16
```

--
## Practice
- Write a script that takes a flag -i as a command-line argument. 
- If the value of -i is "stdin", print the contents of stdin.
- If the value of -i is a valid filename, print the contents of the file.

---
## Extra practice!
Go to folders -> lec5 -> robot_pos_tracker.py 