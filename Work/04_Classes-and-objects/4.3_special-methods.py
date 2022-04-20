"""
Various parts of Python’s behavior can be customized via special or so-called “magic” methods. 
This section introduces that idea. In addition dynamic attribute access and bound methods are discussed.

Classes may define special methods. These have special meaning to the Python interpreter. 
They are always preceded and followed by __. For example __init__.

There are dozens of special methods, but we will only look at a few specific examples.
"""

# 1 special methods for string conversions
# objects have 2 string representations:
# - The str() function is used to create a nice printable output:
# - The repr() function is used to create a more detailed representation for programmers.
# Those functions, use a pair of special methods in the class to produce the string to be displayed.
"""
    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
"""
from datetime import date
d = date(2012, 12, 21)
print(d)
print(repr(d))
# Note: The convention for __repr__() is to return a string that, when fed to eval(), will recreate the underlying object. 
# If this is not possible, some kind of easily readable representation is used instead.


# 2 special methods for mathematics
"""
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()
"""

# 3 special methods for item access
# These are the methods to implement containers.
"""
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
"""

# 4 method invocation
# Invoking a method is a two-step process.
# - Lookup: The . operator
# Method call: The () operator
from stock import Stock
s = Stock('ACME', 100, 123.45)
c = s.cost  # lookup
print(c)
print(c())  # method call

# 5 bound methods
# A method that has not yet been invoked by the function call operator () is known as a bound method. 
# It operates on the instance where it originated.
# Bound methods are often a source of careless non-obvious errors.
"""
print('Cost : %0.2f' % s.cost)
"""
# Or devious behavior that’s hard to debug.
"""
f = open(filename, 'w')
...
f.close     # Oops, Didn't do anything at all. `f` still open.
"""

# 6 attribute access
# There is an alternative way to access, manipulate and manage attributes.
"""
getattr(obj, 'name')          # Same as obj.name
setattr(obj, 'name', value)   # Same as obj.name = value
delattr(obj, 'name')          # Same as del obj.name
hasattr(obj, 'name')          # Tests if attribute exists
"""
# Note: getattr() also has a useful default value *arg.
"""
x = getattr(obj, 'x', None)
"""

# 7.1 exec: better output for printing objects
# Modify the Stock object that you defined in stock.py so that the __repr__() method produces 
# more useful output.
goog = Stock('GOOG', 100, 490.10)
print(repr(goog))

# 7.2 exec: example of using getattr()
# getattr() is an alternative mechanism for reading attributes. 
# It can be used to write extremely flexible code. 
columns = ['name', 'shares']
for c in columns:
    print(c, '=', getattr(goog, c))
# Carefully observe that the output data is determined entirely by the attribute names 
# listed in the columns variable.

# In the file tableformat.py, take this idea and expand it into a generalized function print_table() 
# that prints a table showing user-specified attributes of a list of arbitrary objects.
import sys
sys.path.append('./Solutions/3_18')
import report
# need to modify the report.py file to use Stock objects first.
# pf = report.read_portfolio('./Work/Data/portfolio.csv')
pf = [
    Stock('GOOG', 100, 490.10),
    Stock('AAPL', 50, 545.75),
    Stock('FB', 200, 7.45),
    Stock('MSFT', 30, 32.11)
]
from tableformat import print_table, create_formatter
formatter = create_formatter('txt')
print_table(pf, ['name', 'shares'], formatter)
print_table(pf, ['name', 'shares', 'price'], create_formatter('csv'))
