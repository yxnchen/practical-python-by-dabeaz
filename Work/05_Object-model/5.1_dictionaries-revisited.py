"""
This section covers some of the inner workings of Python objects. 
Programmers coming from other programming languages often find Python’s notion of classes lacking in features. 
For example, there is no notion of access-control (e.g., private, protected), the whole self argument feels weird, 
and frankly, working with objects sometimes feel like a “free for all.” 
Maybe that’s true, but we’ll find out how it all works as well as some common programming idioms to better encapsulate the internals of objects.
"""

# The Python object system is largely based on an implementation involving dictionaries.
# Dictionaries are commonly used for simple data structures. 
# However, they are used for critical parts of the interpreter and may be the most important type of data in Python.

# 1 dicts and modules
# Within a module, a dictionary holds all of the global variables and functions.
# If you inspect foo.__dict__ or globals(), you’ll see the dictionary.
import foo
print(foo.__dict__)

# 2 dicts and objects
# User defined objects also use dictionaries for both instance data and classes. 
# In fact, the entire object system is mostly an extra layer that’s put on top of dictionaries.
# Each instance gets its own private dictionary.
import sys
sys.path.append('./Work/04_Classes-and-Objects')
from stock import Stock
s = Stock('ACME', 100, 123.45)
print(s.__dict__)

# 3 class members
# A separate dictionary also holds the methods.
print(Stock.__dict__)

# 4 instances and classes
# Instances and classes are linked together. The __class__ attribute refers back to the class.
print(s.__class__)
# The instance dictionary holds data unique to each instance, 
# whereas the class dictionary holds data collectively shared by all instances.

# 5 attribute access
# When you work with objects, you access data and methods using the . operator.
"""
x = obj.name          # Getting
obj.name = value      # Setting
del obj.name          # Deleting
"""
# These operations are directly tied to the dictionaries sitting underneath the covers.

# 6 modifying instances
# Operations that modify an object update the underlying dictionary.
s.shares = 50
s.date = '12/17/2012'
print(s.__dict__)

# 7 reading attributes
# Suppose you read an attribute on an instance. The attribute may exist in two places:
# - Local instance dictionary. (check in local __dict__)
# - Class dictionary.  (If not found, look in __dict__ of class through __class__)


# 8 how inheritance works
# Classes may inherit from other classes.
class A:
    pass
class B:
    pass
class C(A, B):
    pass
# The base classes are stored in a tuple in each class. This provides a link to parent classes.
print(C.__bases__)


# 9 reading attributes with inheritance
"""
Logically, the process of finding an attribute is as follows. 
- First, check in local __dict__. 
- If not found, look in __dict__ of the class. 
- If not found in class, look in the base classes through __bases__. 
However, there are some subtle aspects of this discussed next.
"""
# 9.1 reading attributes with single inheritance
# In inheritance hierarchies, attributes are found by walking up the inheritance tree in order.
# With single inheritance, there is a single path to the top. You stop with the first match.
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass

# 9.2 method resolution order (MRO)
# Python precomputes an inheritance chain and stores it in the MRO attribute on the class.
# To find an attribute, Python walks the MRO in order. The first match wins.
print(E.__mro__)

# 9.3 MRO in Multiple Inheritance
# With multiple inheritance, there is no single path to the top.
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
# Python uses *cooperative multiple inheritance* which obeys some rules about class ordering.
# - Children are always checked before parents
# - Parents (if multiple) are always checked in the order listed.
# The MRO is computed by sorting all of the classes in a hierarchy according to those rules.
# The underlying algorithm is called the “C3 Linearization Algorithm.”
print(E.__mro__)

# 9.4 An Odd Code Reuse (Involving Multiple Inheritance)
# Consider two completely unrelated objects:
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
# and
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
# There is a code commonality in the implementation of LoudDog.noise() and LoudBike.noise(). 
# In fact, the code is exactly the same.
# The Mixin pattern is a class with a fragment of code.
class Loud:
    def noise(self):
        return super().noise().upper()
# This class is not usable in isolation. It mixes with other classes via inheritance.
class LoudDog(Loud, Dog):
    pass
class LoudBike(Loud, Bike):
    pass
# Miraculously, loudness was now implemented just once and reused in two completely unrelated classes. 
# This sort of trick is one of the primary uses of multiple inheritance in Python.

# 9.5 why super()
# Always use super() when overriding methods.
# super() delegates to the next class on the MRO.


# 10.1 exec: Representation of Instances
goog = Stock('GOOG', 100, 490.1)
ibm = Stock('IBM', 100, 91.1)
print(goog.__dict__)
print(ibm.__dict__)

# 10.2 exec: modifying of instance data
# the attributes of an instance are not limited to those set up in the __init__() method.
goog.date = '12/17/2012'
print(goog.__dict__)
# try placing a new value directly into the __dict__ object:
goog.__dict__['time'] = '9:45am'
print(goog.time)
# Note: it should be emphasized that direct manipulation of the dictionary is uncommon,
# you should always write your code to use the (.) syntax.

# 10.3 exec: the role of classes
# The definitions that make up a class definition are shared by all instances of that class. 
# Notice, that all instances have a link back to their associated class:
print(goog.__class__)
print(ibm.__class__)
# Notice that the name ‘cost’ is not defined in either goog.__dict__ or ibm.__dict__. 
# Instead, it is being supplied by the class dictionary.
print(goog.cost())
print(Stock.__dict__['cost'])
# Notice how the self argument gets the instance.
print(Stock.__dict__['cost'](goog))
print(Stock.__dict__['cost'](ibm))
# try adding a new attribute to the class:
Stock.foo = 42
# Notice how this new attribute now shows up on all of the instances:
print(goog.foo)
print(ibm.foo)
# However, notice that it is not part of the instance dictionary:
print(goog.__dict__.get('foo'))
# The reason you can access the foo attribute on instances is that 
# Python always checks the class dictionary if it can’t find something on the instance itself.
# Note: This part illustrates something known as a class variable. 
# Suppose, for instance, you have a class like this:
class Foo(object):
     a = 13                  # Class variable (is shared by all of the instances that get created)
     def __init__(self,b):
         self.b = b          # Instance variable
f = Foo(10)
g = Foo(20)
print(f.a, g.a)
print(f.b, g.b)
Foo.a = 40
print(f.a, g.a)


# 10.4 exec: bound methods
# A subtle feature of Python is that invoking a method actually involves two steps 
# and something known as a bound method.
s = goog.sell
print(s)
s(25)
print(goog.shares)
# Bound methods actually contain all of the pieces needed to call a method. 
# For instance, they keep a record of the function implementing the method:
print(s.__func__)
# This is the same value as found in the Stock dictionary.
print(Stock.__dict__['sell'])
# Bound methods also record the instance, which is the self argument.
print(s.__self__)
# When you invoke the function using () all of the pieces come together.
s.__func__(s.__self__, 25)  # same as s(25)
print(goog.shares)


# 10.5 exec: inheritance
# Make a new class that inherits from Stock.
class NewStock(Stock):
    def yow(self):
        print('Yow!')
        
n = NewStock('N', 100, 490.1)
print(n.cost())
n.yow()
# Inheritance is implemented by extending the search process for attributes. 
# The __bases__ attribute has a tuple of the immediate parents:
print(NewStock.__bases__)
# The __mro__ attribute has a tuple of all parents, in the order that they will be searched for attributes.
print(NewStock.__mro__)
# Here’s how the cost() method of instance n above would be found:
for cls in n.__class__.__mro__:
    if 'cost' in cls.__dict__:
        print(cls)
        print(cls.__dict__['cost'])
        break

