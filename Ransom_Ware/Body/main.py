import os
import body
import encrypt
import decrypt
import random

Key='Mykey'
"""encryption_level=128//8
char_pool=''
for i in range(0x00, 0xFF):
    char_pool+=(chr(i))
for i in range(encryption_level):
    Key+=random.choice(char_pool)
"""
def generateKey(size):
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890=-+_*\|?><,.{]}[()")
    indexs = []
    for _ in range(size):
        indexs.append(random.randint(0, len(chars) - 1))
    return "".join(list(map(lambda x : chars[x], indexs)))

Key=generateKey(100)
print(Key)
def main():
    encrypt.encryption(Key)
    key=input("Enter the Key to decrypt: ")
    if Key==key:
        decrypt.decryption(Key)
    
main()