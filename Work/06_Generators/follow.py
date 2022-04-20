import os
import time

# f = open('Data/stocklog.csv')
# f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1)   # Sleep briefly and retry
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)  # move file pointer 0 bytes from end of file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)  # sleep briefly and retry
            continue
        yield line

if __name__ == '__main__':
    import sys
    sys.path.append('./Solutions/3_18')
    import fileparse
    sys.path.append('./Work/04_Classes-and-Objects')
    from stock import Stock
    from portfolio import Portfolio
    with open('./Work/Data/portfolio.csv') as file:
        portdicts = fileparse.parse_csv(file, select=['name','shares','price'], types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    pf_container = Portfolio(portfolio)
    for line in follow('./Work/Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in pf_container:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

# Note: The use of the readline() method in this example is somewhat unusual in that 
# it is not the usual way of reading lines from a file (normally you would just use a for-loop). 
# However, in this case, we are using it to repeatedly probe the end of the file to see 
# if more data has been added (readline() will either return new data or an empty string).
