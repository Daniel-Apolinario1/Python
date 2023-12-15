# ---------------------------------------------------------------
#            %%%%%      DAY FOUR PROJECT      %%%%%
# ---------------------------------------------------------------
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

player_score = 0
computer_score = 0

print(f"Computer score {computer_score}")
print(f"Your score {player_score}")

while player_score < 5 and computer_score < 5:
    computer_move = random.randint(0, 2)
    player_move = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS\n"))
    if player_move < 0 or player_move >= 3:
        print("You chose an invalid number, you lose!")
        computer_score += 1
    else:
        if computer_move == player_move:
            print(moves[player_move])
            print(f"Computer chose:\n{moves[computer_move]}")
            print("It's a draw!")
        elif computer_move == 0 and player_move == 2:
            print(moves[player_move])
            print(f"Computer chose:\n{moves[computer_move]}")
            print("You lose :(")
            computer_score += 1
        elif computer_move == 2 and player_move == 0:
            print(moves[player_move])
            print(f"Computer chose:\n{moves[computer_move]}")
            print("You WON! Congratulations")
            player_score += 1
        elif computer_move < player_move:
            print(moves[player_move])
            print(f"Computer chose:\n{moves[computer_move]}")
            print("You WON! Congratulations")
            player_score += 1
        elif computer_move > player_move:
            print(moves[player_move])
            print(f"Computer chose:\n{moves[computer_move]}")
            print("You lose :(")
            computer_score += 1
        else:
            print("You chose an invalid number, you lose :(")
            computer_score += 1
    print(f"Computer score {computer_score}")
    print(f"Your score {player_score}")
