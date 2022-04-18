# 1 Using a library function
import csv
f = open('./Work/Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for r in rows:
    print(r)
f.close()

# 2 read from the command line
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Work/Data/portfolio.csv'

print(filename)
