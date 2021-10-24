#! usr/bin/env python3

board = [['r', 'k', 'b', 'c', 'q', 'b', 'k', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'K', 'B', 'C', 'Q', 'B', 'K', 'R']]


def print_board(board: list):
    final_str = '    ' + 'H   G   F   E   D   C   B   A' + '\n' + ' ' * 2 + '-' * 33 + '\n'
    for r, row in enumerate(board):
        row_str = str(r + 1) + ' | ' + str(row[0])
        for c, cell in enumerate(row):
            if c == 0:
                continue
            row_str += ' | ' + row[c]
        row_str += ' | '
        final_str += row_str + '\n' + ' ' * 2 + "-" * 33 + '\n'
    print(final_str)


print_board(board)
