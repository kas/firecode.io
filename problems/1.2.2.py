# 1.2 Palindrome Tester

def is_palindrome(input_string):
    if input_string == '':
        return True
    elif not input_string:
        return False

    if input_string[::-1] == input_string:
        return True

    return False

