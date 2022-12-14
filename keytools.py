################################################################################
# Key Tools
#
# This module contains utilities that help with parsing and generating keys
# that can be used for disguiseid. Keys are not required for use but can
# provide a marginally increased level of security. They effectively funciton
# as a cesar cypher for the id which can help disguise the id even more. Adding
# a key does not add any meaninful level of security to the IDs against a
# dedicated attacker however. Disguiseid is not meant to be used in any
# situation where surfacing the plan integer id would not also be surfaced.
################################################################################
from typing import List, Dict
import os


def main():
    key = generate_key(5)

    print(key.hex())

    print(convert_key_to_character_lists(key))

    # mybytes = (factorial(64)-1).to_bytes(38, 'big')
    # permutation_from_index(64, int.from_bytes(mybytes, 'big'))



################################################################################
# generate_key
#
# Generates a new key to be used with disguiseid. Returns a bytes object
# containing a vald 190 byte long key which can be used for a 5 character long
# disguised value unless the size parameter is passed in, in which case a
# different length key will be returned instead.
################################################################################
def generate_key(size: int = 5) -> bytes:
    return b''.join([generate_key_chunk() for _ in range(size)])


################################################################################
# generate_key_chunk
#
# Generates a chunk of the key, representitive of a single permutation of one
# of the characters in the id.
################################################################################
def generate_key_chunk() -> bytes:
    key_chunk = os.urandom(38)
    key_int = int.from_bytes(key_chunk, 'big')
    
    # A slow and dumb way to make sure we have a valid chunk of bytes, but
    # there is only a 0.4% chance of that happening [64!/2^(38*8) = 0.0038]
    # so it will basically have no impact on performance.
    while(key_int >= factorial(64)):
        key_chunk = os.urandom(38)
        key_int = int.from_bytes(key_chunk, 'big')

    return key_chunk


################################################################################
# convert_key_to_character_list
#
# Takes in a key, like one generated from generate_key(), and transforms it
# into an array of character lists that can be used to generate the disguiseid.
################################################################################
def convert_key_to_character_lists(key: bytes) -> List[str]:
    if len(key) % 38 != 0:
        raise ValueError("Key must be a multiple of 38 bytes")


    index = 0
    memkey = memoryview(key)

    character_lists = []

    while(index+38 <= len(memkey)):
        character_lists.append(
            character_list_from_index(int.from_bytes(memkey[index:index+38], 'big'))
        )
        index += 38

    return character_lists


################################################################################
# character_list_from_index
#
# This function takes in an index of one of the 64! permutations of the 64
# characters, and returns a string with the characters in that particular
# permutation. The characters list is the base64 characterset except for the
# two symbols are `-` and `_` instead of `+` and `/`.
################################################################################
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
def character_list_from_index(index: int) -> str:
    permutation: List[int] = permutation_from_index(64, index)
    return "".join([characters[i] for i in permutation])


################################################################################
# permutation_from_index
#
# Returns an array of length `length` with one of the possible permutations of
# integers from `0` to `length-1`. The index value can be any value between and
# including 0 and factorial(length)-1. This operation is deterministic so the
# same combination of  length and index will always return the same
# permutation. This function does not calculate all the permutations, reducing
# the complexity to  O(LOG(length!)), mostly due to handling large integer
# values of `index`.
################################################################################
def permutation_from_index(length: int, index: int) -> List[int]:
    # Sanity check that the permutation index is a valid index.
    if index >= factorial(length) or index < 0:
        raise ValueError("Index out of bounds")

    # Transform the index into an array of possible options with the maximum
    # value of each element being the number of remaining options availalbe for
    # values at that index. The maximum values would be:
    #
    #     [length-1, length-2, length-3, length-4, ... , 3, 2, 1, 0]
    #
    # The last element will always be 0 because the final element only ever has
    # a single option remaining, leaving this 0 in the array makes the next
    # part of this function simpler.
    permutation: List[int] = []
    for i in range(length):
       permutation.append(index // factorial(length - i - 1))
       index = index % factorial(length - i - 1)

   
    # Convert the permutation array of decreasing maximum values into a non
    # repeating array containing all values between and including 0 and
    # length-1 by removing previously chosen values from a list of all possible
    # values before the next element choses a value.
    options = [ option for option in range(length)]
    value: List[int] = []
    for i in permutation:
        value.append(options.pop(i))
    return value

    # # A possibly more efficient method of accomplishing the same thing, but
    # # less intuitive to understand.
    # for upper_index in reversed(range(1, length)):
    #    for lower_index in reversed(range(upper_index)):
    #       if (permutation[lower_index] <= permutation[upper_index]):
    #          permutation[upper_index] += 1;
    # print(permutation)


################################################################################
# factorial
#
# A memoized factorial function.
################################################################################
_factorials: Dict[int, int] = {0: 1, 1: 1}
def factorial(i: int) -> int:
    global _factorials

    if i not in _factorials:
        _factorials[i] = factorial(i-1) * i

    return _factorials[i]




if __name__ == "__main__":
    main()


