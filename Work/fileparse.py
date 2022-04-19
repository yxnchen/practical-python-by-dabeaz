# fileparse.py
#
# Exercise 3.3

import csv

# This function reads a CSV file into a list of dictionaries while hiding the details of opening the file, 
# wrapping it with the csv module, ignoring blank lines, and so forth.
def parse_csv(filename):
    """Parsing a CSV file into a list of records

    Args:
        filename (str): CSV file
    """
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:  ## skip empty rows
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records

pf = parse_csv('./Work/Data/portfolio.csv')
print(pf)
print()


def parse_csv(filename, select=None):
    """Parsing a CSV into a list of dict records with selected headers

    Args:
        filename (str): CSV file
        select (list, optional): selected headers. Defaults to None.

    Returns:
        list: list of dict records
    """
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:
            indices = range(len(headers))
        records = []
        for row in rows:
            if not row:  ## skip empty rows
                continue
            record = {name: row[idx] for name, idx in zip(headers, indices)}
            records.append(record)
    return records

pf = parse_csv('./Work/Data/portfolio.csv')
print(pf)
pf = parse_csv('./Work/Data/portfolio.csv', select=['name', 'shares'])
print(pf)
print()


def parse_csv(filename, select=None, types=None):
    """Parsing a CSV file to a list of dict records with selected headers and type specification

    Args:
        filename (str): CSV file
        select (list, optional): selected headers. Defaults to None.
        types (list, optional): type specification. Defaults to None.
    """
    if select and types and len(select) != len(types):
        raise ValueError('select and types must be the same length')
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:
            indices = range(len(headers))
        if not types:
            types = [str] * len(headers)
        records = []
        for row in rows:
            if not row:  ## skip empty rows
                continue
            record = {name: func(row[idx]) for name, idx, func in zip(headers, indices, types)}
            records.append(record)
    return records
    
pf = parse_csv('./Work/Data/portfolio.csv')
print(pf)
pf = parse_csv('./Work/Data/portfolio.csv', select=['name', 'shares'])
print(pf)
pf = parse_csv('./Work/Data/portfolio.csv', types=[str, int, float])
print(pf)
pf = parse_csv('./Work/Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
print(pf)
print()


def parse_csv(filename, select=None, types=None, has_header=True, delimiter=',', silence_errors=False):
    """Parsing a CSV file to a list of dict records with selected headers and type specification

    Args:
        filename (str): CSV file
        select (list, optional): selected headers. Defaults to None.
        types (list, optional): type specification. Defaults to None.
    """
    if select and not has_header:
        raise RuntimeError("select argument requires column headers")
    if select and types and len(select) != len(types):
        raise ValueError('select and types must be the same length')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_header:
            headers = next(rows)
            if select:
                indices = [headers.index(name) for name in select]
                headers = select
            else:
                indices = range(len(headers))
            if not types:
                types = [str] * len(headers)
        records = []
        for i, row in enumerate(rows, 1):
            if not row:  ## skip empty rows
                continue
            if has_header:
                try:
                    record = {name: func(row[idx]) for name, idx, func in zip(headers, indices, types)}
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i}: Counldn\'t convert {row}')
                        print(f'Row {i}: Reason {e}')
            else:
                try:
                    record = [func(r) for r, func in zip(row, types)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i}: Counldn\'t convert {row}')
                        print(f'Row {i}: Reason {e}')
                record = tuple(record)
            records.append(record)
    return records

pr = parse_csv('./Work/Data/prices.csv', types=[str, float], has_header=False)
print(pr)
pf = parse_csv('./Work/Data/portfolio.dat', types=[str, int, float], delimiter=' ')
print(pf)

# raise exception
# pr = parse_csv('./Work/Data/prices.csv', select=['name'], has_header=False)

# catch exception
pf = parse_csv('./Work/Data/missing.csv', types=[str, int, float])
print(pf)

# silence exception
pf = parse_csv('./Work/Data/missing.csv', types=[str, int, float], silence_errors=True)
print(pf)
