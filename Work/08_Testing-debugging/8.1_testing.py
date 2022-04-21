"""
Testing Rocks, Debugging Sucks
The dynamic nature of Python makes testing critically important to most applications. 
There is no compiler to find your bugs. 
The only way to find bugs is to run the code and make sure you try out all of its features.
"""

# 1 assertations
# The assert statement is an internal check for the program. 
# If an expression is not true, it raises a AssertionError exception.
"""
assert statement syntax.

assert <expression> [, 'Diagnostic message']
"""

assert isinstance(10, int), "Expected an integer"

# It shouldn’t be used to check the user-input (i.e., data entered on a web form or something). 
# It’s purpose is more for internal checks and invariants (conditions that should always be true).

# 2 contract programming
# Also known as Design By Contract, liberal use of assertions is an approach for designing software. 
# It prescribes that software designers should define precise interface specifications for 
# the components of the software.
# For example, you might put assertions on all inputs of a function.
def add(x, y):
    assert isinstance(x, int), "Expected an integer"
    assert isinstance(y, int), "Expected an integer"
    return x + y
# Checking inputs will immediately catch callers who aren’t using appropriate arguments.
try:
    add(2, 3)
    add(2, "3")
except AssertionError as e:
    print(e)

# 3 inline tests
# Assertions can also be used for simple tests.
assert add(2, 3) == 5
"""
This way you are including the test in the same module as your code.

Benefit: If the code is obviously broken, attempts to import the module will crash.

This is not recommended for exhaustive testing. It’s more of a basic “smoke test”. 
Does the function work on any example at all? If not, then something is definitely broken.
"""

# 4 'unittest' module
# Suppose you have some code.
"""
# simple.py

def add(x, y):
    return x + y
"""
# Now, suppose you want to test it. Create a separate testing file like this.
# # Then define a testing class.
"""
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    # define some testing methods
    # *Important: Each method must start with test.
    def test_simple(self):
        # test with simple integer arguments
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # test with string arguments
        r = simple.add("hello", "world")
        self.assertEqual(r, "helloworld")
"""

# 5 using 'unittest'
# There are several built in assertions that come with unittest. Each of them asserts a different thing.
"""
# Assert that expr is True
self.assertTrue(expr)

# Assert that x == y
self.assertEqual(x,y)

# Assert that x != y
self.assertNotEqual(x,y)

# Assert that x is near y
self.assertAlmostEqual(x,y,places)

# Assert that callable(arg1,arg2,...) raises exc
self.assertRaises(exc, callable, arg1, arg2, ...)
"""

# 6 running 'unittest'
# To run the tests, turn the code into a script.
"""
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
"""


"""
Effective unit testing is an art and it can grow to be quite complicated for large applications.

The unittest module has a huge number of options related to test runners, collection of results and 
other aspects of testing. Consult the documentation for details.
"""

# 7 third party testing tools
# The built-in 'unittest' module has the advantage of being available everywhere–it’s part of Python. 
# However, many programmers also find it to be quite verbose. A popular alternative is pytest. 
# With pytest, your testing file simplifies to something like the following:
"""
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
"""
# To run the tests, you simply type a command such as 'python -m pytest'. 
# It will discover all of the tests and run them.


# 8.1 exec: writing unit test
# For this exercise, it assumed that you’re using the code written 
# for Exercise 7.9 involving typed-properties.
# In a separate file test_stock.py, write a set a unit tests for the Stock class.

# Once you’re satisifed that it works, write additional unit tests that check for the following:
# - Make sure the s.cost property returns the correct value (49010.0) 
# - Make sure the s.sell() method works correctly. It should decrement the value of s.shares accordingly.
# - Make sure that the s.shares attribute can’t be set to a non-integer value.
