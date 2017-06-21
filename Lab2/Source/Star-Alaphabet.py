# program to print first alphabet of my name using star
# taking name input from the user
name = input("Please enter you name:")

# extracting the 1st alphabet of the name and converting into caps
alphabet = name[0:1].upper()
# print(alphabet)

# initialising the dimensions of the alphabets that would be printed using star symbol
width = 5
height = 5

# defined function block for each alphabet
# logic for printing alphabet A
def first():
    result = ""
    # looping through vertical dimension
    for r in range(0, height):
        # looping through horizontal dimension
        for c in range(0, width):
            # printing star based on position
            if (((c == 0 or c == 4 ) and (r == 1 or r ==2 or r ==3 or r ==4)) or (c ==1 or c ==2 or c ==3) and (r==0 or r == 2)):
                result = result + "*"
            else:
                result = result + " "
        result = result + "\n"
    print(result)
# logic for printing alphabet B
def second():
    result = ""
    # looping through vertical dimension
    for r in range(0, height):
        # looping through horizontal dimension
        for c in range(0, width):
            # printing star based on position
            if ((c==0) or ((r==0 or r==2 or r==4) and (c==1 or c==2 or c==3)) or ((c==4)and(r==1 or r==3))):
                result = result + "*"
            else:
                result = result + " "
        result = result + "\n"
    print(result)
# logic for printing alphabet C
def third():
    result = ""
    # looping through vertical dimension
    for r in range(0, height):
        # looping through horizontal dimension
        for c in range(0, width):
            # printing star based on position
            if (((r==0 or r==4) and (c==1 or c==2 or c==3 or c==4)) or (c==0 and (r==1 or r==2 or r==3))):
                result = result + "*"
            else:
                result = result + " "
        result = result + "\n"
    print(result)
# logic for printing alphabet D
def fourth():
    result = ""
    # looping through vertical dimension
    for r in range(0, height):
        # looping through horizontal dimension
        for c in range(0, width):
            # printing star based on position
            if ((c==0) or ((r==0 or r==4) and c!=4) or (c==4 and (r==1 or r==2 or r==3))):
                result = result + "*"
            else:
                result = result + " "
        result = result + "\n"
    print(result)
# logic for printing alphabet E
def fifth():
    result = ""
    # looping through vertical dimension
    for r in range(0, height):
        # looping through horizontal dimension
        for c in range(0, width):
            # printing star based on position
            if ((c == 0) or (r == 0) or (r == 2) or (r == 4)):
                result = result + "* "
            else:
                result = result + " "
        result = result + "\n"

    print(result)

# maping each alphabet to the corresponding function blocks
options = {'A': first,
           'B': second,
           'C': third,
           'D': fourth,
           'E': fifth,
}

# calling a particular function based on 1st alphabet of the name
options[alphabet]()
