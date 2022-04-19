# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    """computes the total cost of a portfolio file"""
    total_cost = 0.
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for no, row in enumerate(rows, 1):
            record = dict(zip(headers, row))
            try:
                shares, price = int(record['shares']), float(record['price'])
                total_cost += shares * price
            except ValueError as err:
                print(f'Row {no}: bad row {row}')
    return total_cost


if __name__ == '__main__':
    pcost = portfolio_cost('./Work/Data/portfolio.csv')
    print(pcost)
    pcost = portfolio_cost('./Work/Data/missing.csv')
    print(pcost)
    pcost = portfolio_cost('./Work/Data/portfoliodate.csv')
    print(pcost)
