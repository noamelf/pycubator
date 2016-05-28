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
