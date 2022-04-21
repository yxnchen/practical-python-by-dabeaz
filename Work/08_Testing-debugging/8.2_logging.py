"""
'logging' Module

The logging module is a standard library module for recording diagnostic information. 
It’s also a very large module with a lot of sophisticated functionality. 
We will show a simple example to illustrate its usefulness.
"""

# 1 exceptions revisited
# In the exercises, we wrote a function parse() that looked something like this:
"""
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
"""
# What should you do in the except block?
# - Should you print a warning message?
# - Or do you silently ignore it?
# Neither solution is satisfactory because you often want both behaviors (user selectable).

# 2 using logging
"""
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
    ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("Couldn't parse : %s", line)
        log.debug("Reason : %s", e)
"""
# The code is modified to issue warning messages or a special Logger object. 
# The one created with logging.getLogger(__name__).

# 3 logging basics
import logging
# create a logger object
name = __name__
log = logging.getLogger(name)  # name is a string
# issuing log messages
"""
# Each method represents a different level of severity.

log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])

# All of them create a formatted log message. args is used with the % operator to create the message.
logmsg = message % args # Written to the log
"""
log.critical("Critical message")


# 4 logging configuration
# The logging behavior is configured separately.
"""
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Log output file
        level     = logging.INFO,   # Output level
    )
"""
# Typically, this is a one-time configuration at program startup. 
# The configuration is separate from the code that makes the logging calls.


# 5.1 exec: Adding logging to a module
# In fileparse.py, there is some error handling related to exceptions caused by bad input.
"""
...
print(f"Row {rowno}: Couldn't convert {row}")
print(f"Row {rowno}: Reason {e}")
...
"""
# Replacing those prints with logging operations is relatively simple.
"""
...
log.warning("Row %d: Couldn't convert %s", rowno, row)
log.debug("Row %d: Reason %s", rowno, e)
...
"""

# If you do nothing, you’ll only get logging messages for the WARNING level and above. 
# The output will look like simple print statements. 
# However, if you configure the logging module, you’ll get additional information about the logging levels, module, and more. 
# Type these steps to see that:
"""
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
"""
# You will notice that you don’t see the output from the log.debug() operation. 
# Type this to change the level.
"""
>>> logging.getLogger('fileparse').level = logging.DEBUG
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
DEBUG:fileparse:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
DEBUG:fileparse:Row 7: Reason: invalid literal for int() with base 10: ''
"""
# Turn off all, but the most critical logging messages:
"""
>>> logging.getLogger('fileparse').level=logging.CRITICAL
>>> a = report.read_portfolio('Data/missing.csv')
"""

# 5.2 exec: Adding logging to a program
# To add logging to an application, you need to have some mechanism to initialize the logging module 
# in the main module. One way to do this is to include some setup code that looks like this:
"""
# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
"""
# Again, you’d need to put this someplace in the startup steps of your program.
