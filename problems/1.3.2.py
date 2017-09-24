# 1.3 Horizontal Flip

import math

def flip_horizontal_axis(matrix):
    rows = len(matrix)

    if rows <= 1:
        return

    columns = len(matrix[0])

    jump_rows = int(rows / 2)

    if (rows % 2) != 0:
        jump_rows = int(math.ceil(rows / 2))

    for row in range(0, rows // 2):
        temp = matrix[row + jump_rows]
        matrix[row + jump_rows] = matrix[row]
        matrix[row] = temp
