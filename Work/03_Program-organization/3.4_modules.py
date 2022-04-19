"""
Any Python source file is a module.

The import statement loads and executes a module.

A module is a collection of named values and is sometimes said to be a namespace.

The names are all of the global variables and functions defined in the source file. 
After importing, the module name is used as a prefix. Hence the namespace.

The module name is directly tied to the file name (foo -> foo.py).

Modules are isolated.

When a module is imported, all of the statements in the module execute one after 
another until the end of the file is reached. 

If there are scripting statements that carry out tasks in the global scope 
(printing, creating files, etc.) you will see them run on import.
"""

# 1 import as statement
# You can change the name of a module as you import it:
import math as m
def retangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y

# 2 from module import
# This picks selected symbols out of a module and makes them available locally.
from math import sin, cos
def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y

# 3 commnets on import
"""
import math
# vs
import math as m
# vs
from math import cos, sin
"""
# import always executes the entire file and modules are still isolated environments.
# The import module as statement is only changing the name locally. 
# The from math import cos, sin statement still loads the entire math module behind the scenes. 
# It’s merely copying the cos and sin names from the module into the local space after it’s done.


# 4 module loading
# Each module loads and executes only once. 
# Note: Repeated imports just return a reference to the previously loaded module.
import sys
print(sys.modules.keys())
# sys.modules is a dict of all loaded modules.
"""The safest way to load modified code into Python is to quit and restart the interpreter."""


# 5 locating modules
# Python consults a path list (sys.path) when looking for modules.
# The current working directory is usually first.
print(sys.path)

# 6 module search path
# As noted, sys.path contains the search paths. You can manually adjust if you need to.
sys.path.append('.//somewhere')
# Paths can also be added via environment variables.
"""
% env PYTHONPATH=/project/foo/pyfiles python3
"""

# 7.1 exec: module imports
sys.path.append('./Work')
import fileparse
# help(fileparse)
print()
pf = fileparse.parse_csv('./Work/Data/portfolio.csv', select=['name', 'shares', 'price'], 
                         types=[str, int, float])
print(pf)

from fileparse import parse_csv
print()
pf = parse_csv('./Work/Data/portfolio.csv', select=['name', 'shares', 'price'], 
                         types=[str, int, float])
print(pf)


# 7.2 exec: using your library module
# report.py -> import fileparse
# pcost.py -> import report
