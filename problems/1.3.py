# 1.3 Horizontal Flip

def flip_horizontal_axis(matrix):
    height = len(matrix)

    if height <= 1:
        return

    even = False

    if height % 2 == 0:
        even = True

    upper_bound = height / 2 

    for r in range(0, upper_bound):
        target_r = r + upper_bound

        if not even:
            target_r += 1

        temp = matrix[target_r]

        matrix[target_r] = matrix[r]

        matrix[r] = temp

