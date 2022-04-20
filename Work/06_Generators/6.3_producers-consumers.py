"""
Producers, Consumers and Pipelines
Generators are a useful tool for setting various kinds of producer/consumer problems and dataflow pipelines.

Producer-Consumer Problems
Generators are closely related to various forms of producer-consumer problems.

# Producer
def follow(f):
    ...
    while True:
        ...
        yield line        # Produces value in `line` below
        ...

# Consumer
for line in follow(f):    # Consumes value from `yield` above
    ...
    
yield produces values that for consumes.
"""

# 1 Generator Pipelines
# You can use this aspect of generators to set up processing pipelines (like Unix pipes).
# producer → processing → processing → consumer

# Processing pipes have an initial data producer, some set of intermediate processing stages and a final consumer.
"""
def producer():
    ...
    yield item
    ...
"""
# The producer is typically a generator. Although it could also be a list of some other sequence. 
# yield feeds data into the pipeline.

"""
def consumer(s):
    for item in s:
        ...
"""
# Consumer is a for-loop. It gets items and does something with them.

"""
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
"""
# Intermediate processing stages simultaneously consume and produce items. 
# They might modify the data stream. They can also filter (discarding items).

# Code to setup the pipeline
# You will notice that data incrementally flows through the different functions.
"""
a = producer()
b = processing(a)
c = consumer(b)
"""

# 2.1 exec: Setting up a simple pipeline
# it’s no longer opening a file–it merely operates on a sequence of lines given to it as an argument.
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
            
from follow import follow
lines = follow('./Work/Data/stocklog.csv')
ibm = filematch(lines, 'IBM')
stop_flag = 0
for line in ibm:
    print(line)
    stop_flag += 1
    if stop_flag >= 1:
        break
print()

# 2.2 exec: Setting up a more complex pipeline
# What you’re seeing here is that the output of the follow() function has been piped into the csv.reader() function 
# and we’re now getting a sequence of split rows.
from follow import follow
lines = follow('./Work/Data/stocklog.csv')
import csv
rows = csv.reader(lines)
stop_flag = 0
for row in rows:
    print(row)
    stop_flag += 1
    if stop_flag >= 5:
        break
print()


# 2.3 exec: Making more pipeline components
# In a separate file ticker.py, start by creating a function that reads a CSV file as you did above:

# 2.4 exec: filtering data
# Write a function that filters data.

# 2.5 exec: puttttting it all together
# In the ticker.py program, write a function ticker(portfile, logfile, fmt) that 
# creates a real-time stock ticker from a given portfolio, logfile, and table format. 

"""
Some lessons learned: You can create various generator functions and chain them together to perform processing 
involving data-flow pipelines. In addition, you can create functions that package a series of pipeline stages 
into a single function call (for example, the parse_stock_data() function).
"""
