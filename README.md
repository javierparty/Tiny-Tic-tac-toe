# Tiny Tic-tac-toe

A command-line Tic-tac-toe game written in Python with a rule-based 
bot opponent. The bot plays through five distinct stages, applying 
different strategies depending on the state of the board.

Built as a Python practice exercise, focusing on game logic, modular 
code organisation, and algorithm design.

![ttt](https://user-images.githubusercontent.com/114657212/194425053-91f98daf-d1ed-400b-b4df-3bd62cfa2663.png)

---

## How it works

The human player always goes first. The bot responds according to 
the current game stage:

1. **Opening** — bot responds to center or corner openings with a 
   defined strategy
2. **Mid-game** — bot blocks the player's threats and pursues its 
   own winning lines
3. **End-game** — bot checks for a win or forced draw

The game logic is split across two files: `main.py` handles the game 
loop, `operations.py` contains the board and strategy functions.

---

## Usage
```bash
python main.py
```

---

## Tech Stack

Python · CLI · Game logic · Modular design · Random
