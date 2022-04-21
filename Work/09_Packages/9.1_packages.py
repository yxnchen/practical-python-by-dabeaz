"""
Packages

If writing a larger program, you don’t really want to organize it as a large of collection of standalone files at the top level. 
This section introduces the concept of a package.
"""

# 1 modules
# Any Python source file is a module.
# An import statement loads and executes a module.

# 2 packages vs. modules
# For larger collections of code, it is common to organize modules into a package.
"""
# From this
pcost.py
report.py
fileparse.py

# To this
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
"""
# You pick a name and make a top-level directory. 
# porty in the example above (clearly picking this name is the most important first step).

# Add an __init__.py file to the directory. It may be empty.
# Put your source files into the directory.

# 3 using a package
# A package serves as a namespace for imports.
# This means that there are now multilevel imports.
"""
import porty.report
port = porty.report.read_portfolio('port.csv')
"""
# There are other variations of import statements.
"""
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
"""

# 4 two problems
"""
There are two main problems with this approach.

- imports between files in the same package break.
- Main scripts placed inside the package break.

So, basically everything breaks. But, other than that, it works.
"""

# 4.1 problem with imports
# Imports between files in the same package must now include the package name in the import. 
"""
# report.py
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
"""
# All imports are absolute, not relative.

# 4.2 relative imports
# Instead of directly using the package name, you can use . to refer to the current package.
"""
# report.py
from . import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
"""
# This makes it easy to rename the package.

# 4.3 problem with main scripts
# Running a package submodule as a main script breaks.
"""
bash $ python porty/pcost.py # BREAKS
"""
# Reason: You are running Python on a single file and 
# Python doesn’t see the rest of the package structure correctly (sys.path is wrong).

# All imports break. To fix this, you need to run your program in a different way, using the -m option.
"""
bash $ python -m porty.pcost # WORKS
"""

# 5 __init__.py files
# The primary purpose of these files is to stitch modules together.
"""
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
"""
# This makes names appear at the top-level when importing.
"""
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
"""
# Instead of using the multilevel imports.
"""
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
"""

# 6 Another solution for scripts
# As noted, you now need to use -m package.module to run scripts within your package.
"""
bash % python3 -m porty.pcost portfolio.csv
"""
# There is another alternative: Write a new top-level script.
# This script lives outside the package.
"""
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
"""

# 7 application structure
# Code organization and file structure is key to the maintainability of an application.
# There is no “one-size fits all” approach for Python. 
# However, one structure that works for a lot of problems is something like this.
"""
porty-app/
  README.md
  script.py         # SCRIPT
  porty/
    # LIBRARY CODE
    __init__.py
    pcost.py
    report.py
    fileparse.py
"""
# The top-level porty-app is a container for everything else–documentation, top-level scripts, examples, etc.
# Again, top-level scripts (if any) need to exist outside the code package. One level up.
"""
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
"""

# 8.1 8.2 8.3 exec: 
# - Making a simple package
# - Making an application directory
# - Top-level Scripts
