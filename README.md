# ROCK PAPER SCISSORS (FOUNTAIN) Game

This is a simple rock paper scissors game implemented in Python with a twist - the fountain is overpowered. This project serves as a fun way to learn Python.

## Description

The game is a simple rock paper scissors game with a twist. The fountain is overpowered, because it has two winnings options (against rock and scissors) and only one losing option (against paper). The rules are in a configuration file, so you can change them to your liking. Also, you can add more options to the game, without changing the code. The game is played in the console, so you can play it on any OS.

## Game Rule File
This Game uses this file to determine the outcome of the game. The file is a CSV file with the following structure:
```text
|x        |rock|paper|scissors|fountain|
|rock     |T   |L    |W       |L       |
|paper    |W   |T    |L       |W       |
|scissors |L   |W    |T       |L       |
|fountain |W   |L    |W       |T       |
```
Each cell represents the outcome when the row's choice confronts the column's choice. 'T' stands for a tie, 'L' for a loss, and 'W' for a win. For example, if the player chooses 'rock' and the computer chooses 'paper', the player loses because the cell at 'rock' row and 'paper' column is 'L'.

## Installation and Usage

1. Clone the repository to your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/JanoschA/rock-paper-scissors.git
```

1. Navigate to the project directory:
```bash
cd rock-paper-scissors
```
1. Run the game using Python:
```bash
python3 main.py
```

## Example Game Outputs
```
Welcome to Rock, Paper, Scissors!
Here are the rules:
You need to choose one of the following: rock, paper, or scissors.
But beware, there are other options too!
Enter your choice: paper
Your choice is paper.
The computer's choice is scissors.
You lose!
Do you want to play again? (yes/no): no
Thank you for playing!
```

## License

This project is licensed under the MIT License.

## Acknowledgements

This project was inspired by [this article](https://bootcamp.cvn.columbia.edu/blog/python-projects-for-beginners-to-gain-skills/). The original code [here](https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/) was refactored to improve readability and maintainability.