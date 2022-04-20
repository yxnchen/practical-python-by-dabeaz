"""
User defined exceptions are defined by classes.

class NetworkError(Exception):
    pass
    
- Exceptions always inherit from Exception.
- Usually they are empty classes. Use pass for the body.

You can also make a hierarchy of your exceptions.

class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
"""

# 1.1 exec: defining a custom exception
# It is often good practice for libraries to define their own exceptions.
# This makes it easier to distinguish between Python exceptions raised in response to common programming errors 
# versus exceptions intentionally raised by a library to a signal a specific usage problem.

# Modify the create_formatter() function from the last exercise so that it raises a custom FormatError exception 
# when the user provides a bad format name.
from tableformat import create_formatter
create_formatter('xls')
