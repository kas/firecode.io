# 1.6 Repeated Elements in Array

def duplicate_items(list_numbers):
    dictionary = {}
    duplicates = []

    for number in list_numbers:
        if str(number) in dictionary:
            dictionary[str(number)] += 1
        else:
            dictionary[str(number)] = 1
    
    for number, count in dictionary.items():
        if count > 1:
            duplicates.append(number)

    duplicates.sort()

    return duplicates

duplicate_list = [1, 1, 2, 3, 4, 4]
print(duplicate_items(duplicate_list))

