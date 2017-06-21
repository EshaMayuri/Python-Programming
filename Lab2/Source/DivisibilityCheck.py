# Divisor keys
a=7
b=5
# initialising output list
outputList=[]

# taking the input from user for the range in which the search will be done
print("Enter the range of search")
x = input("Enter the number from which you want to search: ")
leftLimit = int(x)
y = input("Enter the number until which you want to search: ")
rightLimit = int(y)

# iterating through every element in the range
for i in range(leftLimit, rightLimit):
    # checking the number is divisible by both the numbers
    if((i%a==0) and (i%b==0)):
        outputList.append(str(i))
print(','. join(outputList))

