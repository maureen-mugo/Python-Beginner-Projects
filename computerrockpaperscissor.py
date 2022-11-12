#rock, paper, scissors humans vs computer
from random import randint

choices = ["rock", "paper", "scissors"]

play = True
while play:
    try:
        computer = choices[randint(0,2)]
        
        player = input("Rock, Paper, Scissors?").lower()
        if player not in choices:
            print("Key in the the following (rock, paper, scissors)")
            continue
        
    except Exception as e:
        print(str(e))
        break

    if player == computer:
        print("Tie!")
        playagain = True

    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            playagain = True
        else:
            print("You win!", player, "smashes", computer)
            playagain = True

    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            playagain = True
        else:
            print("You win!", player, "covers", computer)
            playagain = True

    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            playagain = True
        else:
            print("You win!", player, "cut", computer)
            playagain = True

    else:
        print("That's not a valid play. Check your spelling!")
        break

    playagain = False
    while not playagain:
        playagain = input("Do you want to play again (y/n)? ")
        if playagain.lower() == 'y':
            play = True

        elif playagain.lower() == 'n':
            print("Byee!")
            play = False
            break
        else:
            print("Wrong Output!")
            play = False
            break
