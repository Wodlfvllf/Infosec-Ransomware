import os
import body
encryption_ext=('.jpeg','.jpg','.pdf','.txt','.png')
def decryption(key):
    aes=body.AESCipher(key)
    file_path=[]
    for root, dirs, files in os.walk('/Users/shashank/Ransomware'):
        for file in files:
            file_path,file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encryption_ext:
                filep=open(os.path.join(root,file),"rb")
                out1=aes.decrypt(filep.read())
                open(os.path.join(root,file), "wb").write(out1)