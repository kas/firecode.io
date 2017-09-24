# 3.4 Make Palindrome

def is_palindrome(input):
    for i in range(0, len(input) // 2):
        if input[len(input) - 1 - i] != input[i]:
            return False

    return True


def make_palindrome(input):
    if is_palindrome(input):
        return input

    input += input[::-1][1:]

    return input
