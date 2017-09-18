# 3.3 Binary Search

def binary_search(a_list, item):
    if not a_list:
        return False

    middle = len(a_list) // 2

    if a_list[middle] == item:
        return True

    if a_list[middle] < item:
        return binary_search(a_list[middle + 1:], item)

    return binary_search(a_list[:middle], item)

