
# The Standard Library

---

# Time

--

-   `time.time` return the time in seconds since the epoch as a floating point number.

        import time
        t0 = time.time()
        for i in range(10000000):
            pass
        t1 = time.time()
        print(t1 - t0)

        # output:
        1.1572110652923584

--

-   `time.sleep` Suspend execution for the given number of seconds.

        import time
        print('Processing, please wait, ...')
        time.sleep(2)
        print('Done.')

        # output:
        Processing, please wait, ...
        Done.

---

# Logging

--
### Logging

-   In large and long running programs we need more sophisticated printing.
-   The logging package enables us to easily log the current state and timestamp of our program

--

-   Basic usage:

        logging.debug('Alltems operational')
        logging.info('Airspeed knots')
        logging.warn('Lowfuel')
        logging.error('Nol. Trying to glide.')
        logging.critical('Glide attempt failed. About to crash.')

        # output:
        WARNING:root:Lowfuel
        ERROR:root:Nol. Trying to glide.
        CRITICAL:root:Glide attempt failed. About to crash.

-   Why can't we see the `debug` and `warning` messages?

--

-   We can determine the varbosity of the log with `setLevel`

        logging.root.setLevel(logging.DEBUG)
        logging.debug('Alltems operational')
        logging.info('Airspeed knots')

        # output
        DEBUG:root:Alltems operational
        INFO:root:Airspeed knots

--

-   With `basicConfig` we can create customisations that fits our needs.
-   For example make our logs more informative:

        logging.basicConfig(format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d]  %(message)s',
                            level=logging.DEBUG)
        logging.debug("you'll see a lot more information now...")

        # output
        [DEBUG 2015-07-14 22:59:59,160 <ipython-input-60-8bd2b8d57226>:5]  you'll see a lot more information now...

--

-   Or logging to a file:

        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('This message should go to the log file')

--

-   Resources:
    -   [Logging module docs](https://docs.python.org/3.5/library/logging.html)
    -   [Logging howto](https://docs.python.org/3.5/howto/logging.html)
    -   [Become a Logging Expert in 30 Minutes](https://youtu.be/24_4WWkSmNo), Gavin M. Roy, PyCon 2013

---

# OS

--
### OS
-   `os.listdir` return a list containing the names of the entries in the directory given by path:

        import os

        for filename in os.listdir('.'):
            print(filename)

        # output
        The-standard-library.ipynb
        example.log
        unit-tests.ipynb

--

-   `os.path.join` concatenate paths (according to OS):

        import os

        home = '/home/user'
        os.path.join(home, 'Downloads')

        # output
        '/home/user/Downloads'

-   `os.path.splitext` splits the file into root, extension:

        os.path.splitext('/home/noam/Downloads/xom.csv')

        # output
        ('/home/noam/Downloads/xom', '.csv')

--

-   `os.path.getsize`

        os.path.getsize('The-standard-library.ipynb')

        # output
        8440



-   `os.path.isdir`

        os.path.isdir('The-standard-library.ipynb')

        # output
        False

---

# Sys and argparse

--
### Sys
- `sys.argv[0]` contains file name
- `sys.argv[1:]` contains arguments (if any)

--

#### Example
-   test.py:

        import sys

        def main(argv):
            a = int(argv[1])
            b = int(argv[2])
            return a + b

        if __name__ == '__main__':
            print(main(sys.argv))

-   cmdline:

        $ python test.py 5 10
        15

--

### argparse
-   A standard library solution for parsing script arguments
-   Generates help messages
-   Robust and clear
-   learn more at [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
--

### argparse example
-   test.py:

        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("square",
                            help="display a square of a given number",
                            type=int)
        args = parser.parse_args()
        print(args.square**2)

-   cmdline:

        $ python3 test.py 4
        16

--

###### Exercises

[The standard library](http://lms.10x.org.il/item/144/)

---

# Subprocess

--

The subprocess module provides a consistent interface to creating and working with additional
processes.

--
### Simple call
-   To run an external command without interacting with it, use the `call()` function.

        import subprocess

        subprocess.call(['ls', '-1'], shell=True)

--

-   The return value from `call()` is the exit code of the program.
-   The caller is responsible for interpreting it to detect errors.

--
### Error handeling

-   The `check_call()` function works like `call()` except that the exit code is checked,
    and if it indicates an error happened then a `CalledProcessError` exception is raised.

        import subprocess

        subprocess.check_call(['false'])

--
### Capturing Output
-   The standard input and output channels for the process started by `call()` are bound to
    the parent’s input and output.
-   Use `check_output()` to capture the output for later processing.

        import subprocess

        output = subprocess.check_output(['ls', '-1'])
        print('Have {} bytes in output'.format(len(output)))
        print(output)

---

# Threading

--

-   The simplest way to use a Thread is to instantiate it with a target function and call `start()`
    to let it begin working.

        import threading

        def worker(num):
            """thread worker function"""
            print('Worker: {}'.format(num))
            return

        for i in range(5):
            t = threading.Thread(target=worker, args=(i,))
            t.start()

--

-   Many time we run threads and wish that the main process will collect their result, to do so
    we use the `join` method

        import threading, random, time

        def worker(num, sleep):
            print('Worker #{} starts to sleep {} seconds '.format(num, sleep))
            time.sleep(sleep)
            print('Worker #{} woke up '.format(num))
            return

        threads = []
        for i in range(5):
            sleep_time = random.randint(1,5)
            t = threading.Thread(target=worker, args=(i, sleep_time,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

---

### Reference
-   [pymotw](https://pymotw.com/2/) - Python module of the week
-   Standard Library [documentation](https://docs.python.org/3/library)
