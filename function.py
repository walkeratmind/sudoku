from utils import *

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

display(grid_values(grid))
grid_with_values = add_values(grid2)

#print("Possible Values")
#possible_values = eliminate(grid_with_values)
#display(possible_values)
#
#print("Updated Values")
#updated_values = only_choice(possible_values)
#display(updated_values)

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False: 
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values; ## Solved
    
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

print("Solved Puzzle")
display(search(grid_with_values))