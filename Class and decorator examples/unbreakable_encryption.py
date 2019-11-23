""" unbreakable_encryption.py
    One-time pad is a way to encrypt data by combining with
    meaningless random dummy data.
    str are coverted to bits first using .encode() and .decore().
    Then bit-string are saved in int. with .from_bytes() and .to_bytes()
    Alot of the operations are done in bit-strings using XOR
    bit-string XOR since very efficient. Taking advantage of XOR property.
                A^B = C then C^B = A and C^A = B.
    Inspired by David Kopec Chapter 1. 
    also good reading at https://www.devdungeon.com/content/working-binary-data-python """

from secrets import token_bytes   # pseudo-random data generating function
from typing import Tuple

def random_key(length: int) -> int:
    """ Generate length random bytes using token-bytes function. """
    randon_bytes: bytes = token_bytes(length)

    # Convert those bytes into a bit string store in (type) int and return it
    # (type) int can be used for generic bit string and can be of arbitrary length
    return int.from_bytes(randon_bytes, "big")

def encrypt(original: str) -> Tuple[int, int]:
    """ Encrypts the string by taking advantage of bit-string XOR property.
        A^B = C then C^B = A and C^A = B.
        Returns the dummy data and encrypted data."""

    # .encode() method converts str to sequence of UTF-8 bytes.
    original_bytes: bytes = original.encode()

    # Get the dummy data of the same length as the string once converted in bytes
    dummy: int = random_key(len(original_bytes))

    # Store the bytes in an int
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy   # ^ is the XOR
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    """ Decrypt the code where key1 is the dummy data and key2 is the encrypted str. """

    # Taking advantage of XOR property. A^B = C then C^B = A and C^A = B.
    decrypted: int = key1 ^ key2

    # Convert the bit-string integer back to bytes
    # Need to add 7 before the int division (//) by 8 to ensure round-up
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) //8, "big")

    # .decode() method converts a sequence of UTF-8 bytes into str
    return temp.decode()

if __name__ == "__main__":
    random_key, code = encrypt("One time pad!")
    # print(f"\n=>{type(random_key)} {random_key}, {code}")
    result: str = decrypt(random_key, code)
    print(f"\n{result}")