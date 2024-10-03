# Prime Game

## Game Description

Maria and Ben are playing a game. The game is played with consecutive integers starting from 1 up to and including `n`. They take turns picking prime numbers from the set and removing that number and its multiples from the set. The player that cannot make a move loses.

- Maria always goes first.
- Both players play optimally.
- The player who cannot make a move loses the game.

## Task

Given `x` rounds of the game where `n` may be different for each round, determine who wins the most rounds. If Maria wins more rounds, return `"Maria"`. If Ben wins more rounds, return `"Ben"`. If it's a tie, return `None`.

## How to Run

You can test the solution by running the `main_0.py` file. Make sure all files are executable:

```bash
chmod +x main_0.py
chmod +x 0-prime_game.py
./main_0.py
