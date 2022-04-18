# 1 list sorting
s = [10, 1, 7, 3]
# lists can be sorted 'in place'
s.sort()
print(s)
# if you'd like to make a new list
t = sorted(s, reverse=True)
print(t)


# 2 lists and math
# Caution: Lists were not designed for math operations.
nums = [1,2,3]
print(nums * 2)
print(nums + [4,5])

# 3 find and remove
# there is no method to find or remove all occurrences of an item
symlist = ['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
print(symlist.index('YHOO'))
symlist.remove('YHOO')
print(symlist)
