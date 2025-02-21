# Lesson 9
import random
choices = ["rock", "paper", "scissors"]
userChoice = ""

while userChoice != "x" :
    print("enter your choice")
    userChoice = input()
    botChoice = random.choice(choices)
    if userChoice not in choices:
        print("not available")
    else :
        if userChoice == botChoice :
            print("draw")
        elif userChoice == "scissors" :
            if botChoice == "rock":
                print("lost")
            else:
                print("won")
        elif userChoice == "rock":
            if botChoice == "paper":
                print("lost")
            else:
                print("won")
        else:
            if botChoice == "scissors":
                print("lost")
            else:
                print("won")
        print(f"{botChoice} vs {userChoice}")

