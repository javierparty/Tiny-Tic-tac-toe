import random as r
import operations as op

op.updateBoard('start')

while op.possible_moves:
    move = input("Your turn! ("+(', '.join(op.possible_moves))+"): ")
    while move not in op.possible_moves:
        print('Invalid move!')
        op.updateBoard('start')
        move = input("Your turn! ("+(', '.join(op.possible_moves))+"): ")
    else:
        op.updateBoard(move)
    if len(op.player_moves) > 2:
        if op.checkIfPlayerWon(op.player_moves):
            print('You won! (Lucky human)')
            exit()
        elif bot_move := op.botWinsOrBlocks(op.bot_moves):
            op.updateBoard(bot_move)
            print('I won!')
            exit()
    if len(op.player_moves) > 1:
        if block := op.botWinsOrBlocks(op.player_moves):
            bot_move = block
        else:
            bot_move = op.goodMove(op.bot_moves)
        op.updateBoard(bot_move)
    else:
        if move == 'b2':
            bot_move = r.choice(list(op.corners))
        else:
            bot_move = 'b2'
        op.updateBoard(bot_move)
    if len(op.player_moves) == 4:
        print('You cannot win, human!')
        exit()
