################################################################################
# Disguiseid
#
# Disguiseid is a tool for converting an integer into a psuedo random id. Its
# purpose is to disguise a lineraly increasing numerical value so that it
# apears to be a random string of letters and numbers. This is not
# cryptographically secure and with enough known consecutive inputs a dedicated
# attacker can easily rebuild the keys. This should only be used to enhance
# the style of a user facing element that could otherwise contain the raw
# integer value.
#
# Every ID and integer have a 1 to 1 mapping, meaning that every ID represents
# a single integer and ever integer represents a single ID.
################################################################################
from typing import List
import keytools


def main():

    key = keytools.generate_key(5)

    key = (0).to_bytes(38, 'big') * 5

    digit_order = keytools.convert_key_to_character_lists(key)

    # print( [compounding_id_to_uint2(compounding_uint_to_id2(i, digit_order), digit_order) for i in range(1000)])
    print( [compounding_uint_to_id2(i, digit_order) for i in range(100)])


    # b = compounding_uint_to_id(1, digit_order)
    # print(b)
    # compounding_id_to_uint(b, digit_order)

# digit_order = [
#     ['W', 'U', 'l', 't', 'V', 'R', '7', 'Y', 'm', 'j', 'i', 'h', 'f', 'E', 'P', 'o', 'c', 'B', '5', 'X', '1', 'n', 'Z', 'q', 's', 'r', '0', 'p', '-', 'C', '2', 'D', 'g', 'G', 'T', 'y', 'I', 'k', 'x', '9', '_', 'u', 'Q', '8', 'J', 'w', 'z', 'A', '4', 'H', 'b', 'v', 'O', 'd', 'N', '3', 'L', 'a', '6', 'e', 'K', 'S', 'F', 'M'],
#     ['7', 'u', 'q', 'j', 'v', 'C', 'h', 'T', 'l', 'd', '-', 'p', 'y', 'J', 'z', 'M', '5', 'F', 'r', 'k', 'Q', 'P', '9', 'N', 'R', '4', 'b', 'H', 'A', '8', 'V', 'G', 'S', 'i', '1', 'B', 'a', 'K', 'X', '2', 'x', 'W', 'Z', 'L', 'O', '3', '_', 'E', 'e', 'c', 't', '6', 's', 'g', 'f', 'm', 'U', 'o', 'I', 'w', 'n', 'Y', '0', 'D'],
#     ['e', '1', 'G', '7', 'c', 'd', 't', 'C', 'W', 'A', 'U', 'Q', 'o', '9', 'N', '5', 'i', 'a', '-', 'K', '3', 'V', 'H', 'I', 'S', '4', 'n', 'B', '6', 'w', 'X', 'M', 'E', 'T', 'h', 'm', 'u', '8', 'J', 'k', 'z', 'D', 'v', 'g', 'q', 'b', 'P', 'f', 'l', 'p', 'O', 'y', 'Z', 'j', 'x', '2', 'L', 'F', 'Y', 'R', 's', 'r', '_', '0'],
#     ['O', 'h', '-', 'Y', 'I', 'J', 'm', '6', 'F', 'W', '1', 'p', 'i', '2', 's', 'E', 'g', 'n', 'R', 'u', 'q', 'A', 'H', '4', 'G', '0', 'w', 'j', 'y', '5', 'C', '9', 'r', 'a', 'c', 't', 'd', 'b', 'D', 'N', 'f', 'B', '7', 'l', 'S', 'z', 'o', 'P', '_', 'Q', '3', 'U', '8', 'X', 'e', 'k', 'V', 'x', 'T', 'v', 'K', 'M', 'L', 'Z'],
#     ['2', 'N', 'P', 'e', 'K', 'u', 's', 'U', 'c', 'n', 'q', 'g', '3', 'W', 'L', 'k', 'r', 'M', 'l', '_', 'y', 'Z', 'i', '5', 'x', 'A', 'j', 'S', '4', 'B', 'm', 'V', '0', 'J', 'p', '1', 'T', 'H', 'O', '6', 'v', 'h', 'G', 'F', 'E', 'Y', '-', 'f', 'R', '8', '7', 'D', 'b', '9', 'Q', 'o', 'C', 'w', 'z', 'I', 'd', 'a', 't', 'X'],
# ]

