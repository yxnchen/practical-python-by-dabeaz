"""This section introduces the idea of using functions to create other functions."""

# 1 introduction
# consider the following function:
def add(x, y):
    def do_add():
        print(f'Adding {x} and {y}')
        return x + y
    return do_add
# This is a function that returns another function.

a = add(3, 4)
print(a)
result = a()
print(result)

# 2 local variables
# Observe how the inner function refers to variables defined by the outer function.
"""
def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
"""
# Further observe that those variables are somehow kept alive after add() has finished.
"""
>>> a = add(3, 4)
>>> a()  # where are these values coming from?
Adding 3 and 4
"""

# 3 closures
# When an inner function is returned as a result, that inner function is known as a closure.
# Essential feature: 
# - A closure retains the values of all variables needed for the function to run properly later on. 
# - Think of a closure as a function plus an extra environment that holds the values of variables that it depends on.

# 4 using closures
# Closure are an essential feature of Python. However, their use is often subtle. Common applications:
"""
- Use in callback functions.
- Delayed evaluation.
- Decorator functions (later).
"""

# 5 delayed evaluation
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
# usage example:
def greeting():
    print('Hello!')
after(2, greeting)
# after executes the supplied function… later.
after(2, add(3, 4))  # do_add has the reference x->3 and y->4

# 6 code repetition
# Closures can also be used as technique for avoiding excessive code repetition. 
# You can write functions that make code.


# 7.1 exec: using closures to avoid code repetition
# One of the more powerful features of closures is their use in generating repetitive code. 
# If you refer back to Exercise 5.7, recall the code for defining a property with type checking.
"""
class Stock(object):
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise ValueError('shares must be an integer')
        if value < 0:
            raise ValueError('shares must be positive')
        self._shares = value
"""
# Instead of repeatedly typing that code over and over again, 
# you can automatically create it using a closure.
# Make a file typedproperty.py
from typedproperty import String, Integer, Float
class Stock:
    # name = typedproperty('name', str)
    # shares = typedproperty('shares', int)
    # price = typedproperty('price', float)
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price
s = Stock('ACME', 50, 91.1)
print(s.name)
try:
    s.shares = '50'
except ValueError as e:
    print(e)
    
# 7.2 exec: simplifying function calls
# In the above example, users might find calls such as typedproperty('shares', int) 
# a bit verbose to type–especially if they’re repeated a lot. 
# Add the following definitions to the typedproperty.py file:
# And, rewrite the Stock class to use these functions instead:
"""
The main takeaway here is that closures and lambda can often be used to simplify code and 
eliminate annoying repetition. This is often good.
"""

        