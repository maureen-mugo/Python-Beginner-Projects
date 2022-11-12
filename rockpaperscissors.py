
choices = ["rock", "paper", "scissors"]

player1 = input("choice: ").lower()
if player1 not in choices :
    print("Invalid entry")
print(f"player 1 plays: {player1}")

player2 = input("choice: ").lower()
if player2 not in choices :
    print("Invalid entry")
print(f"player 2 plays: {player2}")



def winner():
   
   # "rock" > "scissors"
   #"scissors" > "paper"
    #"paper" > "rock"
    

    if player1 == "rock" and player2 == "scissors":
        print("player 1 is the winner,", player1, "smashes", player2) 
    elif player1 == "scissors" and player2 == "rock":
        print("player 2 is the winner,", player2, "smashes", player1)
    elif player1 == "scissors" and player2 == "paper":
        print("player 1 is the winner,", player1, "smashes", player2)
    elif player1 == "paper" and player2 == "scissors":
        print("player 2 is the winner,", player2, "smashes", player1)
    elif player1 == "paper" and player2 == "rock":
        print("player 1 is the winner,", player1, "smashes", player2)
    elif player1 == "rock" and player2 == "paper":
        print("player 2 is the winner,",player2, "smashes", player1)
    elif player1 == player2:
        print("its a tie, play again")
            
    else:
        print("That's not a valid play. Check your spelling or entry!")


winner()
