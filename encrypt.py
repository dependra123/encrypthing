import tkinter as tk
from cryptography.fernet import Fernet
from tkinter import filedialog
import os
import threading
import ctypes
import sys
import queue
from pathlib import Path



folder_mode = False
fpath = ""



def convert_to_binary(data):
    return (data).encode("utf-8")

#make a fu
def encrypt(file_path):
    


    key = Fernet.generate_key()

    #save the key to a file
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        key_file.close()

    #make a key with fernet and save it in a file
    fernet = Fernet(key) 


    file_fpath = file_path.name
    print(file_fpath)
    #use Path.read_bytes to read from file_fpath
    data = Path(file_fpath).read_bytes()
    print ("read")
    print ("encrypting")
    #encrypt the file with the key
    #encrypted_file = fernet.encrypt(data)
    print ("encrypted")
    Path(file_fpath).write_bytes(data)
    print ("encrypted file saved")
    
    

print(fpath)

#wait for all threads to finish
"""for thread in threading.enumerate():
    if thread is not threading.current_thread():
        thread.join()"""
#close the windowdelete the Fpath.name



