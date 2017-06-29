# Taking input from user and converting into list and tuple

# Taking input string from user
str = input("Enter a string:")

# Initialising list
list = []

# Iterating through each element in the string and appending it to list
if(str != ""):
    for x in range(0, len(str)):
        list.append(str[x])
else:
    input("Please enter a string:")

# printing list
print("The list created from string is:",list)
# printing tuple
print("The tuple created from string is:",tuple(list))