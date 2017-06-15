#importing library to use random number generator module
import random

#generating random number between 0 to 9
rand = int(random.randint(0,9))
#print(rand)
#count variable to count the number of rounds the player takes to guess the number
count = 1

#Asking the user to input the number that they want to guess in the 1st round
print("Turn 1:")
num = input("Guess the number picked by the system:")

#Type casting the num to integer
n = int(num)

#displaying the result to user
while(n!=rand):

    #checking if number guessed is less than the random number picked by the system
    if (n<rand):
        print("Sorry! number guessed by you is less than the number picked by the system.")

    # checking if number guessed is more than the random number picked by the system
    else:
        print("Sorry! number guessed is more than the number picked by the system.")

    count = count + 1
    # Asking the user to input the number that they have guessed
    print("Turn", count, ":")
    num = input("Guess the number picked by the system:")

    # Type casting the num to integer
    n = int(num)

#checking if number guessed is exactly equal
if (count == 1):
    print("Congratulations! You have guessed the number correctly in 1 round")
else:
    print("You have guessed the number correctly in", count, "rounds")