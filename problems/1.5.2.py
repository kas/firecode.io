# 1.5 Find One Missing Number from 1 to 10

def find_missing_number(list_numbers):
    list_sum = 0

    for number in list_numbers:
        list_sum += number

    return 55 - list_sum
