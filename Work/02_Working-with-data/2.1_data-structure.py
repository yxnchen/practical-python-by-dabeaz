# 1 None type
# None is often used as a placeholder for optional or missing value. 
# It evaluates as False in conditionals.
from re import S


email_addr = None
if email_addr:
    print(email_addr)
    
# 2 Tuples
# A tuple is a collection of values grouped together.
t = ('GOOG', 100, 490.1)
# Sometimes the () are omitted in the syntax.
t = "GOOG", 100, 490.1
# empty tuple
te = ()
# 1-item tuple
t1 = ('GOOG',)
# Tuple contents are ordered (like an array).
name, shares, price = t[0], t[1], t[2]
print(name, shares, price)
# tuple contents can bot be modified
try:
    t[0] = 'dede'
except TypeError:
    print('tuple is immutable')
# tuple packing
s = ('GOOG', 100, 490.1)
# tuple unpacking: The number of variables on the left must match the tuple structure.
name, shares, price = s
# tuples vs. lists
# Tuples look like read-only lists. However, tuples are most often used for a single item consisting of multiple parts. 
# Lists are usually a collection of distinct items, usually all of the same type.
record = ('GOOG', 100, 490.1)
symbol = ['GOOG', 'AAPL', 'MSFT']

# 3 Dictionaries
d = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
d['date'] = '09/11/2016'
# delete a value
del d['date']
print(d)

# 4.1 exec: using tuples
import csv
f = open('./Work/data/portfolio.csv')
rows = csv.reader(f)
print(next(rows))
row = next(rows)
t = (row[0], int(row[1]), float(row[2]))
print(t)
print('cost: ', t[1] * t[2])
name, shares, price = t
t = (name, shares*2, price)
print(t)

# 4.2 exec: using dictionaries
d = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
print(d)
print('cost: ', d['shares'] * d['price'])
d['shares'] = 75
print(d)

# 4.3 exec: additional dictionary operations
# If you turn a dictionary into a list, you’ll get all of its keys:
print(list(d))
# Similarly, if you use the for statement to iterate on a dictionary, you will get the keys:
for k in d:
    print('key = ', k)
# lookup at the same tiem
for k in d:
    print(k, ' = ', d[k])
# get all of the keys
# keys() is a bit unusual in that it returns a special dict_keys object.
# This is an overlay on the original dictionary that always gives you the current keys—even if the dictionary changes
ks = d.keys()
print(ks)
del d['price']
print(ks)
# using item() method
print(d.items())
for k, v in d.items():
    print(k, ' = ', v)

# 4.4 exec: tuple and dictionary conversion
# If you have tuples such as items, you can create a dictionary using the dict() function. 
items = d.items()
print(items)
d1 = dict(items)
print(d1)
