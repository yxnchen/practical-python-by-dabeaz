"""
In many programming languages, there is a concept of a main function or method.

Python has no main function or method. Instead, there is a main module. 
The main module is the source file that runs first.
% python3 prog.py

Whatever file you give to the interpreter at startup becomes main. It doesn’t matter the name.
"""

# 1 __main__ check
# It is standard practice for modules that run as a main script to use this convention:
"""
if __name__ == '__main__':
    statements
"""
# Statements enclosed inside the if statement become the main program.

# 2 Main programs vs. library imports
# Any Python file can either run as main or as a library import:
# In both cases, __name__ is the name of the module. 
# However, it will only be set to __main__ if running as main.
# Usually, you don’t want statements that are part of the main program to execute on a library import. 
# So, it’s common to have an if-check in code that might be used either way.
"""
if __name__ == '__main__':
    # Does not execute if loaded with import ...
"""

# 3 program template
# Here is a common program template for writing a Python program:
"""
# Import statements (libraries)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main():
    ...

if __name__ == '__main__':
    main()
"""

# 4 command line tools
# The command line is a list of text strings.
# % python3 report.py portfolio.csv prices.csv
# This list of text strings is found in sys.argv.
# sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']

# a simple example of processing the arguments
import sys
if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]}' ' portfoliofile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]


# 5 standard I/O
# Standard Input / Output (or stdio) are files that work the same as normal files.
"""
sys.stdout
sys.stderr
sys.stdin

By default, print is directed to sys.stdout. 
Input is read from sys.stdin. 
Tracebacks and errors are directed to sys.stderr.
"""
# Be aware that stdio could be connected to terminals, files, pipes, etc.
# % python3 prog.py > results.txt
# % cmd1 | python3 prog.py | cmd2

# 6 environment variables
# Environment variables are set in the shell.
# % setenv NAME dave
# % setenv RSH ssh
# % python3 prog.py

# os.environ is a dictionary that contains these values.
import os
name = os.environ['NAME']


# 7 program exit
# Program exit is handled through exceptions.
"""
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
"""
# An alternative. A non-zero exit code indicates an error.
"""
import sys
sys.exit(exitcode)
"""

# 8 the #! line
# On Unix, the #! line can launch a script as Python. 
# Add the following to the first line of your script file.
"""
#!/usr/bin/env python3
# prog.py
...
"""
# It requires the executable permission.
# % chmod +x prog.py


# 9 script template
"""
#!/usr/bin/env python3
# prog.py

# Import statements (libraries)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
"""

# 10.1 exec: Making Scripts
# Modify the report.py and pcost.py programs so that they can execute as a script on the command line:
