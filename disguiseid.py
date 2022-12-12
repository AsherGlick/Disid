import random
# digits = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"]
# random.shuffle(digits)
# print(digits)








digit_order = [
    ['W', 'U', 'l', 't', 'V', 'R', '7', 'Y', 'm', 'j', 'i', 'h', 'f', 'E', 'P', 'o', 'c', 'B', '5', 'X', '1', 'n', 'Z', 'q', 's', 'r', '0', 'p', '-', 'C', '2', 'D', 'g', 'G', 'T', 'y', 'I', 'k', 'x', '9', '_', 'u', 'Q', '8', 'J', 'w', 'z', 'A', '4', 'H', 'b', 'v', 'O', 'd', 'N', '3', 'L', 'a', '6', 'e', 'K', 'S', 'F', 'M'],
    ['7', 'u', 'q', 'j', 'v', 'C', 'h', 'T', 'l', 'd', '-', 'p', 'y', 'J', 'z', 'M', '5', 'F', 'r', 'k', 'Q', 'P', '9', 'N', 'R', '4', 'b', 'H', 'A', '8', 'V', 'G', 'S', 'i', '1', 'B', 'a', 'K', 'X', '2', 'x', 'W', 'Z', 'L', 'O', '3', '_', 'E', 'e', 'c', 't', '6', 's', 'g', 'f', 'm', 'U', 'o', 'I', 'w', 'n', 'Y', '0', 'D'],
    ['e', '1', 'G', '7', 'c', 'd', 't', 'C', 'W', 'A', 'U', 'Q', 'o', '9', 'N', '5', 'i', 'a', '-', 'K', '3', 'V', 'H', 'I', 'S', '4', 'n', 'B', '6', 'w', 'X', 'M', 'E', 'T', 'h', 'm', 'u', '8', 'J', 'k', 'z', 'D', 'v', 'g', 'q', 'b', 'P', 'f', 'l', 'p', 'O', 'y', 'Z', 'j', 'x', '2', 'L', 'F', 'Y', 'R', 's', 'r', '_', '0'],
    ['O', 'h', '-', 'Y', 'I', 'J', 'm', '6', 'F', 'W', '1', 'p', 'i', '2', 's', 'E', 'g', 'n', 'R', 'u', 'q', 'A', 'H', '4', 'G', '0', 'w', 'j', 'y', '5', 'C', '9', 'r', 'a', 'c', 't', 'd', 'b', 'D', 'N', 'f', 'B', '7', 'l', 'S', 'z', 'o', 'P', '_', 'Q', '3', 'U', '8', 'X', 'e', 'k', 'V', 'x', 'T', 'v', 'K', 'M', 'L', 'Z'],
    ['2', 'N', 'P', 'e', 'K', 'u', 's', 'U', 'c', 'n', 'q', 'g', '3', 'W', 'L', 'k', 'r', 'M', 'l', '_', 'y', 'Z', 'i', '5', 'x', 'A', 'j', 'S', '4', 'B', 'm', 'V', '0', 'J', 'p', '1', 'T', 'H', 'O', '6', 'v', 'h', 'G', 'F', 'E', 'Y', '-', 'f', 'R', '8', '7', 'D', 'b', '9', 'Q', 'o', 'C', 'w', 'z', 'I', 'd', 'a', 't', 'X'],
]

# simplified digit order to understand the modification algorithm
# digit_order = [
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
# ]


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return [0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(int(x % base))
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    # digits.reverse()

    return digits



def pad_zero_array(array):
    length = 5

    delta_length = length - len(array)

    for i in range(delta_length):
        array.append(0)

    return array



def int_to_id(integer):
    base_64 = int2base(integer, 64)
    base_64 = pad_zero_array(base_64)

    for i in range(1,5):
        base_64[i] = (base_64[i] + base_64[i-1]) % 64

    identifier = ""
    for i in range(5):
        identifier += digit_order[i][base_64[i]]

    return identifier
    # print(identifier)




def id_to_int(identifier):
    base_64 = []
    for i in range(5):
        base_64.append(digit_order[i].index(identifier[i]))

    for i in range(4,0,-1):
        base_64[i] = (base_64[i] - base_64[i-1]) % 64

    modifier = 1

    integer = 0

    for digit in base_64:
        integer += digit * modifier
        modifier *= 64

    return integer




# start_id = 99999999
# for i in range(10):
#     id_code = int_to_id(start_id + i)
#     print(i+start_id, id_code, id_to_int(id_code))


# id_code = int_to_id(1)
# print(1, id_code, id_to_int(id_code))






print( [int_to_id(i) for i in range(1000)] )