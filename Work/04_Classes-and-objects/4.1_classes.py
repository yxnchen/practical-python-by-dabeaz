""" object oriented programming (OOP)

An object consists of:

- Data. Attributes
- Behavior. Methods which are functions applied to the object.

nums is an instance of a list.
Methods (append() and insert()) are attached to the instance (nums).
"""

import sys
sys.path.append('./Solutions/3_18')

# 1 the class statement
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def damage(self, pts):
        self.health -= pts
# In a nutshell, a class is a set of functions that carry out various operations on so-called instances.


# 2 instances
# Instances are the actual objects that you manipulate in your program.
# They are created by calling the class as a function.
a = Player(2, 3)
b = Player(10, 20)
# Emphasize: The class statement is just the definition (it does nothing by itself). 
# Similar to a function definition.

# 3 instance data
# Each instance has its own local data.
# This data is initialized by the __init__().
print(a.x, a.y)

# 4 instance methods
# Instance methods are functions applied to instances of an object.
# The object itself is always passed as first argument.
a.move(1, 1)

# 5 class scoping
# class do not define a scope of names
# If you want to operate on an instance, you always refer to it explicitly (e.g., self).
"""
...
    def left(self, amt):
        move(-amt, 0)       # NO. Calls a global `move` function
        self.move(-amt, 0)  # YES. Calls method `move` from above.
...
"""

# 6.1 exec: objects as data structures
# In section 2 and 3, we worked with data represented as tuples and dictionaries.
# Thus, another approach for representing data would be to define a class. 
# Create a file called stock.py and define a class Stock that represents a single holding of stock.
import stock
a = stock.Stock('ACME', 100, 123.45)
print(a.name, a.shares, a.price)
b = stock.Stock('IBM', 50, 91.1)
c = stock.Stock('YHOO', 50, 17.1)
print(b.shares * b.price)
stocks = [a, b, c]
print(stocks)
for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')
# add some methods
print(a.cost())
a.sell(25)
print(a.shares)
print(a.cost())
# creating a list of instances
import fileparse
with open('./Work/Data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], 
                                    types=[str, int, float])
portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
print(portfolio)
print(sum([s.cost() for s in portfolio]))
# using your class
# Modify the read_portfolio() function in the report.py program so that 
# it reads a portfolio into a list of Stock instances as just shown in Exercise 4.3.
import pcost, report
print(pcost.portfolio_cost('./Work/Data/portfolio.csv'))
report.portfolio_report('./Work/Data/portfolio.csv', './Work/Data/prices.csv')
