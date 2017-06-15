#var to check if the user wants to continue check for another number
i = 1

while(i != 0):
    # take input from user
    number = input("Please enter a number: ")

    #type casting input from user into integer
    n = int(number)

    #calculating the remainder when the number is divided by 2
    r = n%2

    #displaying if the number is even or odd based on the remainder
    if (r == 0):
        print("The number", n, "entered by user is even")
    else:
        print("The number", n, "entered by user is odd")

    data = input("Do you want to continues(yes/no): ")
    if (data.upper() == "YES" ):
        i = 1
    else:
        i = 0