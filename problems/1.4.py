# 1.4 Binary Representation

def get_binary(number):
    binary = None

    if number % 2 != 0:
        binary = 1
    else:
        binary = 0

    return binary

def dec_to_bin(number):
    binary_representation = ''
    remainders_stack = []
    
    while number > 1:
        remainders_stack.append(get_binary(number))

        number /= 2
        
        number = int(number)
    
    remainders_stack.append(get_binary(number))
    
    while remainders_stack:
        binary_representation += str(remainders_stack.pop())
    
    return binary_representation

print(dec_to_bin(5))
