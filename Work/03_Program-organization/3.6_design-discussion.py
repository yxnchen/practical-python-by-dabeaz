# 1 filenames vs. iterables
"""
# Provide a filename
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
"""

"""
# Provide lines
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
"""

# 2 Deep Idea: “Duck Typing”
"""
Duck Typing is a computer programming concept to determine whether an object can be used for a particular purpose. 
It is an application of the duck test.

If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

In the second version of read_data() above, the function expects any iterable object. 
Not just the lines of a file.

This means that we can use it with other lines.
e.g., CSV file, zipped file, standard input, list of strings, etc.

lines = open('data.csv'); read_data(lines)
lines = gzip.open('data.csv.gz', 'rt'); read_data(lines)
lines = sys.stdin; read_data(lines)
lines = ['a', 'b', 'c']; read_data(lines)
"""
# There is considerable flexibility with this design.

# 3 Library Design Best Practices
# Code libraries are often better served by embracing flexibility. 
# Don’t restrict your options. With great flexibility comes great power.


# 4.1 exec: 
# You’ve now created a file fileparse.py that contained a function parse_csv(). 
# Modify the function so that it works with any file-like/iterable object.
# be aware that what if we still feed in a file name?

# 4.2 exec:
# fixing existing functions at report.py and pcost.py