# coding=utf-8
__author__ = "mlaptev"

if __name__ == "__main__":
    initial_alphabet = input()
    encrypted_alphabet = input()
    to_encrypt = input()
    to_decrypt = input()

    direct_code = dict()
    return_code = dict()

    for i in range(len(initial_alphabet)):
        direct_code[initial_alphabet[i]] = encrypted_alphabet[i]
        return_code[encrypted_alphabet[i]] = initial_alphabet[i]

    for to_encrypt_symbol in to_encrypt:
        print(direct_code[to_encrypt_symbol], end="")

    print()

    for to_decrypt_symbol in to_decrypt:
        print(return_code[to_decrypt_symbol], end="")
