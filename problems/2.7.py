# 2.7 Find the Transpose of a Square Matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(0, rows):
        for column in range(0, columns):
            # if top left, if bottom right, if odd and element is center element, if column <= row
            if (row == 0 and column == 0) or (row == (rows - 1) and column == (columns - 1)) or (odd and row == ((rows // 2) + 1) and column == ((columns // 2) + 1)) or (column <= row):
                continue

            temp = matrix[column][row]
            matrix[column][row] = matrix[row][column]
            matrix[row][column] = temp
