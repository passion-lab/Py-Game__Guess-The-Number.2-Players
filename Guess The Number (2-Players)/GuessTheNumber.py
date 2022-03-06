# Practical Problem 6
# Input max and min number, choose in between those two without displaying, two players plays one-by-one until
# they choose the right one, have to display the number of trail to complete and declared winner with min trail

import random

a = int(input("Choose a minimum number: "))
b = int(input("Choose a maximum number: "))

player1_target = random.randint(a, b)
player2_target = random.randint(a, b)


def play(player_target: int):
    trial = 1

    while 1:
        player1_input = int(input(f"Guess the number between {a} and {b}: "))

        if player1_input == player_target:
            print(f"\nYou guess just the RIGHT number i.e., {player_target} in {trial} trail(s).\n")
            return trial
        else:
            if player1_input > player_target:
                print("Choose a lesser number this time.")
            else:
                print("Choose a greater number this time.")
            trial += 1
            continue


print("\nTurn: PLAYER 1\n")
round1 = play(player1_target)

print("\nTurn: PLAYER 2\n")
round2 = play(player2_target)

if round1 > round2:
    print(f"WINNER: Player 2 | BY: {round1 - round2} Trial(s)")
elif round1 < round2:
    print(f"WINNER: Player 1 | BY: {round2 - round1} Trial(s)")
else:
    print(f"MATCH DRAW!")
