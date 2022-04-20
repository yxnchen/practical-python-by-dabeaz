"""
Inheritance is used to specialize existing objects:

class Parent:
    ...

class Child(Parent):
    ...
    
The new class Child is called a derived class or subclass. 
The Parent class is known as base class or superclass. 
Parent is specified in () after the class name, class Child(Parent):.

With inheritance, you are taking an existing class and:
- Adding new methods
- Redefining some of the existing methods
- Adding new attributes to instances
"""
import stock

class MyStock(stock.Stock):
    # 4 __init__ and inheritance:
    # If __init__ is redefined, it is essential to initialize the parent.
    # You should call the __init__() method on the super which is the way to 
    # call the previous version as shown previously.
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
    # 1 add a new method
    def panic(self):
        self.sell(self.shares)
    # 2 redefine an existing method
    def cost(self):
        # 3 overiding: 
        # Sometimes a class extends an existing method, 
        # but it wants to use the original implementation inside the redefinition. 
        # For this, use super():
        actual_cost = super().cost()
        return self.factor * actual_cost
    

s = MyStock('ACME', 50, 91.1, 1.25)
s.sell(25)
print(s.shares)
print(s.cost())
s.panic()
print(s.shares)


# 5 using inheritance
"""
Inheritance is sometimes used to organize related objects.

However, a more common (and practical) usage is related to making reusable or extensible code. 
For example, a framework might define a base class and instruct you to customize it.

The base class contains some general purpose code. 
Your class inherits and customized specific parts.
"""
# "is a" relationship:
# Inheritance establishes a type relationship.
class Shape(object):
    pass

class Circle(Shape):
    pass

c = Circle()
print('c is a Circle:', isinstance(c, Circle))
print('c is a Shape:', isinstance(c, Shape))

# object base class
# If a class has no parent, you sometimes see object used as the base.
# e.g., class A(object):
# object is the parent of all objects in Python.

# 6 multiple inheritance
# You can inherit from multiple classes by specifying them in the definition of the class.
# The class Child inherits features from both parents. There are some rather tricky details. 
# Don’t do it unless you know what you are doing.
class Mother:
    pass

class Father:
    pass

class Child(Mother, Father):
    pass


# 7.1 7.2 exec: report.py
# Suppose that you wanted to modify the print_report() function to support a variety of different 
# output formats such as plain-text, HTML, CSV, or XML. 
# To do this, you could try to write one gigantic function that did everything. 
# However, doing so would likely lead to an unmaintainable mess. 
# Instead, this is a perfect opportunity to use inheritance instead.
# see tableformat.py

# Polymorphism in Action
# A major feature of object-oriented programming is that you can plug an object into a program and 
# it will work without having to change any of the existing code. 
# For example, if you wrote a program that expected to use a TableFormatter object, 
# it would work no matter what kind of TableFormatter you actually gave it. 
# This behavior is sometimes referred to as “polymorphism.”

import sys
sys.path.append('./Solutions/3_18')
# import report
import tableformat

def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Cost'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:.2f}', f'{change:.2f}']
        formatter.row(rowdata)
        
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    import report
    portfolio = report.read_portfolio(portfoliofile)
    prices = report.read_prices(pricefile)
    report = report.make_report_data(portfolio, prices)
    # if fmt == 'txt':
    #     formatter = tableformat.TextTableFormatter()
    # elif fmt == 'csv':
    #     formatter = tableformat.CSVTableFormatter()
    # elif fmt == 'html':
    #     formatter = tableformat.HTMLTableFormatter()
    # else:
    #     raise RuntimeError(f'Unknown format: {fmt}')
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    
portfolio_report('./Work/Data/portfolio.csv', './Work/Data/prices.csv', 'csv')