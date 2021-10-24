#! usr/bin/env python3

board = [['R', 'K', 'B', 'C', 'Q', 'B', 'K', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'K', 'B', 'C', 'Q', 'B', 'K', 'R']]


class Piece(object):
    # TODO: _name should be an enum value
    def __init__(self, _name, _color):
        self.name = _name
        self.color = _color

    def __repr__(self):
        should_caps = True if self.color == 'black' else False
        output = self.name[0].upper() if should_caps else self.name[0].lower()
        return output


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


# print_board(board)
p = Piece("knight", "white")
print(p)
