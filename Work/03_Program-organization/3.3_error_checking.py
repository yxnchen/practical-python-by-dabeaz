# 1 how program fails
# Python performs no checking or validation of function argument types or values. 
# A function will work on any data that is compatible with the statements in the function.
def add(x, y):
    return x + y

print(add(3,4))
print(add('hello', 'world'))
print(add('3', '4'))

# If there are errors in a function, they appear at run time (as an exception).
# print(add(3, '4'))

# 2 exceptions
"""
- To raise an exception yourself, use raise statement.
- To catch an exception use try-except.
"""

# 3 exception handling
# Exceptions propagate to the first matching except.
# 1To handle the exception, put statements in the except block.
# 2After handling, execution resumes with the first statement after the try-except.
def grok():
    raise RuntimeError('Whoops!')  # exception raised here

def spam():
    grok()  # call grok() will raise an exception
    
def bar():
    try:
        spam()  
    except RuntimeError as e:
        print('Caught an error at bar() saying: ', e)  # exception caught here
        # handle here
    print("resume execution.")
        
def foo():
    try:
        bar()
    except RuntimeError as e:
        print('Caught an error at foo() saying: ', e)  # exception NOT caught here
        
foo()

# 4 built-in exceptions
"""
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
"""

# 5 Exception Values
# Exceptions have an associated value. It contains more specific information about what’s wrong.
# raise RuntimeError('Invalid user name')

# This value is part of the exception instance that’s placed in the variable supplied to except.
# except RuntimeError as e:   # `e` holds the exception raised

# e is an instance of the exception type. However, it often looks like a string when printed.


# 6 catching multiple exceptions
# You can catch different kinds of exceptions using multiple except blocks.
"""
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...

# or if the statements to handle them is the same, you can group them:

try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
"""

# 7 catching all exceptions
"""
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
    
# If you’re going to catch all errors, this is a more sane approach.

try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
"""

# 8 re-raising exceptions
# Use raise to propagate a caught error.
"""
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
"""
# This allows you to take action (e.g. logging) and pass the error on to the caller.


# 9 exception best practices
# finally statement
"""
It specifies code that must run regardless of whether or not an exception occurs.
Commonly used to safely manage resources (especially locks, files, etc.).

lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
"""
# with statement
"""
In modern code, try-finally is often replaced with the with statement.
'with' defines a usage context for a resource. 
When execution leaves that context, resources are released. 
'with' only works with certain objects that have been specifically programmed to support it.

with open(filename) as f:
    # Use the file
    ...
# File closed
"""


# 10.1 exec: 
# The parse_csv() function you wrote in the last section allows user-specified columns to be selected, 
# but that only works if the input data file has column headers.
# see fileparse.py

# This indicates a programming error on the part of the calling code. 
# Checking for cases that “aren’t supposed to happen” is often a good idea.

# 10.2 exec: 
# file with missing value or so
# see fileparse.py

# 10.3 exec: silencing errors
# Modify the parse_csv() function so that parsing error messages 
# can be silenced if explicitly desired by the user.
# see fileparse.py
