"""
This section discusses a few built-in decorators that are used in combination with method definitions.

predefined decorators
There are predefined decorators used to specify special kinds of methods in class definitions.

class Foo:
    def bar(self,a):
        ...

    @staticmethod
    def spam(a):
        ...

    @classmethod
    def grok(cls,a):
        ...

    @property
    def name(self):
        ...
"""

# 1 static methods
# @staticmethod is used to define a so-called static class methods (from C++/Java). 
# A static method is a function that is part of the class, but which does not operate on instances.

class Foo(object):
    @staticmethod
    def bar(x):
        print('x = ', x)
        
Foo.bar(1)

# Static methods are sometimes used to implement internal supporting code for a class. 
# For example, code to help manage created instances (memory management, system resources, persistence, locking, etc). 
# They’re also used by certain design patterns (not discussed here).

# 2 class methods
# @classmethod is used to define class methods. 
# A class method is a method that receives the class object as the first parameter instead of the instance.

class Foo:
    def bar(self):
        print(self)
    
    @classmethod
    def spam(cls):
        print(cls)
        
f = Foo()
f.bar()  # the instance f
Foo.spam()  # the class Foo

# Class methods are most often used as a tool for defining alternate constructors.
from select import select
import time
class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def today(cls):
        # notice how the class is passed as an argument
        tm = time.localtime()
        # and used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
d = Date.today()
print(d.__class__)

# Class methods solve some tricky problems with features like inheritance.
class NewDate(Date):
    pass

nd = NewDate.today()
print(nd.__class__)

# 3.1 exec: class methods in practice
# In your report.py and portfolio.py files, the creation of a Portfolio object is a bit muddled. 
# and the portfolio.py file defines Portfolio() with an odd initializer like this:
"""
class Portfolio:
    def __init__(self, holdings):
        self.holdings = holdings
    ...
"""

# If a Portfolio class is supposed to contain a list of Stock instances, 
# maybe you should change the class to be a bit more clear.
from portfolio import Portfolio
    
with open('./Work/Data/portfolio.csv') as f:
    portfolio = Portfolio.from_csv(f)
for s in portfolio.holdings:
    print(s)
