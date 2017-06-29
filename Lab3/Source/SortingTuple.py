# program to sort the list by last element of tuple in increasing order
List=[(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]

output = sorted(List, key=lambda x: x[-1])
print(output)