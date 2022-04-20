"""
This section introduces a few additional generator related topics including \
- generator expressions 
- the itertools module.
"""

# 1 generator expressions
# A generator version of a list comprehension.
a = [1,2,3,4,5]
b = (2 * x for x in a)
print(b)
for i in b:
    print(i, end=' ')
print()

"""
Differences with List Comprehensions.
- Does not construct a list.
- Only useful purpose is iteration.
- Once consumed, can’t be reused.

General syntax:
(<expression> for i in s if <conditional>)
"""

# It can also serve as a function argument.
print(sum(x * x for x in a))

# It can be applied to any iterable.
b = (x * 2 for x in a)
c = (-x for x in b)
for i in c:
    print(i, end=' ')
print()

"""
The main use of generator expressions is in code that performs some calculation on a sequence, 
but only uses the result once. For example, strip all comments from a file.

f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()

With generators, the code runs faster and uses little memory. It’s like a filter applied to a stream.
"""

# 2 why generators?
"""
Many problems are much more clearly expressed in terms of iteration.
- Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.).
- Processing pipelines can be applied to a wide range of data processing problems.

Better memory efficiency.
- Only produce values when needed.
- Contrast to constructing giant lists.
- Can operate on streaming data

Generators encourage code reuse
- Separates the iteration from code that uses the iteration
- You can build a toolbox of interesting iteration functions and mix-n-match.
"""

# 3 itertools module
# The itertools is a library module with various functions designed to help with iterators/generators.
"""
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
"""
# All functions process data iteratively. They implement various kinds of iteration patterns.


# 4.1 exec； generator expressions
# Unlike a list a comprehension, a generator expression can only be used once. 
# Thus, if you try another for-loop, you get nothing:

# 4.2 exec: Generator Expressions in Function Arguments
nums = [1,2,3,4,5]
print(sum([x*x for x in nums]))  # A list comprehension
print(sum(x*x for x in nums))  # A generator expression
# The second version using generators would use significantly less memory if a large list was being manipulated.
# In your portfolio.py file, you performed a few calculations involving list comprehensions. 
# Try replacing these with generator expressions.

# 4.3 exec: Code simplification
# Generators expressions are often a useful replacement for small generator functions.
"""
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
"""
# You could write something like this:
"""
rows = (row for row in rows if row['name'] in names)
"""
# Modify the ticker.py program to use generator expressions as appropriate.
