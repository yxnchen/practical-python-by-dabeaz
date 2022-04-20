"""
A problem
Suppose you wanted to create your own custom iteration pattern.

>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
"""

# 1 generators
# A generator is a function that defines iteration.
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for x in countdown(10):
    print(x, end=' ')
print()
# A generator is any function that uses the yield statement.
# The behavior of generators is different than a normal function. 
# Calling a generator function creates a generator object. It does not immediately execute the function.
def countdown(n):
    print('Counting down from: ', n)
    while n > 0:
        yield n
        n -= 1
cd = countdown(10)  # no print statement
print(cd)  # a generator object
# The function only executes on __next__() call.
print(cd.__next__())

# yield produces a value, but suspends the function execution. 
# The function resumes on next call to __next__().
print(cd.__next__())
print(cd.__next__())
# When the generator finally returns, the iteration raises an error.

"""
Observation: A generator function implements the same low-level protocol 
that the for statements uses on lists, tuples, dicts, files, etc.
"""

# 2.1 exec: A Simple Generator
# If you ever find yourself wanting to customize iteration, you should always think generator functions. 
# They’re easy to write—make a function that carries out the desired iteration logic and 
# use yield to emit values.
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line
for line in open('./Work/Data/portfolio.csv'):
    print(line, end='')
print()
for line in filematch('./Work/Data/portfolio.csv', 'IBM'):
    print(line, end='')
# This is kind of interesting–the idea that you can hide a bunch of custom processing in a function 
# and use it to feed a for-loop.


# 2.2 exec: Monitoring a streaming data source
# Generators can be an interesting way to monitor real-time data sources such as log files or 
# stock market feeds. In this part, we’ll explore this idea.

# The program Data/stocksim.py is a program that simulates stock market data. 
# As output, the program constantly writes real-time data to a file Data/stocklog.csv. 
# In a separate command window go into the Data/ directory and run this program:
# % python3 stocksim.py

# Using another window, look at the file Data/stocklog.csv being written by the simulator. 
# You should see new lines of text being added to the file every few seconds. 
# Again, just let this program run in the background—it will run for several hours 
# (you shouldn’t need to worry about it).

# Once the above program is running, let’s write a little program to open the file, 
# seek to the end, and watch for new output. Create a file follow.py and put this code in it:

# If you run the program, you’ll see a real-time stock ticker. 
# Under the hood, this code is kind of like the Unix 'tail -f' command that’s used to watch a log file.


# 2.3 exec: Using a generator to produce data
# If you look at the code in Exercise 6.5, the first part of the code is producing lines of data 
# whereas the statements at the end of the while loop are consuming the data. 
# A major feature of generator functions is that you can move all of the data production code into a reusable function.

# Modify the code in Exercise 6.5 so that the file-reading is performed by a generator function follow(filename). 


# 2.3 exec: Watching your portfolio
# Modify the follow.py program so that it watches the stream of stock data and 
# prints a ticker showing information for only those stocks in a portfolio. 

# Note: For this to work, your Portfolio class must support the in operator. 
# See Exercise 6.3 and make sure you implement the __contains__() operator.
