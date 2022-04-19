# 1 calling a function
from re import X


def read_prices(filename, debug):
    print(f'Calling read_prices({filename}, {debug})')

# call the function with positional arguments
read_prices('prices.csv', False)
# call the function with keyword arguments
read_prices(filename='prices.csv', debug=False)

# 2 default arguments
# Arguments with defaults must appear at the end of the arguments list 
# (all non-optional arguments go first).
def read_prices(filename, debug=False):
    print(f'Calling read_prices({filename}, [{debug}])')
read_prices('prices.csv')
read_prices('prices.csv', True)

# 3 prefer keyword arguments for optional arguments
# In most cases, keyword arguments improve code clarity–especially for arguments 
# that serve as flags or which are related to optional features.

# 4 design best practices
# always give short, but meaningful names to functions arguments

# 5 returning values
# If no return value is given or return is missing, None is returned.
def bar(x):
    return
a = bar(42)
print(a)

def foo(x):
    pass
b = foo(42)
print(b)

# 6 multiple return values
# Functions can only return one value. 
# However, a function may return multiple values by returning them in a tuple.
def divide(a, b):
    return a // b, a % b

x, y = divide(42, 8)
x = divide(42, 9)
print(x)  # tuple

# 7 variable scope
# Variables defined outside are “global”. Variables inside a function are “local”.
value = 10
x = value  # global variable
def foo():
    y = value  # local variable
    
# 8 local variables
# Variables assigned inside functions are private.

# 9 global variables
# Functions can freely access the values of globals defined in the same file.
name = 'David'
def greeting():
    print(f'Hello, {name}')
    
greeting()
# However, functions can’t modify globals:
def spam():
    name = 'Spam'
spam()
print(name)

# 10 modifying globals
# If you must modify a global variable you must declare it as such.
def spam():
    global name
    name = 'Spam'
spam()
print(name)
# The global declaration must appear before its use and the corresponding variable must exist in the same file as the function. 
# Having seen this, know that it is considered poor form. In fact, try to avoid global entirely if you can. 
# If you need a function to modify some kind of state outside of the function, it’s better to use a class instead (more on this later).

# 11 arguments passing
"""
When you call a function, the argument variables are names that refer to the passed values. 
These values are NOT copies (see section 2.7). 
If mutable data types are passed (e.g. lists, dicts), they can be modified in-place.

Key point: Functions don’t receive a copy of the input arguments.
"""
def foo(items):
    items.append(42)
a = [1, 2, 3]
foo(a)
print(a)

# 12 reassignment vs modifying
# understand the subtle difference between modifying a value and reassigning a variable name.
def foo(items):
    items.append(42)  # modifies the input object
a = [1, 2, 3]
foo(a)
print(a)

def bar(items):
    items = [4, 5, 6]  # changes local variable 'items' to point to a new object
b = [1, 2, 3]
bar(b)
print(b)
"""Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value."""

# 13 exec: see Work/fileparse.py
