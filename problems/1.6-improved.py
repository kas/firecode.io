# 1.6 Repeated Elements in Array

def duplicate_items(list_numbers):
    duplicates = []

    list_numbers.sort()

    for i in range(1, len(list_numbers)):
        if list_numbers[i] == list_numbers[i - 1]:
            duplicates.append(list_numbers[i])

    return duplicates
