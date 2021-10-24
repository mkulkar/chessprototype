#! usr/bin/env python3
class Piece(object):
    # TODO: _name should be an enum value
    def __init__(self, _name, _color):
        self.name = _name
        self.color = _color

    def __repr__(self):
        should_caps = True if self.color == 'black' else False
        output = self.name[0].upper() if should_caps else self.name[0].lower()
        return output

    def __str__(self):
        return self.__repr__()



board = [[Piece('rook','white'), Piece('knight','white'), Piece('bishop','white'), Piece('cing','white'), Piece('queen','white'), Piece('bishop','white'), Piece('knight','white'), Piece('rook','white')],
         [Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white'), Piece('pawn','white')],
         [Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black')],
         [Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white')],
         [Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black')],
         [Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white'), Piece('empty','black'), Piece('empty','white')],
         [Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black'), Piece('pawn','black')],
         [Piece('rook','black'), Piece('knight','black'), Piece('bishop','black'), Piece('cing','black'), Piece('queen','black'), Piece('bishop','black'), Piece('knight','black'), Piece('rook','black')]]


def print_board(board: list):
    final_str = '    ' + 'H   G   F   E   D   C   B   A' + '\n' + ' ' * 2 + '-' * 33 + '\n'
    for r, row in enumerate(board):
        row_str = str(r + 1) + ' | ' + str(row[0])
        for c, cell in enumerate(row):
            if c == 0:
                continue
            row_str += ' | ' + str(row[c])
        row_str += ' | '
        final_str += row_str + '\n' + ' ' * 2 + "-" * 33 + '\n'
    print(final_str)


print_board(board)
p = Piece("knight", "white")
print(p)
