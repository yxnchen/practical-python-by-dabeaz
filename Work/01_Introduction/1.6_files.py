# 1 file input and output
f = open('./Work/01_Introduction/foo.txt', 'rt')  # open file for reading (text)
# real only up to 'maxbytes' bytes
data = f.read(2)
print(data)
# real all of the data
data = f.read()
print(data)
f.close()

g = open('./Work/01_Introduction/foo.txt', 'wt')  # open file for writing (text)
g.write('something')
g.close()

# Files should be properly closed and it’s an easy step to forget. 
# Thus, the preferred approach is to use the with statement like this.
with open('./Work/01_Introduction/foo.txt', 'rt') as f:
    data = f.read()
    print(data)
    

# 2 Common Idioms for Reading File Data
with open('./Work/01_Introduction/foo.txt', 'rt') as f:
    data = f.read()
    print(data)
    # data is a string with all the text in 'foo.txt'

with open('./Work/01_Introduction/foo.txt', 'rt') as f:
    for line in f:
        print(line)
    # line is a string with each line in 'foo.txt'

# 3 Common Idioms for Writing File Data
with open('./Work/01_Introduction/foo.txt', 'wt') as f:
    f.write('something\n')

with open('./Work/01_Introduction/foo.txt', 'wt') as f:
    # redirect the  print function
    print('something', file=f)
    
    
# 4 exec
import os
print(os.getcwd())

# 4.1 file preliminaries
with open('./Work/Data/portfolio.csv', 'rt') as f:
    data = f.read()
print(data)

with open('./Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')

f = open('./Work/Data/portfolio.csv', 'rt')
headers = next(f)
print(headers, end='')
for line in f:
    print(line, end='')
f.close()

# 5 other kind of files
# What if you wanted to read a non-text file such as a gzip-compressed datafile? 
# The builtin open() function won’t help you here, 
# but Python has a library module gzip that can read gzip compressed files.
import gzip
with gzip.open('./Work/Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
