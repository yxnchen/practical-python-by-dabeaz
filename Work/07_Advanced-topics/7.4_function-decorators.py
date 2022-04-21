# 1 logging example
from time import time


def add(x, y):
    return x + y
# and the function with some logging added to it:
def add(x, y):
    print(f'Adding {x} and {y}')
    return x + y

def sub(x, y):
    print(f'Subtracting {x} and {y}')
    return x - y
"""
Observation: It’s kind of repetitive.

Writing programs where there is a lot of code replication is often really annoying. 
They are tedious to write and hard to maintain. 
Especially if you decide that you want to change how it works (i.e., a different kind of logging perhaps).
"""

# 2 code that makes logging
# Perhaps you can make a function that makes functions with logging added to them. A wrapper.
def logged(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

def add(x, y):
    return x + y
logged_add = logged(add)
# You see the logging message appear
res = logged_add(3, 4)
"""
This example illustrates the process of creating a so-called wrapper function.

A wrapper is a function that wraps around another function with some extra bits of processing, 
but otherwise works in the exact same way as the original function.

Note: The logged() function creates the wrapper and returns it as a result.
"""

# 3 decorators
# Putting wrappers around functions is extremely common in Python. 
# So common, there is a special syntax for it.
@logged
def add(x, y):
    return x + y
# The special syntax performs the same exact steps as shown above. A decorator is just new syntax. 
# It is said to decorate the function.


"""
Commentary
There are many more subtle details to decorators than what has been presented here. 
For example, using them in classes. Or using multiple decorators with a function. 
However, the previous example is a good illustration of how their use tends to arise. 
Usually, it’s in response to repetitive code appearing across a wide range of function definitions. 
A decorator can move that code to a central definition.
"""

# 4.1 exec: a decorator for timing
# If you define a function, its name and module are stored in the __name__ and __module__ attributes.
def sleep_func(n):
    import time
    time.sleep(n)

print(sleep_func.__name__)
print(sleep_func.__module__)

# In a file timethis.py, write a decorator function timethis(func) that wraps a function with 
# an extra layer of logic that prints out how long it takes for a function to execute. 
# To do this, you’ll surround the function with timing calls like this:
import time
start = time.time()
r = sleep_func(3)
end = time.time()
print(f'Elapsed time for {sleep_func.__module__}.{sleep_func.__name__}: {end - start:.4f}s')

from timethis import timethis
@timethis
def countdown(n):
    while n > 0:
        n -=1

countdown(10000000)

"""
Discussion: 
This @timethis decorator can be placed in front of any function definition. 
Thus, you might use it as a diagnostic tool for performance tuning.
"""
