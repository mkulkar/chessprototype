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
    final_str = '=' * len(board) + '\n'
    for r, row in enumerate(board):
        row_str = row[0]
        for c, cell in enumerate(row):
            if c == 0:
                continue
            row_str += ' | ' + row[c]
        final_str += row_str + '\n'
    final_str += '=' * len(board)


print(board)
