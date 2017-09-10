# 1.2 Palindrome Tester

def is_palindrome(input_string):
    length = len(input_string)

    palindrome = True

    for i in range(0, length // 2):
        if input_string[i] != input_string[length - i - 1]:
            palindrome = False

    return palindrome

