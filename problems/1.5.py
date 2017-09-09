# 1.5 Find One Missing Number from 1 to 10

def find_missing_number(list_numbers):
    dictionary = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, '10': None}

    # have to traverse list once, O(n) complexity
    for number in list_numbers:
        dictionary.pop(str(number))

    for key in dictionary:
        return int(key)

