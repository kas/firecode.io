# 2.5 Merge Integer Ranges

def merge_ranges(input_range_list):
    output_list = []

    lists = len(input_range_list)

    tracking = False
    begin = None

    for i in range(0, lists - 1):
        if not tracking:
            tracking = True
            begin = input_range_list[i].lower_bound

        if input_range_list[i].upper_bound < input_range_list[i + 1].lower_bound:
            # stop tracking, add current tracking to output_list
            tracking = False
            output_list.append([begin, input_range_list[i].upper_bound])

    if tracking:
        output_list.append([begin, input_range_list[lists - 1].upper_bound])
    else:
        output_list.append(input_range_list[lists - 1])

    return output_list
