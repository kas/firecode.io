# 1.7 Flip it!

def flip_vertical_axis(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    odd = False

    if columns % 2 != 0:
        odd = True

    for row in range(0, rows):
        middle = None
        new_row = []
        middle_found = False

        for column in range((columns // 2), columns):
            # finish first half of new row

            if odd and not middle_found:
                middle = matrix[row][column]
                middle_found = True
                continue

            new_row.append(matrix[row][column])

        if odd:
            new_row.append(middle)

        for column in range(0, columns // 2):
            new_row.append(matrix[row][column])

        matrix[row] = new_row

