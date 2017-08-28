# 1.1 Reverse a String

def reverse_string(a_string):
    if not a_string:
        return None

    a_list = []
    another_string = ''

    for c in a_string:
        a_list.append(c)

    while a_list:
        another_string += str(a_list.pop())

    return another_string

