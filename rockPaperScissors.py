# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like randome and time packages wev'e discussed about) 
# ----------------------------------------------------------------------------------------------------------------------
#import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course :
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
# """
# # I'll give you the text inputs for this program, to make your lives a little easier.
# # In addition, and to make it simple to you, the input from the user will be an integer:
# # 1 for ROCK
# # 2 for PAPER
# # 3 for SCISSORS
# # A text input describing the operation is unacceptable and will cost you with points.
# #
# # A quick reminder of the rules:
# #
# # ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
# # SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
# # PAPER(2) vs ROCK(1)      --> PAPER(2) wins
# #
# #
# # DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
# # # """
#
# # print the instructions for the user to see:
# print("GAME RULES: \n"
#       "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
#       "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
#       "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
#
# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
# while True:
#    """
#      This is the game's heart. You'll need to think and use everything we've learned so far to make this game work.
#      Remember Python's rules ( the ':' after a statement, the indentation with loops and statements..)
#
#      """
#    pass
#"


print("#Hello User please enter your name down below")

User_name = input("Enter User`s name:")

print("Hello" , User_name + " Welcome to Rock Paper Scissor game in python Created by Roman Karpov , Enjoy and have a good time!")

print("Game Rules : "
        "Rock(1) vs Scissors(3)  --> Rock(1) wins |"
        " Scissors(3) vs Paper(2)  --> Scissors(3) win |"
        " Paper(2) vs Rock(1)  --> Paper(2) wins")

gamelist = ["Rock","Paper","Scissors"]

from random import randint
AI = gamelist[randint(0,2)]

User = False

while User == False:

    print(User_name + " Please enter your choice down below")
    User = input("Rock, Paper, Scissors?")
    if User == AI:
        print("Its a tie!")
    elif User == "Rock":
        if AI == "Paper":
            print("You lose! Computers choice:", AI, "Wins this time! Your choice:", User)
        else:
            print("You win! Your choice:", User, "Wins this time! Computer's choice:", AI)
    elif User == "Paper":
        if AI == "Scissors":
            print("You lose! Computer's choice", AI, "Wins this time! Your choice:", User)
        else:
            print("You win! Your choice:", User, "Wins this time! Computer's choice:", AI)
    elif User == "Scissors":
        if AI == "Rock":
            print("You lose! Computers choice:", AI, "Wins this time! Your choice:", User)
        else:
            print("You win! Your choice:", User, "Wins this time! Computers choice:", AI)
    else:
        print("That's not a valid choice. Check your spelling!")

    User = False
    AI = gamelist[randint(0,2)]

    Newgame = input("Do you want to keep playing? Choose y/n\n")
    while Newgame != "y" and Newgame != "n":
        print("Invalid answer , please choose y/n")
        Newgame = input("Do you want to keep playing? Choose y/n\n")

    if Newgame == 'y':
        print("New game has started!")
    elif Newgame =="n":
        print("Thanks for playing goodbye")
        break











