# program to build a tic tac toe game

import random
class Game(object):

    def __init__(self):
        # initialising dimensions
        self.d = 3
        self.player1_win = False
        self.player2_win = False

    # initialising the lists to store the corresponding co-ordinates
    list_star = []
    list_zero = []


    # string to store result
    result = ""

    # var to check if the round was played
    zero_Check = False
    star_Check = False


    # function to print horizontal lines
    def print_horiz_line(self):
      return " --- "

    # function to print vertical lines
    def print_vert_line(self):
        return "|    "

    # function to print star
    def print_star(self):
        return "| *  "

    # function to print zero
    def print_zero(self):
        return "| 0  "

    # function to handle player 1
    def player1(self):
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
            self.player1()

        global list_star
        # checking if the co-ordinate is used up
        if((list1 in self.list_star) or (list1 in self.list_zero)):
            check = False;
            print("The spot is already used up. Please use another one.")
            self.player1()
        else:
            check = True
        # appending to the list and printing the star
        if(check == True and verify == True):
            self.list_star.append(list1)
            self.print_player()
            star_Check = True

    # function to handle player 2
    def player2(self):
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
            self.player2()

        global list_zero
        # checking if the co-ordinate is used up
        if ((list2 in self.list_star) or (list2 in self.list_zero)):
            check = False;
            print("The spot is already used up. Please use another one.")
            self.player2()
        else:
            check = True
        # appending to the list and printing the zero
        if (check == True and verify == True):
            self.list_zero.append(list2)
            self.print_player()
            zero_Check = True

    # function to print game board
    def print_player(self):
        global d
        global result
        game = ""
        # iterating through rows and columns
        for i in range(0, self.d):
            # printing horizontal line for 3 columns
            game = game + self.print_horiz_line() * self.d + "\n"
            for j in range(0, self.d):
                # printing star if the (row,col) matches
                if([str(i+1),str(j+1)] in self.list_star):
                    game = game + self.print_star()
                # printing zero if the (row,col) matches
                elif ([str(i + 1), str(j + 1)] in self.list_zero):
                    game = game + self.print_zero()
                # printing just borders
                else:
                    game = game + self.print_vert_line()
            game = game + self.print_vert_line()
            game = game + "\n"
        # printing horizontal line for 3 columns
        game = game + self.print_horiz_line() * self.d
        # printing result
        result = game

    # start function to check which users turn is it and taking to corresponding operations
    def start(self):
        global result
        global list_star
        global list_zero
        global star_Check
        global zero_Check
        i = 0
        while(len(self.list_star)<5 or len(self.list_zero)<4):
            if((i+1)%2 == 0):
                self.player2()
            else:
                self.player1()
            print(result)
            if(star_Check == True or zero_Check == True):
                i = i + 1
                star_Check = False
                zero_Check = False
            # check for winning condition
            self.CheckWinningCondition()
            if(self.player1_win == True):
                print("Player 1 won! Congratulations!")
                break
            if (self.player2_win == True):
                print("Player 2 won! Congratulations!")
                break
        print("End of the game!")

        # checking if user wants to play again and correspondingly taking action
        game = input("Do you want to play again?(YES/NO):")
        if(game.upper() == "YES"):
            i = 0
            self.list_zero = []
            self.list_star = []
            result=""
            self.start()
        else:
            print("Thanks for playing")

    #function to check for winning condition
    def CheckWinningCondition(self):
        winningCond = [[['1', '1'], ['2', '2'], ['3', '3']],[['1', '1'], ['1', '2'], ['1', '3']],
                       [['2', '1'], ['2', '2'], ['2', '3']],[['3', '1'], ['3', '2'], ['3', '3']],
                       [['1', '2'], ['2', '2'], ['3', '2']], [['1', '1'], ['2', '1'], ['3', '1']],
                       [['1', '3'], ['2', '3'], ['3', '3']]]
        if (self.list_star in winningCond):
            self.player1_win = True
        if (self.list_zero in winningCond):
            self.player2_win = True

# Creating an instance
game = Game()
game.start()