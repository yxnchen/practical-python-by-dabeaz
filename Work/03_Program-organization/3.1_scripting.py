"""
A script is a program that runs a series of statements and stops.
"""

# 1 defining things
# Names must always be defined before they get used later.
def square(x):
    """
    Returns the square of a number.
    """
    return x * x

a = 42
z = square(a)

# 2 defining functions
# It is a good idea to put all of the code related to a single task all in one place. 
# A function is a named sequence of statements.
# Any Python statement can be used inside.
def foo():
    import math
    print(math.sqrt(2))
    help(math)

# Functions can be defined in any order.
# Functions must only be defined prior to actually being called during program execution.

# bottom-up style function definition: Later functions build upon earlier functions. 
def foo(x):
    pass

def bar(x):
    foo(x)

def spam(x):
    bar(x)

spam(42)

# 3 function design
# 3.1 Doc strings:
# Doc-strings are strings written immediately after the name of the function. 
# They feed help(), IDEs and other tools.
def read_prices(filename):
    """Read prices from a CSV file of name, price data

    Args:
        filename (str): CSV file
    """
    pass
# 3.2 type annotations:
# The hints do nothing operationally. They are purely informational. 
# However, they may be used by IDEs, code checkers, and other tools to do more.
def read_prices_2(filename: str) -> dict:
    pass

# 4.1 exec: modified report.py
# Create a function print_report(report) that prints out the report.
# Change the last part of the program so that it is nothing more than a series of function calls and no other computation.

# Creating a top-level function for program execution