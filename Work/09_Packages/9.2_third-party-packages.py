"""
Third Party Modules

Python has a large library of built-in modules (batteries included).

There are even more third party modules. Check them in the Python Package Index or PyPi. 
Or just do a Google search for a specific topic.

How to handle third-party dependencies is an ever-evolving topic with Python. 
This section merely covers the basics to help you wrap your brain around how it works.
"""

# 1 the module search path
# sys.path is a directory that contains the list of all directories checked by the import statement.
import sys
for p in sys.path:
    print(p)
# If you import something and it’s not located in one of those directories, 
# you will get an ImportError exception.


# 2 standard library modules
# Modules from Python’s standard library usually come from a location such as `/usr/local/lib/python3.6’. 
# You can find out for certain by trying a short test:
import re
print(re)


# 3 third party modules
# Third party modules are usually located in a dedicated site-packages directory. 
# You’ll see it if you perform the same steps as above:
import numpy
print(numpy)


# 4 installing modules
# The most common technique for installing a third-party module is to use pip.
"""
bash % python3 -m pip install packagename
"""
# This command will download the package and install it in the site-packages directory.

# 5 problems
"""
- You may be using an installation of Python that you don’t directly control.
    > A corporate approved installation
    > You’re using the Python version that comes with the OS.
- You might not have permission to install global packages in the computer.
- There might be other dependencies.
"""

# 6 virtual environments
# A common solution to package installation issues is to create a so-called “virtual environment” for yourself. 
# Naturally, there is no “one way” to do this–in fact, there are several competing tools and techniques. 
# However, if you are using a standard Python installation, you can try typing this:
"""
bash % python -m venv mypython
"""
# After a few moments of waiting, you will have a new directory 'mypython' that’s your own little Python install. 
# Within that directory you’ll find a bin/ directory (Unix) or a Scripts/ directory (Windows). 
# If you run the activate script found there, it will “activate” this version of Python, 
# making it the default python command for the shell. For example:
"""
bash % source mypython/bin/activate
"""
# From here, you can now start installing Python packages for yourself. For example:
"""
(mypython) bash % python -m pip install pandas
"""

# 7 Handling Third-Party Dependencies in Your Application
# If you have written an application and it has specific third-party dependencies, 
# one challenge concerns the creation and preservation of the environment that includes your code 
# and the dependencies. Sadly, this has been an area of great confusion and frequent change over 
# Python’s lifetime. It continues to evolve even now.

# Python Packaging User Guide: https://packaging.python.org/


# 8.1 exec: Creating a Virtual Environment
