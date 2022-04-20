# ticker.py

from follow import follow
import csv

# Write a new function that selects specific columns:
def select_columns(rows, indices):
    for row in rows:
        yield [row[i] for i in indices]
        
# Write generator functions that convert data types and build dictionaries.
def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row) ]
        
def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
# Write a function that filters data.
def filter_symbols(rows, names):
    # for row in rows:
    #     if row['name'] in names:
    #         yield row
    return (row for row in rows if row['name'] in names)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    import sys
    sys.path.append('./Solutions/3_18')
    import fileparse
    sys.path.append('./Work/04_Classes-and-Objects')
    from stock import Stock
    from tableformat import create_formatter, print_table
    from portfolio import Portfolio
    with open(portfile) as file:
        portdicts = fileparse.parse_csv(file, select=['name','shares','price'], types=[str,int,float])
    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    pf = Portfolio(portfolio)
    
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, pf)
    formatter = create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        rowdata = [str(row[h]) for h in ['name', 'price', 'change']]
        formatter.row(rowdata)

if __name__ == '__main__':
    ticker('./Work/Data/portfolio.csv', './Work/Data/stocklog.csv', 'txt')
