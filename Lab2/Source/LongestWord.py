# program to find longest word in each line
# fetching the file name to be checked from user
file = input("Input the file name: ")
# reading the file
x = open(file, 'r')
# reading a line in the file
line = x.readline()
# iterating through until we reach the end of the file
while line != "":
    l = 0
    data = ""
    # splitting the by ',' and iterating through the list of words
    for str in line.split(","):
        # trying to fetch the longest word length
        if (l < len(str)):
            l = len(str)
            data = str
    line = x.readline()
    # printing the longest word and its length in each line
    print(data, ":", l)