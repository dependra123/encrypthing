import tkinter as tk
from tkinter import filedialog
import os
import encrypt


# Create a window
root = tk.Tk()
root.title("Encryptor")
root.geometry("300x200")



def filemode():
    
    fpath = filedialog.askopenfile()
    print ("File mode")
    return fpath
def foldermode():
  
    fpath = filedialog.askdirectory()
    print ("folder mode")
    return fpath


fpath = filemode()

"""if os.path.isdir(fpath.name):
    encrypt.folders.put(fpath)
    
    #for each file in the folder, encrypt it
    for file in os.listdir(encrypt.folders.get()):
        print("opening file: " + file)
        #check if folder is empty
        if not len(os.listdir(fpath.name)) == 0:
            if os.path.isdir(fpath.name + "\\" + file):
                encrypt.folders.put(fpath.name + "\\" + file)
            else:
                with open("file_names.txt", "a") as file_names:
                    file_names.write(fpath.name + "\\" + file + ".ENCRYPTED" + "\n")
                    file_names.close()
                encrypt(fpath.name + "\\" + file)
                print (file + "encrypted")"""

#else:
encrypt.encrypt(fpath)
with open("file_names.txt", "a") as file_names:
    file_names.write(fpath.name + "\n")
    file_names.close()
print (fpath.name + "encrypted") 

print(fpath.name + "removed")

os.rename(fpath.name, fpath.name + ".ENCRYPTED")
