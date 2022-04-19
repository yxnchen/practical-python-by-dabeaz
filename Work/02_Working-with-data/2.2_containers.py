"""
Programs often have to work with many objects:

- A portfolio of stocks
- A table of stock prices

There are three main choices to use:

- Lists. Ordered data.
- Dictionaries. Unordered data.
- Sets. Unordered collection of unique items.
"""

# 1 lists as a container
# Use a list when the order of the data matters.
portfolio = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
]
records = []
with open('./Work/data/portfolio.csv') as f:
    next(f)  # skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
print(records)

# 2 dictionaries as a container
prices = {}
with open('./Work/data/prices.csv') as f:
    next(f)  # skip header
    for line in f:
        row = line.split(',')
        if len(row) == 2:
            prices[row[0]] = float(row[1])
print(prices)
print(prices.get('"AXP"'))
# look up a value that might not exist and provide a default value in case it doesn’t.
print(prices.get('hello', 0.))
# composite keys
# Almost any type of value can be used as a dictionary key in Python. 
# A dictionary key must be of a type that is immutable.
# Neither a list, a set, nor another dictionary can serve as a dictionary key, 
# because lists and dictionaries are mutable.
holidays = {
    (1, 1): 'New Year\'s Day',
    (3, 14): 'Pi Day',
    (12, 25): 'Christmas Day'
}
print(holidays[(1, 1)])
print(holidays[3, 14])

# 3 sets
tech_stocks = {'AAPL', 'GOOG', 'MSFT', 'FB'}
# or
tech_stocks = set(['AAPL', 'GOOG', 'MSFT', 'FB'])
print(tech_stocks)
print('IBM' in tech_stocks)
print('FB' in tech_stocks)
tech_stocks.add('IBM')
tech_stocks.remove('FB')
# other operations
s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}
print('set union:', s1 | s2)
print('set intersection:', s1 & s2)
print('set difference:', s1 - s2)
