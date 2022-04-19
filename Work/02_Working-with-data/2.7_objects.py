"""
This section introduces more details about Python’s internal object model and 
discusses some matters related to memory management, copying, and type checking.
"""

# 1 assignment
# Many operations in Python are related to assigning or storing values.
value = 1
a = value
s = [2]; s[0] = value
s.append(value)
d = {}; d['key'] = value
"""
A caution: assignment operations never make a copy of the value being assigned. 
All assignments are merely reference copies (or pointer copies if you prefer).
"""
a = [1, 2, 3]
b = a
c = [a, b]
# there is only one list object [1,2,3], but there are four different references to it.
a.append(999)
print(a)
print(b)
print(c)

# 2 reassigning values
# Reassigning a value never overwrites the memory used by the previous value.
"""Remember: Variables are names, not memory locations."""
a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(a)
print(b)
 
# 3 identity and references
# Use the is operator to check if two values are exactly the same object.
a = [1, 2, 3]
b = a
print('a is b: ', a is b) 
# is compares the object identity (an integer). The identity can be obtained using id().
print('a id: ', id(a), 'b id: ', id(b))
# It is almost always better to use == for checking objects. 
# The behavior of is is often unexpected:
c = [1, 2, 3]
print('a is c: ', a is c)
print('a == c: ', a == c)

# 4 shallow copies
"""Lists and dicts have methods for copying."""
a = ['a', [2, 4], 3]
b = list(a)  # make a copy
print('a is b: ', a is b)
# but the list items are shared
a[1].append(5)
print(b)
print('a[1] is b[1]: ', a[1] is b[1])

# 5 deep copies
"""need to make a copy of an object and all the objects contained within it"""
a = ['a', [2, 4], 3]
import copy
b = copy.deepcopy(a)
a[1].append(5)
print(b)
print('a[1] is b[1]: ', a[1] is b[1])

# 6 Names, Values and Types
# Variable names do not have a type. It’s only a name. However, values do have an underlying type.
a = 42
b = 'spam'
print('type(a): ', type(a))
print('type(b): ', type(b))
# type checking
if isinstance(a, list):
    print('a is a list')
if isinstance(b, (str, list, tuple)):
    print('b is a string or a list or a tuple')

# 7 everything is an object
"""
Numbers, strings, lists, functions, exceptions, classes, instances, etc. are all objects. 
It means that all objects that can be named can be passed around as data, placed in containers, etc., without any restrictions. 
There are no special kinds of objects. 
Sometimes it is said that all objects are “first-class”.
"""
import math
items = [abs, math, ValueError]
print(items)
print(items[0](-42))
print(items[1].sqrt(2))
try:
    x = int('NaN')
except items[2]:
    print('Caught a ValueError')

# 8.1 exec: first-class data
# Make a Python list that contains the names of the conversion functions you would use to 
# convert each column into the appropriate type:
types = [str, int, float]
import csv
f = open('./Work/Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
print(types[1](row[1]))
print(types[2](row[2]))
print(types[1](row[1]) * types[2](row[2]))
r = list(zip(types, row))
print(r)
converted = []
for func, val in zip(types, row):
    converted.append(func(val))
print(converted)
print(converted[1] * converted[2])

# 8.2 exec: making dictionaries
headers = ['name', 'shares', 'price']
d = dict(zip(headers, converted))
print(d)
print({name: func(val) for name, func, val in zip(headers, types, row)})

# 8.3 exec: the big picture
f = open('./Work/Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(headers)
print(row)
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)
print(record['name'])
print(record['price'])

def mydate(s):
    month, day, year = s.split('/')
    return (int(month), int(day), int(year))
types = [str, float, mydate, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)
print(record['date'])
