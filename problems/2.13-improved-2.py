# 2.13 Numbers and Ranges ...

def find_range(input_list, input_number):
    first = 0
    lower_bound = -1
    upper_bound = -1
    last = len(input_list) - 1

    while first < last:
        mid = (first + last) / 2

        if input_list[mid] < input_number:
            first = mid + 1
        else:
            last = mid

    if input_list[first] != input_number:
        return Range()
    else:
        lower_bound = first

    first = 0
    last = len(input_list) - 1

    while first < last:
        mid = (first + last) / 2

        if input_list[mid] < input_number + 1
            first = mid + 1
        else:
            last = mid

    if input_list[first] == input_number:
        upper_bound = first
    else:
        upper_bound = first - 1

    return Range(lower_bound, upper_bound)

