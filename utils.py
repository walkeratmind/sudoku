"""
Utils for the Game
"""
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]


boxes = cross(rows, cols)
#print(boxes)

# separate rows
row_units = [cross(r, cols) for r in rows]
#separate columns
column_units = [cross(rows, c) for c in cols]
# group square units
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
# Total units list
unitlist = row_units + column_units + square_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
#group boxes that belong to a common unit
# (namely, those that belong to the same row, column, or 3x3 square)
# peers
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)

def display(values):
    """
    Display values as 2D Grid
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
