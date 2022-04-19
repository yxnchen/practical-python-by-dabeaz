"""
Python has three sequence datatypes.

- String: 'Hello'. A string is a sequence of characters.
- List: [1, 4, 5].
- Tuple: ('GOOG', 100, 490.1).
All sequences are ordered, indexed by integers, and have a length.
"""

a = 'string'
b = [1, 2, 3]
c = ('GOOG', 100, 490.1)
print(a[0])
print(b[-1])
print(c[1])
print(len(a))
print(len(b))
print(len(c))

# 1 sequences can be replicated using the * operator.
print(a * 3)
print(b * 2)
print(c * 2)

# 2 sequences of the same type can be concatenated using the + operator.
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)
c = [1, 2]
try:
    print(a + c)
except TypeError:
    print('TypeError: can only concatenate list (not "tuple") to list')
    
# 3 slicing
# Slicing means to take a subsequence from a sequence. The syntax is s[start:end]. 
# Where start and end are the indexes of the subsequence you want.
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:5])
print(a[-5:])
print(a[:3])

# 4 slice re-assignment
# On lists, slices can be reassigned and deleted.
# The reassigned slice doesn’t need to have the same length.
a[2:4] = [10, 11, 12]
print(a)
del a[2:4]
print(a)

# 5 sequence reductions
# There are some common functions to reduce a sequence to a single value.
s = [1,2,3,4]
print(sum(s))
print(min(s))
print(max(s))
t = ['hello', 'world']
print(max(t))

# 6 enumerate function
# The enumerate function adds an extra counter value to iteration.
names = ['Alice', 'Bob', 'Cathy', 'Doug']
for i, name in enumerate(names):
    print(i, name)
# The general form is enumerate(sequence [, start = 0]). start is optional. 
# A good example of using enumerate() is tracking line numbers while reading a file:
with open('./Work/Data/portfolio.csv') as f:
    for i, line in enumerate(f, 1):
        print(i, line, end='')
        
# 7 zip function
# The zip function takes multiple sequences and makes an iterator that combines them.
cols = ['symbol', 'price', 'date']
vals = ['GOOG', 100, '10-01-2010']
pairs = zip(cols, vals)
for col, val in pairs:
    print(col, val)
# A common use of zip is to create key/value pairs for constructing dictionaries.
d = dict(zip(cols, vals))
print(d)

# 8 sequence for-loop
"""
Sometimes the for statement, len(), and range() get used by novices in some kind 
of horrible code fragment that looks like it emerged from the depths of a rusty C program.

Don’t do that! It’s inefficient with memory and it runs a lot slower. 
Just use a normal for loop if you want to iterate over data. 
Use enumerate() if you happen to need the index for some reason.
"""

# 9.1 exec: A practical enumerate() example
"""in pcost.py"""

# 9.2 exec: inverting a dictionary
prices = {'apple': 0.50, 'orange': 0.25, 'pear': 0.15}
pricelist = list(zip(prices.values(), prices.keys()))
print(pricelist)
print(min(pricelist))
print(max(pricelist))
print(sorted(pricelist))
# When used in comparisons, tuples are compared element-by-element starting with the first item. 
# Similar to how strings are compared character-by-character.

# Note that zip() is not limited to pairs. 
# For example, you can use it with any number of input lists:
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.3, 0.4, 0.5]
print(list(zip(a, b, c)))
# Also, be aware that zip() stops once the shortest input sequence is exhausted.
a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b']
print(list(zip(a, b)))
