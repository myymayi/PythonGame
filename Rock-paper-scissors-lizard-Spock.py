# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
    
import random

# helper functions
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name =="lizard":
        return 3
    elif name == "scissors":
        return 4

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Wrong"
    
def rpsls(player_choice):
    computer_number = random.randrange(0,5)
    player_number = name_to_number(player_choice)
    
    print "Player chooses "  + player_choice + "."
    print "Computer chooses " + number_to_name(computer_number) + "."
        
    if player_number - computer_number in [1, 2, -4, -3]:
        print "Player wins!"
        print " "
    elif player_number - computer_number in [3, 4, -1, -2]:
        print "Computer wins!"
        print " "
    elif player_number - computer_number == 0:
        print "Player and computer tie!"
        print " "
    else:
        print "Wrong"
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

