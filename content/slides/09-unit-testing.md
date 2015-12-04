# Unit testing
### Pycubator

--
### What for?

-   Fixing defects early costs less than fixing them late.
-   Defects removed in Unit Testing cost around 10 times less than defects removed in Functional
    verification.
-   And around 40 times less than defects removed by Systems or Integration testing.

--

### What is Unit Testing?


-   A unit test isolates a part of the program
-   Tests a single behaviour
-   Clearly identifies any reason for failure
-   Documents expected behaviour
-   Runs quickly

--

### A test is not a unit test if

*   It talks to the database
*   It communicates across the network
*   It touches the file system
*   It can't run at the same time as other unit tests
*   You have to do special things to your environment (such as editing config files) to run it

Source: [Michael Feathers' blog](http://www.artima.com/weblogs/viewpost.jsp?thread=126923) (2005)

---

# Unit test demonstration

--

### Interleave

-   Lets write a function to interleave two lists
-   It will be okay if one list is longer than the other
-   Before we start writing the code, we should know what the function should produce for all types
    of inputs:

        interleave([], []) # -> []
        interleave([1,5,3], ["hello"]) # -> [1,"hello",5,3]
        interleave([True], [[], 8]) # -> [True, [], 8]

--

-   Write the test first, `interleave_test.py`:

        from interleave import interleave
        import unittest

        class TestGettingStartedFunctions(unittest.TestCase):
            def test_interleave(self):
                cases = [
                    ([], [], []),
                    ([1], [9], [1, 9]),
                    ([2], [7, 8, 9], [2, 7, 8, 9]),
                ]

                for a, b, expected in cases:
                    self.assertEqual(interleave(a, b), expected)

        if __name__ == '__main__':
            unittest.main()


--

-   Write a stub, `interleave.py`:

        def interleave(a, b):
            return None

--

-   Run the test

        $ python interleave_test.py
        F
        ======================================================================
        FAIL: test_interleave (__main__.TestGettingStartedFunctions)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "interleavetest.py", line 15, in test_interleave
            self.assertEqual(interleave(a, b), expected)
        AssertionError: None != []

        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        FAILED (failures=1)

--

-   Now write the code

        def interleave(a, b):
            """Return the interleaving of two sequences as a list."""
            return [y for x in izip_longest(a, b) for y in x if y is not None]

--

-   Test again

        $ python interleave_test.py
        E
        ======================================================================
        ERROR: test_interleave (__main__.TestGettingStartedFunctions)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "interleavetest.py", line 15, in test_interleave
            self.assertEqual(interleave(a, b), expected)
          File "/Users/raytoal/scratch/interleave.py", line 3, in interleave
            return [y for x in izip_longest(a, b) for y in x if y is not None]
        NameError: global name izip_longest is not defined

        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        FAILED (errors=1)
--

-   Fix the code

        from itertools import izip_longest

        def interleave(a, b):
            """Return the interleaving of two sequences as a list."""
            return [y for x in izip_longest(a, b) for y in x if y is not None]

--

-   Rerun the test

        $ python interleave_test.py
        .
        -------------------------------------------------------------
        Ran 1 test in 0.000s

        OK

---
# Resources and exercise

--
### Resources
-   Ray Toal, [unittest in 5 minutes](http://www.slideshare.net/raytoal/unittest-in-5-minutes)
-   Python stdlib [documentation](https://docs.python.org/3/library/unittest.html#module-unittest)


--
###### Exercise
[Unit testing](Unit-Testing.html)
