import config as c
import random as r


def checkIfPlayerWon(moves):
    lines = [m[0:1] for m in moves]
    cols = [m[1:2] for m in moves]
    for line in ['a', 'b', 'c']:
        if lines.count(line) == 3:
            return True
    for col in ['1', '2', '3']:
        if cols.count(col) == 3:
            return True
    if {'a1', 'b2' 'c3'}.issubset(moves):
        return True
    elif {'a3', 'b2', 'c1'}.issubset(moves):
        return True
    return False


def botWinsOrBlocks(moves):
    for m_1 in moves:
        for m_2 in moves:  # comparisons should be optimized
            if m_1 != m_2:
                if m_1[0:1] == m_2[0:1]:
                    nm_col = '123'.replace(m_1[1:2], '')
                    nm_col = nm_col.replace(m_2[1:2], '')
                    next_move = m_1[0:1] + nm_col
                    if next_move in c.possible_moves:
                        return next_move
                elif m_1[1:2] == m_2[1:2]:
                    nm_line = 'abc'.replace(m_1[0:1], '')
                    nm_line = nm_line.replace(m_2[0:1], '')
                    next_move = nm_line + m_1[1:2]
                    if next_move in c.possible_moves:
                        return next_move
                elif ((m_1 == 'b2' and m_2 in c.corners) or
                        ''.join(sorted(m_1+m_2)) == '13ac'):
                    nm_col = '123'.replace(m_1[1:2], '')
                    nm_col = nm_col.replace(m_2[1:2], '')
                    nm_line = 'abc'.replace(m_1[0:1], '')
                    nm_line = nm_line.replace(m_2[0:1], '')
                    next_move = nm_line + nm_col
                    if next_move in c.possible_moves:
                        return next_move
    return False


def goodMove(moves):
    good_moves = set()
    for m in moves:
        if len(c.player_moves) == 2 and 'b2' in c.player_moves:
            player_move_2 = ''.join(c.player_moves).replace('b2', '')
            if player_move_2 in c.corners and m in c.corners:
                for next_move in c.corners:
                    if next_move in c.possible_moves:
                        return next_move
        elif m == 'b2':
            if {'a1', 'c3'}.issubset(c.possible_moves):
                return r.choice(['a1', 'c3'])
            elif {'a3', 'c1'}.issubset(c.possible_moves):
                return r.choice(['a3', 'c1'])
        if m in c.corners:
            good_moves = {'b2', 'ac13'.replace(m[0:1], '').replace(m[1:2], '')}
            if good_moves.issubset(c.possible_moves):
                return r.choice(list(good_moves))
        gm_cols = '123'.replace(m[1:2], '')
        good_moves = {m[0:1] + gm_cols[0:1], m[0:1] + gm_cols[1:2]}
        if good_moves.issubset(c.possible_moves):
            return r.choice(list(good_moves))
        gm_lines = 'abc'.replace(m[0:1], '')
        good_moves = {gm_lines[0:1] + m[1:2], gm_lines[1:2] + m[1:2]}
        if good_moves.issubset(c.possible_moves):
            return r.choice(list(good_moves))
    return r.choice(list(c.possible_moves))


def updateBoard(last_move):
    if last_move != 'start':
        if len(c.possible_moves) % 2 == 0:
            c.e[last_move] = 'X'
            c.bot_moves.add(last_move)
        else:
            c.e[last_move] = 'O'
            c.player_moves.add(last_move)
        c.possible_moves.remove(last_move)
    print("\n   1   2   3\n" +
          "a _" + c.e['a1'] + "_|_" + c.e['a2'] + "_|_" + c.e['a3'] + "_\n" +
          "b _" + c.e['b1'] + "_|_" + c.e['b2'] + "_|_" + c.e['b3'] + "_\n" +
          "c  " + c.e['c1'] + " | " + c.e['c2'] + " | " + c.e['c3'] + " \n")
