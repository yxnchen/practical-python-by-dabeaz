# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

pf = read_portfolio('./Work/data/portfolio.csv')
print(pf)
print(pf[0])
print(pf[1][1])
total = 0.
for s in pf:
    total += s[1] * s[2]
print(total)

total = 0.
for name, shares, price in pf:
    total += shares * price
print(total)


def read_portfolio_2_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio

pf = read_portfolio_2_dict('./Work/data/portfolio.csv')
print(pf[0])
print(pf[1]['shares'])
total = 0.
for s in pf:
    total += s['shares'] * s['price']
print(total)
# Viewing large dictionaries and lists can be messy. 
# To clean up the output for debugging, consider using the pprint function.
from pprint import pprint
pprint(pf)


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices

prices = read_prices('./Work/data/prices.csv')
pprint(prices)
print(prices['IBM'])
