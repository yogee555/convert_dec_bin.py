# python program to covert decimal to binary
def decimal_to_binary(n):
    return bin(n).replace("0b","")
if __name__ == '__main__':
    print(decimal_to_binary(8))
    print(decimal_to_binary(18))
    print(decimal_to_binary(7))