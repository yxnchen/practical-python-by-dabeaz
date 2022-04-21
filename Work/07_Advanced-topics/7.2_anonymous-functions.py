"""
Anonymous Functions and Lambda
"""

# 1 list sorting revisited
# Lists can be sorted in-place. Using the sort method.
s = [2, 3, 1, 5, 4]
s.sort()
print(s)
s.sort(reverse=True)
print(s)
# how to sort a list of dicts? by what criteria?

# You can guide the sorting by using a key function.
# The key function is a function that receives the dictionary and returns the value of interest for sorting.
pf = [{'name': 'AA', 'price': 32.2, 'shares': 100},
{'name': 'IBM', 'price': 91.1, 'shares': 50},
{'name': 'CAT', 'price': 83.44, 'shares': 150},
{'name': 'MSFT', 'price': 51.23, 'shares': 200},
{'name': 'GE', 'price': 40.37, 'shares': 95},
{'name': 'MSFT', 'price': 65.1, 'shares': 50},
{'name': 'IBM', 'price': 70.44, 'shares': 100}]
def stock_name(s):
    return s['name']
pf.sort(key=stock_name)
print(pf)

# 2 callback functions
"""
In the above example, the key function is an example of a callback function. 
The sort() method “calls back” to a function you supply. 
Callback functions are often short one-line functions that are only used for that one operation. 
Programmers often ask for a short-cut for specifying this extra processing.
"""

# 3 lambda: anonymous functions
# Use a lambda instead of creating the function.
pf.sort(key=lambda s: s['name'])
print()
# This creates an unnamed function that evaluates a single expression. 
# The above code is much shorter than the initial code.

# 4 using lambda
"""
- lambda is highly restricted.
- Only a single expression is allowed.
- No statements like if, while, etc.
- Most common use is with functions like sort().
"""

# 5 exec: 
import sys
sys.path.append('./Solutions/3_18')
import fileparse
sys.path.append('./Work/04_Classes-and-Objects')
from stock import Stock
with open('./Work/Data/portfolio.csv') as file:
    portdicts = fileparse.parse_csv(file, select=['name','shares','price'], types=[str,int,float])
portfolio = [ Stock(**d) for d in portdicts ]
print(portfolio)

# 5.1 exec: sorting on a field
portfolio.sort(key=lambda s: s.name)
print(portfolio)
portfolio.sort(key=lambda s: s.shares)
print(portfolio)
portfolio.sort(key=lambda s: s.price)
print(portfolio)

"""
Note: lambda is a useful shortcut because it allows you to define a special processing function directly 
in the call to sort() as opposed to having to define a separate function first.
"""
