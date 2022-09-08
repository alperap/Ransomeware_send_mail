import os
from cryptography.fernet import Fernet

list = []

def take_files():
    global list
    for f in os.listdir():
        if f == "ransome_ware_email_decrypt.py" or f == "ransome_ware_email.py":
            continue
        if f == "key.key":
            continue
        if os.path.isfile(f):
            list.append(f)
    print(f"This is file inventory: {list}")

def decrypt_file(key):
    global list
    for file in list:
        with open(file,"rb") as f:
            read = f.read()
        decrypt = Fernet(key).decrypt(read)
        with open(file,"wb") as f:
            f.write(decrypt)

def i_want_key():
    key = input("\nPlease enter your decrypt key: ")
    return key

while True:
    try:
        take_files()
        key = i_want_key()
        decrypt_file(key)
        print("\nOkay, it is work!")
        break
    except:
        print("\nOps! Wrong key or something")
        break


