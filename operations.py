import config as c
import random


def checkIfPlayerWon(moves):
    lines = []
    cols = []
    for m in moves:
        lines.append(m[0:1])
        cols.append(m[1:2])
    for line in ['a', 'b', 'c']:
        if lines.count(line) == 3:
            return True
    for col in ['1', '2', '3']:
        if cols.count(col) == 3:
            return True
    if {'a1', 'b2' 'c3'}.issubset(set(moves)):
        return True
    elif {'a3', 'b2', 'c1'}.issubset(set(moves)):
        return True
    return False


def botWinsOrBlocks(moves):
    for m_1 in moves:
        for m_2 in moves:  # compares can be optimized
            if m_1 != m_2:
                if m_1[0:1] == m_2[0:1]:
                    next_move_col = '123'.replace(m_1[1:2], '')
                    next_move_col = next_move_col.replace(m_2[1:2], '')
                    next_move = m_1[0:1] + next_move_col
                    if next_move in c.possible_moves:
                        return next_move
                elif m_1[1:2] == m_2[1:2]:
                    next_move_line = 'abc'.replace(m_1[0:1], '')
                    next_move_line = next_move_line.replace(m_2[0:1], '')
                    next_move = next_move_line + m_1[1:2]
                    if next_move in c.possible_moves:
                        return next_move
                elif ((m_1 == 'b2' and m_2 in c.corners) or
                        ''.join(sorted(m_1+m_2)) == '13ac'):
                    next_move_col = '123'.replace(m_1[1:2], '')
                    next_move_col = next_move_col.replace(m_2[1:2], '')
                    next_move_line = 'abc'.replace(m_1[0:1], '')
                    next_move_line = next_move_line.replace(m_2[0:1], '')
                    next_move = next_move_line + next_move_col
                    if next_move in c.possible_moves:
                        return next_move
    return False


def goodMove(moves):
    good_moves = ['', '']
    print('inicia goodMove')
    for m in moves:
        if len(c.player_moves) == 2 and 'b2' in c.player_moves:
            print('walla 1')
            player_move_2 = ''.join(c.player_moves).replace('b2', '')
            if player_move_2 in c.corners and m in c.corners:
                print('walla 2')
                for next_move in c.corners:
                    print('walla 3')
                    if next_move in c.possible_moves:
                        print('walla 4')
                        return next_move
        elif m == 'b2':
            print('turu 1')
            if {'a1', 'c3'}.issubset(c.possible_moves):
                print('turu 1 A')
                return random.choice(['a1', 'c3'])
            elif {'a3', 'c1'}.issubset(c.possible_moves):
                print('turu 1 B')
                return random.choice(['a3', 'c1'])
        if m in c.corners:
            print('turu 2')
            good_moves[0] = 'b2'
            good_moves[1] = 'ac'.replace(m[0:1], '') + '13'.replace(m[1:2], '')
            if {good_moves[0], good_moves[1]}.issubset(c.possible_moves):
                print('turu 2 A')
                return random.choice(good_moves)
        print('turu 3')
        good_moves_cols = '123'.replace(m[1:2], '')
        good_moves[0] = m[0:1] + good_moves_cols[0:1]
        good_moves[1] = m[0:1] + good_moves_cols[1:2]
        if {good_moves[0], good_moves[1]}.issubset(c.possible_moves):
            print('turu 3 A')
            return random.choice(good_moves)
        print('turu 4')
        good_moves_lines = 'abc'.replace(m[0:1], '')
        good_moves[0] = good_moves_lines[0:1] + good_moves_lines[0:1]
        good_moves[1] = good_moves_lines[1:2] + good_moves_lines[1:2]
        if {good_moves[0], good_moves[1]}.issubset(c.possible_moves):
            print('turu 4 A')
            return random.choice(good_moves)
    return random.choice(c.possible_moves)


def updateBoard(last_move):
    if last_move != 'start':
        if len(c.possible_moves) % 2 == 0:
            c.e[last_move] = 'X'
            c.bot_moves.append(last_move)
        else:
            c.e[last_move] = 'O'
            c.player_moves.append(last_move)
        c.possible_moves.remove(last_move)
    print(" ")
    print("   1   2   3 ")
    print("a _"+c.e['a1']+"_|_"+c.e['a2']+"_|_"+c.e['a3']+"_")
    print("b _"+c.e['b1']+"_|_"+c.e['b2']+"_|_"+c.e['b3']+"_")
    print("c  "+c.e['c1']+" | "+c.e['c2']+" | "+c.e['c3']+" ")
    print(" ")
