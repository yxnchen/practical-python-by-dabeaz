"""
When writing classes, it is common to try and encapsulate internal details. 
This section introduces a few Python programming idioms for this including private variables and properties.

Public vs Private.
One of the primary roles of a class is to encapsulate data and internal implementation details of an object. 
However, a class also defines a public interface that the outside world is supposed to use to manipulate the object. 
This distinction between implementation details and the public interface is important.

In Python, almost everything about classes and objects is open.
- You can easily inspect object internals.
- You can change things at will.
- There is no strong notion of access-control (i.e., private class members)
That is an issue when you are trying to isolate details of the internal implementation.

Python Encapsulation
Python relies on programming conventions to indicate the intended use of something. 
These conventions are based on naming. 
There is a general attitude that it is up to the programmer to observe the rules 
as opposed to having the language enforce them.
"""

# 1 private attributes
# Any attribute name with leading _ is considered to be private.
class Person(object):
    def __init__(self, name) -> None:
        self._name = name
# As mentioned earlier, this is only a programming style. You can still access and change it.
p = Person('Guido')
print(p._name)
p._name = 'Larry'
print(p._name)
# As a general rule, any name with a leading _ is considered internal implementation whether 
# it’s a variable, a function, or a module name. 
# If you find yourself using such names directly, you’re probably doing something wrong. 
# Look for higher level functionality.

# 2 simple attributes
class Stock1:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
# A surprising feature is that you can set the attributes to any value at all:
s = Stock1('ACME', 50, 91.1)
s.shares = 75
s.shares = '50'
s.shares = [1, 2, 3]
# You might look at that and think you want some extra checks. e.g., raise a TypeError

# 3 managed attributes
# One approach: introduce accessor methods.
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price
    def get_shares(self):
        return self._shares
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('shares must be an integer')
        if value < 0:
            raise ValueError('shares must be positive')
        self._shares = value

# Another approach: use properties.
# Normal attribute access now triggers the getter and setter methods under @property and @shares.setter.
# With this pattern, there are no changes needed to the source code. 
# The new setter is also called when there is an assignment within the class, including inside the __init__() method.
class Stock3(object):
    def __init__(self, name, shares, price):
        self.name = name
        # this assignment triggers the setter below
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('shares must be an integer')
        if value < 0:
            raise ValueError('shares must be positive')
        self._shares = value
    
    # There is often a confusion between a property and the use of private names. 
    # Although a property internally uses a private name like _shares, 
    # the rest of the class (not the property) can continue to use a name like shares.
    # This allows you to drop the extra parantheses, hiding the fact that it’s actually a method:
    @property
    def cost(self):
        return self.shares * self.price

s = Stock3('ACME', 50, 91.1)
print(s.shares)  # triggers the getter @property
s.shares = 75  # triggers the setter @shares.setter
print(s.cost)


# 4 uniform access
# how to put a more uniform interface on an object. 
# If you don’t do this, an object might be confusing to use:
s = Stock2('ACME', 50, 91.1)
a = s.get_shares()
b = s.price
# Why is the () required for the get_shares, but not for the price? A property can fix this.

# Decorator Syntax
# The @ syntax is known as “decoration”. 
# It specifies a modifier that’s applied to the function definition that immediately follows.
"""
...
@property
def cost(self):
    return self.shares * self.price
"""

# __slots__ Attribute
# You can restrict the set of attributes names.
class Stock4:
    __slots__ = ('name','shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
# It will raise an error for other attributes.
s = Stock4('ACME', 50, 91.1)
s.price
try:
    s.prices
except AttributeError as e:
    print(e)
# Although this prevents errors and restricts usage of objects, 
# it’s actually used for performance and makes Python use memory more efficiently.


# 5.1 exec: simple properties
# Properties are a useful way to add “computed attributes” to an object.
# You can get rid of the extra () on cost() if you turn it into a property. 
# Take your Stock class and modify it so that the cost calculation works like this:
# s.cost

# Try calling s.cost() as a function and observe that it doesn’t work now that 
# cost has been defined as a property.


# 5.2 exec: properties and setters
# Modify the shares attribute so that the value is stored in a private attribute and 
# that a pair of property functions are used to ensure that it is always set to an integer value. 

# 5.3 exec: adding slots
# Modify the Stock class so that it has a __slots__ attribute. 
# Then, verify that new attributes can’t be added.
# When you use __slots__, Python uses a more efficient internal representation of objects. 
# What happens if you try to inspect the underlying dictionary of s above?
try:
    print(s.__dict__)
except AttributeError as e:
    print(e)
"""
It should be noted that __slots__ is most commonly used as an optimization on classes that serve as data structures. 
Using slots will make such programs use far-less memory and run a bit faster. 
You should probably avoid __slots__ on most other classes however.
"""
