# 1 creating new lists
a = [1, 2, 3]
b = [2*x for x in a]
print(b)

names = ['Alice', 'Bob', 'Cathy', 'Doug']
nn = [name.lower() for name in names]
print(nn)

# 2 filtering
a = [1, -3, 2, 0, -5, 6]
b = [2 * x for x in a if x > 0]
print(b)

stocks = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09}
]
stocknames = [s['name'] for s in stocks]
print(stocknames)
a = [s for s in stocks if s['price'] > 50 and s['shares'] > 50]
print(a)
cost = sum([s['shares'] * s['price'] for s in stocks])
print(cost)

# 3.1 exec: map-reduce
from select import select
import sys

from requests import head
sys.path.append('./Work')
from report import read_portfolio, read_prices
pf = read_portfolio('./Work/Data/portfolio.csv')
pr = read_prices('./Work/Data/prices.csv')
cost = sum([s[1] * s[2] for s in pf])
print(cost)
value = sum([s[1] * pr[s[0]] for s in pf if s[0] in pr])
print(value)

# 3.2 exec: data extraction
name_shares = [(s[0], s[1]) for s in pf]
print(name_shares)
# If you change the the square brackets ([,]) to curly braces ({, }), 
# you get something known as a set comprehension. 
# This gives you unique or distinct values.
names = {s[0] for s in pf}
print(names)
# If you specify key:value pairs, you can build a dictionary. [dictionary comprehension]
holdings = {s[0]: 0 for s in pf}
print(holdings)
for s in pf:
    holdings[s[0]] += s[1]
print(holdings)

# 3.3 exec: extracting data from csv files
import csv
f = open('./Work/Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
select = ['name', 'shares', 'price']
indices = [headers.index(col) for col in select]
print(indices)
row = next(rows)
record = {col: row[index] for col, index in zip(select, indices)}
print(record)

# reduced much of the read_portfolio() function to a single statement.
pf = [{col: row[index] for col, index in zip(select, indices)} for row in rows]
print(pf)
f.close()
