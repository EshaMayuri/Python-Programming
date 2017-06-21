# program to check if a string contains all letters of alphabet
# importing string module
import string

# taking input string from the user
str = input("Please enter a string to check if it contains all letters of alphabets:")
# converting string to lower case
str = str.lower()
# using string module fetching all the alphabets in english in lower case
alphabets = string.ascii_lowercase
data = ""
# iterating through each english alphabet
for i in range(0, len(alphabets)):
    # checking if string contains the current alphabet
    # if not storing the alphabet that is not available in the string entered by user
    if str.find(alphabets[i]) == -1:
        data = data + alphabets[i]
    # increment for the next alphabet
    i = i + 1
# printing relevant information to user
if (data != ""):
    print("The string entered does not contain alphabets '" , data, "'")
else:
    print("The string entered has all the alphabets")
