# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.


#Hashset and not map
#We just need to exclude duplicates existing
#we'll need 9 sets for the rows
#9 sets for the columns
#9 sets for the subgrids

def valid_sudoku(board):
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    
    for row in range(9):
        
        for column in range(9):
            num_in_cell = board[row][column]

            if num_in_cell == ".":
                continue
            
            subgrid_row, subgrid_column = row // 3, column // 3

            if num_in_cell in row_sets[row]:
                return False
            if num_in_cell in column_sets[column]:
                return False
            if num_in_cell in subgrid_sets[subgrid_row][subgrid_column]:
                return False

            row_sets[row].add(num_in_cell)
            column_sets[column].add(num_in_cell)
            subgrid_sets[subgrid_row][subgrid_column].add(num_in_cell)

    return True

print(valid_sudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))