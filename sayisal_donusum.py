
def binary2decimal(n):
    return int(n, 2)

def hex2Bin(input_line):
    res = bin(int(input_line, 16)).zfill(8)
    return  res
def bin2hex(input_line):
    num = int(input_line, 2)
    # convert int to hexadecimal
    hex_num = hex(num)
    return (hex_num)
def decimal2binary(n):
    return "{0:b}".format(int(n))

def decimalToHexadecimal(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ''
    decimal = int(decimal)
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def HexadecimalTodecimal(decimal):
    table = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11,
             'C': 12, 'D': 13, 'E': 14, 'F': 15}

    hexadecimal = decimal.strip().upper()
    res = 0
    # computing max power value
    size = len(hexadecimal) - 1

    for num in hexadecimal:
        res = res + table[num] * 16 ** size
        size = size - 1

    return res