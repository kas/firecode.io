# 1.2 Palindrome Tester

def is_palindrome(input_string):
    if not input_string:
        return True
    elif input_string[::-1] != input_string:
        return False
    return True

