# 1 string formatting with f-string
name = 'IBM'
shares = 100
price = 91.1

print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

# 2 format codes
"""
Format codes (after the : inside the {}) are similar to C printf().
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)

Common modifiers adjust the field width and decimal precision.
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
"""

# 3 dictionary formatting
# You can use the format_map() method to apply string formatting to a dictionary of values:
d = {'name': 'IBM', 'shares': 100, 'price': 91.1}
print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(d))

# 4 format() method
print('{name:>10s} {shares:>10d} {price:>10.2f}'.format(name='IBM', shares=100, price=91.1))
print('{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))

# 4 C-style formatting
print('The value is %d' % 3)
print('%5d %-5d %10d' % (1, 2, 3))
print('%.2f' % (3.14159,))
# This is the only formatting available on byte strings.
print(b'%s has %d messages' % (b'Dave', 37))

# 5.1 exec: how to format numbers
val = 42863.1
print(val)
print(f'{val:0.4f}')
print(f'{val:>16.2f}')
print(f'{val:<16.2f}')
print(f'{val:*>16,.2f}')
s = '%.4f' % val
print(s)

# 5.2 exec: collecting data
import sys
sys.path.append('./Work')
from report import read_portfolio, read_prices
pf = read_portfolio('Work/Data/portfolio.csv')
pr = read_prices('Work/Data/prices.csv')

def make_report(pf, pr):
    """
    Prints a report of the portfolio.
    """
    report = []
    for name, shares, price in pf:
        report.append((name, shares, price, price - pr.get(name, 0)))
    return report

report = make_report(pf, pr)
for r in report:
    print(r)
    
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
    
header = ('Name', 'Shares', 'Price', 'Change')
print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
print(f"{'-'*10:10s} {'-'*10:10s} {'-'*10:10s} {'-'*10:10s}")
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {"$%.2f" % price:>10s} {change:>10.2f}')
