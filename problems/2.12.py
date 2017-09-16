# 2.12 Max Gain

def max_gain(input_list):
    if not input_list:
        return 0

    maximum_gain = 0
    minimum = input_list[0]

    for i in range(0, len(input_list)):
        if i == 0:
            continue

        current_gain = input_list[i] - minimum

        if current_gain > maximum_gain:
            maximum_gain = current_gain

        if input_list[i] < minimum:
            minimum = input_list[i]

    return maximum_gain

