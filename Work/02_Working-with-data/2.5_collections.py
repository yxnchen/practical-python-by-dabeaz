"""
The collections module provides a number of useful objects for data handling. 
"""

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('HPQ', 75, 53.0),
    ('YHOO', 50, 32.8),
    ('ACME', 10, 5.0),
    ('AAPL', 10, 91.1),
    ('GOOG', 10, 490.1),
    ('IBM', 10, 91.1)
]

# 1 using a counter
from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares
print(total_shares['IBM'])

# 2 one-2-many mapping
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
print(holdings['IBM'])
print(holdings['unknown'])

# 3 keeping a history
# Problem: We want a history of the last N things. Solution: Use a deque.
from collections import deque
history = deque(maxlen=3)
with open('./Work/Data/portfolio.csv') as f:
    for line in f:
        history.append(line)
print(history)

# 4.1 exec: tabulating with counters
import sys
sys.path.append('./Work')
from report import read_portfolio
pf = read_portfolio('./Work/Data/portfolio.csv')
holdings = Counter()
for s in pf:
    holdings[s[0]] += s[1]
print(holdings)
# You can use a Counter just like a dictionary to retrieve individual values:
print(holdings['IBM'])
# rank the values: get 3 most held stocks
print(holdings.most_common(3))

pf2 = read_portfolio('./Work/Data/portfolio2.csv')
holdings2 = Counter()
for s in pf2:
    holdings2[s[0]] += s[1]
print(holdings2)

# ombine all of the holdings doing one simple operation:
combined = holdings + holdings2
print(combined)
