# A tiny Tic-tac-toe written in a few python lines. 


![ttt](https://user-images.githubusercontent.com/114657212/194425053-91f98daf-d1ed-400b-b4df-3bd62cfa2663.png)


The game has five stages and the bot calculates his move according to the stage of the game. The human player always begins.

## :one: First stage
The bot presents the clean board.

## :two: Second Stage
The bot calculates his first move using two criteria: a) If the player starts on the center (B2), the bot choose a corner randomly. b) If the player starts anywhere else, the bot chooses the center (B2).

## :three: Third stage
The bot checks if the player has played two times in the same row|column|diagonal (RCD). If this is the case, it checks if the third space in that RCD is empty. If it is, it plays on the empty space of that RCD, blocking the strategy of the player. If it is not empty and all the moves are on a diagonal, it chooses one of the two remaining corners randomly. If the player has not played two times in the same RCD, the bot looks for the next RCD that contains its first move and two empty spaces, and plays in one of these two spaces randomly.

## :four: Fourth stage
First, the bot checks if the player has three in a RCD, and therefore has won. If yes, the game is over. If not, it checks if it has two in a RCD. If this is the case, it plays the third spaces in that RCD and wins. If nobody has won, it repeats the procedure of the third stage.

## :five: Fifth stage
The same procedure of the fourth stage but if no body has won, it is a tie and the game is over.
