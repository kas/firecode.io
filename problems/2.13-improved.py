# 2.13 Numbers and Ranges ...

def find_range(input_list, input_number):
    begin = None
    end = None

    for i in range(0, len(input_list)):
        if input_list[i] == input_number:
            if not begin:
                begin = i

            end = i
        elif input_list[i] > input_number:
            break

    return Range(begin, end)

