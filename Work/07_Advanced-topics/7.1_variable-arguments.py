"""
This section covers variadic function arguments, sometimes described as *args and **kwargs.
"""

# 1 Positional variable arguments (*args)
# A function that accepts any number of arguments is said to use variable arguments.
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)  get passed as a tuple
    print(x)
    for arg in args:
        print(arg)

f(1, 2, 3, 4, 5)

# 2 Keyword variable arguments (**kwargs)
# A function can also accept any number of keyword arguments.
def f2(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }  get passed as a dictionary
    print(x, y)
    for key, value in kwargs.items():
        print(key, value)

f2(1, 2, flag=True, name='John')

# 3 combineing both
# A function can also accept any number of variable keyword and non-keyword arguments.
def f3(*args, **kwargs):
    # args -> (1,2,3,4,5)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    print(args)
    print(kwargs)

f3(2, 3, flag=True, name='John')
# This function takes any combination of positional or keyword arguments. 
# It is sometimes used when writing wrappers or when you want to pass arguments through 
# to another function.

# 4 passing tuples and dicts
# tuples can be expanded into variable arguments
numbers = (2,3,4,5)
f(1, *numbers)
# dictionaries can be expanded into keyword arguments
options = {
    'color': 'red',
    'delimiter': '*',
    'width': 100
}
f2(2, 3, **options)

# 5.1 exec: a simple example of variable arguments
def avg(x, *more):
    return float(x + sum(more)) / (1 + len(more))
print(avg(10, 11))
print(avg(3,4,5))
print(avg(1,2,3,4,5))

# 5.2 exec: passing tuples and dicts as arguments
import sys
sys.path.append('./Work/04_Classes-and-objects')
from stock import Stock
data = ('GOOG', 100, 490.1)
s =Stock(*data)
print(s)

data = {'name': 'IBM', 'shares': 100, 'price': 490.1}
s =Stock(**data)
print(s)

# 5.3 exec: creating a list of instances
# in report.py, you created a list of instances of the Stock class like this:
"""
portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
"""
# can be simplified to:
"""
portfolio = [ Stock(**d) for d in portdicts ]
"""

# 5.4 exec: argument pass-through
# The fileparse.parse_csv() function has some options for changing the file delimiter and for error reporting. 
# Maybe you’d like to expose those options to the read_portfolio() function above. Make this change:
"""
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
"""
# and try
# port = report.read_portfolio('Data/missing.csv')
# port = report.read_portfolio('Data/missing.csv', silence_errors=True)
