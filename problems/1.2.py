# 1.2 Palindrome Tester

def is_palindrome(input_string):
    if not input_string:
        return True
    
    a_list = []
    reversed_string = ''

    for c in input_string:
        a_list.append(c)

    while a_list:
        reversed_string += str(a_list.pop())
    
    result = input_string == reversed_string

    return result

