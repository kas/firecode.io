# 1.3 Horizontal Flip

def flip_horizontal_axis(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    row_add = rows / 2

    if rows % 2 != 0:
        row_add += 1

    for row in range(0, rows / 2):
        for column in range(row, columns):
            temp = matrix[row][column]
            matrix[row][column] = matrix[row + row_add][column]
            matrix[row + row_add][column] = temp

