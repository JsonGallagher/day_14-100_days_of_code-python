"""
Move options:
RR - draw
RP
RS

PP - draw
PR
PS

SS - draw
SR
SP

p1 invalid
p2 invalid
"""

from getpass import getpass as input

print("EPIC    🪨 📄 ✂️    BATTLE ")
print()
print("Select your move: R, P S")

p1_move = input("Player 1: What is your move? ").lower()
p2_move = input("Player 2: What is your move? ").lower()

if p1_move == 'r':
    if p2_move == 'r':
        print("You both chose rock, the game is a draw!")
    elif p2_move == 'p':
        print("Player 1's rock is smothered by Player 2's paper.")
    elif p2_move == 's':
        print("Player 1's rock destroyed Player 2's scissors.")
    else:
        print(f"Sorry Player 2, {p2_move} is an invalid move.")
elif p1_move == 'p':
    if p2_move == 'p':
        print("You both chose paper, the game is a draw!")
    elif p2_move == 'r':
        print("Player 1's paper smothered Player 2's rock.")
    elif p2_move == 's':
        print("Player 2's scissors cut up Player 1's paper.")
    else:
        print(f"Sorry Player 2, {p2_move} is an invalid move.")
elif p1_move == 's':
    if p2_move == 's':
        print("You both chose scissors, the game is a draw!")
    elif p2_move == 'r':
        print("Player 2's rock is destroyed Player 1's scissors.")
    elif p2_move == 'p':
        print("Player 1's scissors cut up Player 2's paper.")
    else:
        print(f"Sorry Player 2, {p2_move} is an invalid move.")
else:
    print(f"Sorry Player 1, {p1_move} is an invalid move.")
