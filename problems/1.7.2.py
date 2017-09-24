# 1.7 Flip it!

def flip_vertical_axis(matrix):
    height = len(matrix)
    width = len(matrix[0])

    add = width // 2

    if row % 2 != 0:
        add += 1

    for row in range(0, height):
        for column in range(0, width // 2):
            temp = matrix[height][column + add]
            matrix[height][column + add] = matrix[height][column]
            matrix[height][column] = temp
