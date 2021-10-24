#! usr/bin/env python3

class Piece(object):
    curr_id = 0

    # TODO: _name should be an enum value
    def __init__(self, _name, _color):
        self.name = _name
        self.color = _color
        self.id = Piece.curr_id
        Piece.curr_id += 1

    def __repr__(self):
        should_caps = True if self.color == 'black' else False
        output = self.name[0].upper() if should_caps else self.name[0].lower()
        output += "{:0>2d}".format(self.id)
        return output

    def __str__(self):
        return repr(self)[0]


board = [
    [  # 1
        Piece('rook', 'white'),  # H
        Piece('knight', 'white'),  # G
        Piece('bishop', 'white'),  # F
        Piece('cing', 'white'),  # E
        Piece('queen', 'white'),  # D
        Piece('bishop', 'white'),  # C
        Piece('knight', 'white'),  # B
        Piece('rook', 'white')  # A
    ],
    [  # 2
        Piece('pawn', 'white'),  # H
        Piece('pawn', 'white'),  # G
        Piece('pawn', 'white'),  # F
        Piece('pawn', 'white'),  # E
        Piece('pawn', 'white'),  # D
        Piece('pawn', 'white'),  # C
        Piece('pawn', 'white'),  # B
        Piece('pawn', 'white')  # A
    ],
    [  # 3
        None,  # H
        None,  # G
        None,  # F
        None,  # E
        None,  # D
        None,  # C
        None,  # B
        None  # A
    ],
    [  # 4
        None,  # H
        None,  # G
        None,  # F
        None,  # E
        None,  # D
        None,  # C
        None,  # B
        None  # A
    ],
    [  # 5
        None,  # H
        None,  # G
        None,  # F
        None,  # E
        None,  # D
        None,  # C
        None,  # B
        None  # A
    ],
    [  # 6
        None,  # H
        None,  # G
        None,  # F
        None,  # E
        None,  # D
        None,  # C
        None,  # B
        None  # A
    ],
    [  # 7
        Piece('pawn', 'black'),  # H
        Piece('pawn', 'black'),  # G
        Piece('pawn', 'black'),  # F
        Piece('pawn', 'black'),  # E
        Piece('pawn', 'black'),  # D
        Piece('pawn', 'black'),  # C
        Piece('pawn', 'black'),  # B
        Piece('pawn', 'black')  # A
    ],  
    [  # 8
        Piece('rook', 'black'),  # H
        Piece('knight', 'black'),  # G
        Piece('bishop', 'black'),  # F
        Piece('cing', 'black'),  # E
        Piece('queen', 'black'),  # D
        Piece('bishop', 'black'),  # C
        Piece('knight', 'black'),  # B
        Piece('rook', 'black')  # A
    ]
]


def print_board(board: list, repr_mode=False):
    if not repr_mode:
        final_str = '    ' + 'H   G   F   E   D   C   B   A' + '\n' + ' ' * 2 + '-' * 33 + '\n'
    else:
        final_str = '    ' + 'H     G     F     E     D     C     B     A' + '\n' + ' ' * 2 + '-' * 49 + '\n'
    for r, row in enumerate(board):
        if repr_mode:
            row_str = str(
                r + 1) + ' | ' + (repr(row[0]) if row[0] else '   ')
        else:
            row_str = str(r + 1) + ' | ' + (str(row[0]) if row[0] else ' ')
        for c, cell in enumerate(row):
            if c == 0:
                continue
            if repr_mode:
                row_str += ' | ' + (repr(row[c]) if row[c] else '   ')
            else:
                row_str += ' | ' + (str(row[c]) if row[c] else ' ')
        row_str += ' | '
        if repr_mode:
            final_str += row_str + '\n' + ' ' * 2 + "-" * 49 + '\n'
        else:
            final_str += row_str + '\n' + ' ' * 2 + "-" * 33 + '\n'
    print(final_str)


print_board(board, True)
