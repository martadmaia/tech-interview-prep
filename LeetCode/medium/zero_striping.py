#For each zero in an m x n matrix, set its entire row and column to zero in place.

#Key takeway:
#If a cell is in a row or column that contains a zero, that cell will become a 0
def zero_striping(matrix):
    rows_with_zeros = set()
    columns_with_zeros = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            cell = matrix[row][column]
        
            if cell == 0:
                rows_with_zeros.add(row)
                columns_with_zeros.add(column)

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row in rows_with_zeros or column in columns_with_zeros:
                matrix[row][column] = 0

    return matrix

print(zero_striping(
    [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 15, 15],
        [16, 17, 18, 19, 0]
    ]))

def zero_striping_2(matrix): 
    rows_with_zeros = set()
    columns_with_zeros = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            cell = matrix[row][column]
        
            if cell == 0:
                rows_with_zeros.add(row)
                columns_with_zeros.add(column)

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row in rows_with_zeros or column in columns_with_zeros:
                matrix[row][column] = 0

    return matrix