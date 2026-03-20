import hashlib
import json
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
def add():
    site=input("Enter site:")
    username=input("Enter username:")
    password=input("Enter password:")
    vault_dict[site]={"username":username,"password":password}
def view():
    site=input("Enter site:")
    if site in vault_dict:
      print("Username:",vault_dict[site]["username"])
      print("Password:",vault_dict[site]["password"])
    else:
      print("Not found")
def delete():
    site = input("Enter site:")
    if site in vault_dict:
        del vault_dict[site]
        print("deleted")
    else:
        print("Not found")
    


file_path='vault.json'
if os.path.isfile(file_path) and os.path.isfile("pass_w.txt"):
    with open("pass_w.txt","r") as f:
       Mast_pass=input("Enter your Master password:")
       Hashed_pass=(hashlib.sha256((Mast_pass).encode('utf-8'))).hexdigest()
       del Mast_pass
       if f.read().strip()!=Hashed_pass:
           print("Wrong password!")
           exit()
       with open("data.encrypted","rb") as l:
            h=l.read()
            with open('filekey.key','rb') as o:
                 key=o.read()
                 cipher= Fernet(key)
                 vault_bytes=cipher.decrypt(h) 
                 vault_string=vault_bytes.decode('utf-8')
                 vault_dict=json.loads(vault_string)
       while True:
           print("1 Add")
           print("2 View")
           print("3 delete")
           print("4 Exit")
           choice =input("Enter choice(1,2,3,4):")
           if choice=="1":
               add()
           elif choice =="2":
               view()
           elif choice =="3":
               delete()
           elif choice=="4":
               vault_string=json.dumps(vault_dict)
               vault_bytes=vault_string.encode()
               encrypted=cipher.encrypt(vault_bytes)
               with open("data.encrypted","wb") as file:
                   file.write(encrypted)
               break
       

            
else:
    Check=input("File does not exist,Do you wish to create it?(T/F):")
    if Check=="T":
         with open("pass_w.txt","w") as k:
            Mast_Password=input("Enter your master password:")
            Hashed_pass=(hashlib.sha256((Mast_Password).encode('utf-8'))).hexdigest()
            k.write(Hashed_pass)
            del Mast_Password
         empty_vault={}
         with open("vault.json","w") as e:
            json.dump(empty_vault,e)
         with open("vault.json","r") as e:
            key = Fernet.generate_key()
            with open('filekey.key', 'wb') as key_file:
                key_file.write(key)
            key = open('filekey.key', 'rb').read()
            f = Fernet(key)
            encrypted = f.encrypt(e.read())
         with open('data.encrypted', 'wb') as file:
            file.write(encrypted)
            
      


            
    



         





            
    