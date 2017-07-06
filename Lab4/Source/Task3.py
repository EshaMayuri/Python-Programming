# program to get a coma separated sequence of words then the output should be sorted in comma separated manner
# importing operator module
import operator
import re
# Taking the data from the user that needs to be sorted
str = input("enter the list of words to be sorted(ex: here, is, a, sample):")
data = {}
i = 0
# storing the words in dict
for x in str.split(","):
    data[i] = x.replace(" ","")
    i = i + 1
# sorting the values as per the their first letter
sorted_x = sorted(data.items(), key=operator.itemgetter(1))
result =""
# print the sorted data
for data in sorted_x:
    if(result ==""):
        result = result + data[1]
    else:
        result = result + ","+data[1]

print("The sorted data is:",result)