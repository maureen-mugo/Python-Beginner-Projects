#This is a guess the number game
import random
x = int(input("Range begins at: "))    #range begins at the given number
y = int(input("Range ends at: "))     #range ends at the given number

z = int(random.randint(x, y))

play = True
while play:
    try:

        choice = int(input("My guess is: "))
        if choice < x or choice > y:
            print("Your choice should be between {0} and {1}".format(x, y))
            continue

    except ValueError as e:
        print("An error has occurred, please counter check your input")
        print(str(e))
    
    if choice > z:
        print("Your guess is way too big.")
        playagain = True
        
    elif choice < z:
        print("Your guess is way too small.")
        playagain = True

    else:
        print("Your guess is correct")
        break

    playagain = False
    while not playagain:
        playagain = input("Do you wish to play again (yes, no)? ")
        if playagain.lower() == 'yes':
            play = True
        elif playagain.lower() == 'no':
            print("The number guessed should have been {}".format(z))
            print("Game Over!")
            play = False
            break
        else:
            print("Invalid Entry")
            play = False
            break

