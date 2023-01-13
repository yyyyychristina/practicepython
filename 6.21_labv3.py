def int_to_reverse_binary(integer_value):
    result = ''
    while integer_value > 0:
        result += str(integer_value % 2)
        integer_value = integer_value // 2
    return result

def string_reverse(input_string):
    result = ''
    for n in reversed(input_string):
        result += n
    return result
        
if __name__ == '__main__':
    integer = int(input())
    string = string_reverse(int_to_reverse_binary(integer))
    
    print(string)
    
