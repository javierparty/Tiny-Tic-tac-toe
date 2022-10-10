import random as r

possible_moves = {'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'}
e = {m: ' ' for m in possible_moves}
corners = {'a1', 'a3', 'c1', 'c3'}
player_moves = set()
bot_moves = set()


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
                    if next_move in possible_moves:
                        return next_move
                elif m_1[1:2] == m_2[1:2]:
                    nm_line = 'abc'.replace(m_1[0:1], '')
                    nm_line = nm_line.replace(m_2[0:1], '')
                    next_move = nm_line + m_1[1:2]
                    if next_move in possible_moves:
                        return next_move
                elif ((m_1 == 'b2' and m_2 in corners) or
                        ''.join(sorted(m_1+m_2)) == '13ac'):
                    nm_col = '123'.replace(m_1[1:2], '')
                    nm_col = nm_col.replace(m_2[1:2], '')
                    nm_line = 'abc'.replace(m_1[0:1], '')
                    nm_line = nm_line.replace(m_2[0:1], '')
                    next_move = nm_line + nm_col
                    if next_move in possible_moves:
                        return next_move
    return False


def goodMove(moves):
    good_moves = set()
    for m in moves:
        if len(player_moves) == 2 and 'b2' in player_moves:
            player_move_2 = ''.join(player_moves).replace('b2', '')
            if player_move_2 in corners and m in corners:
                for next_move in corners:
                    if next_move in possible_moves:
                        return next_move
        elif m == 'b2':
            if {'a1', 'c3'}.issubset(possible_moves):
                return r.choice(['a1', 'c3'])
            elif {'a3', 'c1'}.issubset(possible_moves):
                return r.choice(['a3', 'c1'])
        if m in corners:
            good_moves = {'b2', 'ac13'.replace(m[0:1], '').replace(m[1:2], '')}
            if good_moves.issubset(possible_moves):
                return r.choice(list(good_moves))
        gm_cols = '123'.replace(m[1:2], '')
        good_moves = {m[0:1] + gm_cols[0:1], m[0:1] + gm_cols[1:2]}
        if good_moves.issubset(possible_moves):
            return r.choice(list(good_moves))
        gm_lines = 'abc'.replace(m[0:1], '')
        good_moves = {gm_lines[0:1] + m[1:2], gm_lines[1:2] + m[1:2]}
        if good_moves.issubset(possible_moves):
            return r.choice(list(good_moves))
    return r.choice(list(possible_moves))


def updateBoard(last_move):
    if last_move != 'start':
        if len(possible_moves) % 2 == 0:
            e[last_move] = 'X'
            bot_moves.add(last_move)
        else:
            e[last_move] = 'O'
            player_moves.add(last_move)
        possible_moves.remove(last_move)
    print("\n   1   2   3\n" +
          "a _" + e['a1'] + "_|_" + e['a2'] + "_|_" + e['a3'] + "_\n" +
          "b _" + e['b1'] + "_|_" + e['b2'] + "_|_" + e['b3'] + "_\n" +
          "c  " + e['c1'] + " | " + e['c2'] + " | " + e['c3'] + " \n")
