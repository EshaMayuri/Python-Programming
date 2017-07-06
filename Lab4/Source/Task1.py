import operator
import collections

# Ordering elements of dictionary by either key or value
x = {1:34, 6:4, 5:10, 2:12, 9:25}

# Ordering elements of dictionary by key
sortedByElement1 = dict(sorted(x.items(), key=operator.itemgetter(0)))
print("Ordered by key:",sortedByElement1)

# Ordering elements of dictionary by value
sortedByElement2 = dict(sorted(x.items(), key=operator.itemgetter(1)))
print("Ordered by value:",sortedByElement2)

# using ordereddict
z = {1:34, 6:4, 5:10, 2:12, 9:25}
print("Sorted dictionary(using orderedDict): ",collections.OrderedDict(sorted(z.items())))