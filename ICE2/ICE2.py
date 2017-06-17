def task1():
    filename = input("Input the file name: ")
    x = open(filename, 'r')
    sum = 0.0
    n = 0
    line = x.readline()
    while line != "":
        for str in line.split(","):
            sum = sum + eval(str)
            n = n + 1
        line = x.readline()
    print("\n The avg is ", sum/n)


#Calculate character frequency in a string
print("Enter the string:")
s =input()
def freq(s):
    dict = {}
    for i in s:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i]+ 1
        else:
            dict[i] = 1
    return dict
print(freq(s))

#take list of words and return the length of longest word
data = input("Enter a string to calculate the longest word:")
l = 0
str = ""
for x in data.split(" "):
    if(l < len(x)):
        l = len(x)
        str = x
print( str, ":", l)

#take string and calculate the number of digits and letters
data = input("Enter a word to calculate num of digits and alphabets:")
alpha = 0
dig = 0
i = 0
l = len(data)
while i < len(data):
    if data[i].isalpha():
        alpha = alpha + 1
    elif data[i].isnumeric():
        dig = dig + 1
    i = i + 1
print("Number of digits is ", dig ,"and number of alphabets is:", alpha)





