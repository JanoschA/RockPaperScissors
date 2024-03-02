import random
from GameRule import GameRule

gameRules = GameRule.from_file('gameRules.txt')
game_rules_dict = GameRule.to_dict(gameRules)

print("Welcome to Rock, Paper, Scissors!")
print("Here are the rules:")
print("You need to choose one of the following: rock, paper, or scissors.")
print("But beware, there are other options too!")

while True:
    user_choice = input("Enter your choice: ").lower()
    if user_choice in game_rules_dict:
        print(f"Your choice is {user_choice}.")

        computer_choice = random.choice(list(game_rules_dict.keys()))

        print(f"The computer's choice is {computer_choice}.")

        if user_choice in game_rules_dict[computer_choice]['beats']:
            print("You lose!")
        elif user_choice in game_rules_dict[computer_choice]['tie']:
            print("It's a tie!")
        elif user_choice in game_rules_dict[computer_choice]['lose']:
            print("You win!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Let's play again!")
    else:
        print("Invalid choice. Please try again.")
