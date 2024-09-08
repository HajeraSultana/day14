from getpass import getpass as input
print("🪨Rock 📄Paper ✂️Scissors! the ultimate game of chance")
print()
print("""Get ready for the ultimate battle of wits...and luck!
Let's play!""")
print()
print("Make your move (R, P or S)")
print()
player1Move = input("Player 1 >")
player2Move = input("player 2 >")
print()
if player1Move == "R" and player2Move == "R":
   print("You both picked Rock, draw!")
elif player1Move == "S" and player2Move == "S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
elif player1Move == "P" and player2Move == "P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
elif player1Move == "R" and player2Move == "P":
    print("Player1's Rock is smothered by Player2's Paper!")
elif player1Move == "R" and player2Move == "S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
elif player1Move == "P" and player2Move == "R":
    print("Player1 wins! Paper beats rock!")
elif player1Move == "P" and player2Move == "S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
elif player1Move == "S" and player2Move == "R":
    print("Player2 beats player1 wiht rock!")
elif player1Move == "S" and player2Move == "P":
    print("Scissors beats paper! Player1 is the winner.")
else:
    print("Invalid move. Try again.")