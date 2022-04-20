"""
Iteration (the for-loop) is one of the most common programming patterns in Python. 
Programs do a lot of iteration to process lists, read files, query databases, and more. 
One of the most powerful features of Python is the ability to customize and redefine iteration 
in the form of a so-called “generator function.” 
This section introduces this topic. 
By the end, you’ll write some programs that process some real-time streaming data in an interesting way.
"""

# 1 iteration everywhere
a = 'hello'
for c in a:
    print(c, end=' ')
print()

b = {'name': 'Guido', 'age': 56}
for k in b:
    print(k, '=', b[k], end=' ')
print()

c = [1, 2, 3]
for i in c:
    print(i, end=' ')
print()
    
f = open('./Work/Data/portfolio.csv')
for x in f:
    print(x, end='')
print()

# 2 iteration protocol
"""
for x in obj:
    # statements
"""
# what happens under the hood?
"""
_iter = obj.__iter__()        # Get iterator object
while True:
    try:
        x = _iter.__next__()  # Get next item
        # statements ...
    except StopIteration:     # No more items
        break
"""
# All the objects that work with the for-loop implement this low-level iteration protocol.
x = [1, 2, 3]
iter = x.__iter__()
print(iter)
while True:
    try:
        print(iter.__next__())
    except StopIteration:
        print('No more items')
        break

# 3 supporting iteration protocol
class Portfolio:
    def __init__(self) -> None:
        self.holdings = []
        
    def __iter__(self):
        return self.holdings.__iter__()
pf = Portfolio()
pf.holdings = ['pf1', 'pf2', 'pf3']
for s in pf:
    print(s)


# 4.1 exec: Iteration Illustrated
a = [1, 9, 8, 4, 5, 6, 7, 2, 3]
it = a.__iter__()
print(it.__next__())
print(it.__next__())
# The next() built-in function is a shortcut for calling the __next__() method of an iterator.
# Try using it on a file:
f = open('./Work/Data/portfolio.csv')
f.__iter__()  # note, this returns the file itself
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
print(next(f), end='')
# print(next(f), end='')

# 4.2 exec: supporting iteration on portofolio.py and modify report.py and pcost.py

# 4.3 exec: making a more proper container
# If making a container class, you often want to do more than just iteration. 
# Modify the Portfolio class so that it has some other special methods like this:
import sys
sys.path.append('./Solutions/3_18')
sys.path.append('./Work/04_Classes-and-Objects')
import fileparse
from stock import Stock
from portfolio import Portfolio
# report.py -> read_portfolio()
with open('./Work/Data/portfolio.csv') as file:
    portdicts = fileparse.parse_csv(file,
                                    select=['name','shares','price'],
                                    types=[str,int,float])

portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
obj = Portfolio(portfolio)

print(len(obj))
print(obj[0])
print(obj[0:3])
print('IBM in portfolio?', 'IBM' in obj)
print(obj.total_cost)
print(obj.tabulate_shares())
"""
One important observation about this–generally code is considered “Pythonic” 
if it speaks the common vocabulary of how other parts of Python normally work. 

For container objects, supporting iteration, indexing, containment, and other kinds of operators 
is an important part of this.
"""
