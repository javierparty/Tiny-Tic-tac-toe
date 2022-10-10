import random as r
import config as c
import operations as op

op.updateBoard('start')
while c.possible_moves:
    move = input("Your turn! ("+(', '.join(c.possible_moves))+"): ")
    while move not in c.possible_moves:
        print('Invalid move!')
        op.updateBoard('start')
        move = input("Your turn! ("+(', '.join(c.possible_moves))+"): ")
    else:
        op.updateBoard(move)
    if len(c.player_moves) > 2:
        if op.checkIfPlayerWon(c.player_moves):
            print('You won! (Lucky human)')
            exit()
        elif bot_move := op.botWinsOrBlocks(c.bot_moves):
            op.updateBoard(bot_move)
            print('I won!')
            exit()
    if len(c.player_moves) > 1:
        if block := op.botWinsOrBlocks(c.player_moves):
            bot_move = block
        else:
            bot_move = op.goodMove(c.bot_moves)
        op.updateBoard(bot_move)
    else:
        if move == 'b2':
            bot_move = r.choice(list(c.corners))
        else:
            bot_move = 'b2'
        op.updateBoard(bot_move)
    if len(c.player_moves) == 4:
        print('You cannot win, human!')
        exit()
