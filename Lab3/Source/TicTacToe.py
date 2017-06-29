# program to build a tic tac toe game

import random

# initialising the lists to store the corresponding co-ordinates
list_star = []
list_zero = []
# initialising dimensions
d = 3
# string to store result
result = ""

# var to check if the round was played
zero_Check = False
star_Check = False


# function to print horizontal lines
def print_horiz_line():
  return " --- "

# function to print vertical lines
def print_vert_line():
    return "|    "

# function to print star
def print_star():
    return "| *  "

# function to print zero
def print_zero():
    return "| 0  "

# function to handle player 1
def player1():
    global star_Check
    check = False;
    verify = False
    # taking co-ordinates from user
    list1 = input("Enter the the row and column for player 1(row,col):").split(",")
    if(len(list1[0]) == 1 and len(list1[1]) == 1):
        verify = True
    else:
        verify = False
        print("Something went wrong! Please play again.")
        player1()

    global list_star
    # checking if the co-ordinate is used up
    if((list1 in list_star) or (list1 in list_zero)):
        check = False;
        print("The spot is already used up. Please use another one.")
        player1()
    else:
        check = True
    # appending to the list and printing the star
    if(check == True and verify == True):
        list_star.append(list1)
        print_player()
        star_Check = True

# function to handle player 2
def player2():
    global zero_Check
    check = False;
    verify = False
    # taking co-ordinates from user
    list2 = input("Enter the the row and column for player 2(row,col):").split(",")
    if (len(list2[0]) == 1 and len(list2[1]) == 1):
        verify = True
    else:
        verify = False
        print("Something went wrong! Please play again.")
        player2()

    global list_zero
    # checking if the co-ordinate is used up
    if ((list2 in list_star) or (list2 in list_zero)):
        check = False;
        print("The spot is already used up. Please use another one.")
        player2()
    else:
        check = True
    # appending to the list and printing the zero
    if (check == True and verify == True):
        list_zero.append(list2)
        print_player()
        zero_Check = True

# function to print game board
def print_player():
    global d
    global result
    game = ""
    # iterating through rows and columns
    for i in range(0, d):
        # printing horizontal line for 3 columns
        game = game + print_horiz_line() * d + "\n"
        for j in range(0, d):
            # printing star if the (row,col) matches
            if([str(i+1),str(j+1)] in list_star):
                game = game + print_star()
            # printing zero if the (row,col) matches
            elif ([str(i + 1), str(j + 1)] in list_zero):
                game = game + print_zero()
            # printing just borders
            else:
                game = game + print_vert_line()
        game = game + print_vert_line()
        game = game + "\n"
    # printing horizontal line for 3 columns
    game = game + print_horiz_line() * d
    # printing result
    result = game

# main function to check which users turn is it and taking to corresponding operations
def main():
    global result
    global list_star
    global list_zero
    global star_Check
    global zero_Check
    i = 0
    while(len(list_star)<5 or len(list_zero)<4):
        if((i+1)%2 == 0):
            player2()
        else:
            player1()
        print(result)
        if(star_Check == True or zero_Check == True):
            i = i + 1
            star_Check = False
            zero_Check = False

    print("End of the game!")

    # checking if user wants to play again and correspondingly taking action
    game = input("Do you want to play again?(YES/NO):")
    if(game.upper() == "YES"):
        i = 0
        list_zero = []
        list_star = []
        result=""
        main()
    else:
        print("Thanks for playing")
# calling main function
main()