# simplified digit order to understand the modification algorithm
# digit_order = [
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
#     ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","-","_"],
# ]


################################################################################
# uint_to_id
#
# Transforms an unsigned integer into the disguised stringy id.
################################################################################
def uint_to_id(integer: int, digit_order: List[str]) -> str:
    base_64 = uint_to_base64(integer)
    base_64 = pad_zeros(base_64)

    for i in range(1,5):
        base_64[i] = (base_64[i] + base_64[i-1]) % 64

    identifier = ""
    for i in range(5):
        identifier += digit_order[i][base_64[i]]

    return identifier



def compounding_uint_to_id(integer: int, digit_order: List[str]) -> str:
    base_64 = uint_to_base64(integer)
    base_64 = pad_zeros(base_64)

    offset = base_64[0]+1
    for i in range(1,5):
        base_64[i] = (base_64[i] + offset) % 64
        offset+=base_64[i]

    identifier = ""
    for i in range(5):
        identifier += digit_order[i][base_64[i]]

    return identifier



import math
def compounding_uint_to_id2(integer: int, digit_order: List[str]) -> str:
    length = len(digit_order)

    base_64 = uint_to_base64(integer)
    base_64 = pad_zeros(base_64, length)

    for late_index in reversed(range(1, length)):
        for early_index in range(0, late_index):
            base_64[late_index] = base_64[late_index] + (base_64[early_index] + 1) * (late_index - early_index)
        base_64[late_index] = base_64[late_index] % 64

    # for early_index in range(0, length):
    #     base_64[early_index] = base_64[early_index] % 64
    #     for late_index in range(early_index+1, length):
    #         base_64[late_index] = base_64[late_index] + (base_64[early_index] + 1) * (late_index - early_index)

    identifier = ""
    for i in range(length):
        identifier += digit_order[i][base_64[i]]

    return identifier



################################################################################
# id_to_uint
#
# Transforms a disguised stringy id into a unsigned integer
################################################################################
def id_to_uint(identifier: str, digit_order: List[str]) -> int:
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

def compounding_id_to_uint(identifier: str, digit_order: List[str]) -> int:
    offset_base_64 = []
    for i in range(5):
        offset_base_64.append(digit_order[i].index(identifier[i]))

    base_64 = [offset_base_64[0]]
    offset = offset_base_64[0] + 1
    for i in offset_base_64[1:]:
        base_64.append((i - offset)%64)
        offset += i

    modifier = 1

    integer = 0

    for digit in base_64:
        integer += digit * modifier
        modifier *= 64

    return integer




def compounding_id_to_uint2(identifier: str, digit_order: List[str]) -> int:
    length = len(identifier)

    base_64 = []
    for i in range(length):
        base_64.append(digit_order[i].index(identifier[i]))

    for early_index in range(0, length):
        base_64[early_index] = base_64[early_index] % 64
        for late_index in range(early_index+1, length):
            base_64[late_index] = base_64[late_index] - (base_64[early_index] + 1) * (late_index - early_index)

    # Decode the values into an int
    modifier = 1
    integer = 0
    for digit in base_64:
        integer += digit * modifier
        modifier *= 64

    return integer






################################################################################
# int_to_base64
#
# Converts a regular unsigned integer to a list of base64 digits. The first
# element in the returned list is the least significant digit. If a negative
# number is received it will error.
#
# TODO: Because this is just base64 now instead of any base we can take
# advantage of bit-slicing and bitwise operators to make this faster.
################################################################################
def uint_to_base64(x: int) -> List[int]:
    if x < 0:
        raise ValueError("Cannot turn negative int into base64.")
    elif x == 0:
        return [0]

    digits = []

    while x:
        digits.append(int(x % 64))
        x = int(x / 64)

    return digits


################################################################################
# pad_zeros
#
# A helper function to add 0's to the end of the digit list to make it five
# elements long.
################################################################################
def pad_zeros(array: List[int], length:int=5) -> List[int]:
    delta_length = length - len(array)

    for _ in range(delta_length):
        array.append(0)

    return array


if __name__ == "__main__":
    main()