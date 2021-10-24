#! usr/bin/env python3

board = [['R', 'K', 'B', 'C', 'Q', 'B', 'K', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'K', 'B', 'C', 'Q', 'B', 'K', 'R']]


def print_board(board: list):
    final_str = '    ' + '=' * 30 + '\n'
    for r, row in enumerate(board):
        row_str = '{} ~ '.format(r +1)
        row_str += row[0]
        for c, cell in enumerate(row):
            if c == 0:
                continue
            row_str += ' | ' + row[c]
        final_str += row_str + '\n' + '    ' + "-" * 30 + '\n'
    final_str += '    ' + '=' * 30 + '\n' + '    H   G   F   E   D   C   B   A'
    print(final_str)


print_board(board)
