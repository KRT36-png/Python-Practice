import json
import os
import pprint
def add():
    name=input("Enter Contact Name:")
    phone_number=input("Enter Phone Number:")
    email=input("Enter email id:")
    contact_dict[name]={"phone_number":phone_number,"email":email}
def view_all():
    pprint.pprint(contact_dict, indent=4)
def delete_entry():
    name=input("Enter Name of the contact:")
    if name in contact_dict:
         del contact_dict[name]
         print("deleted")
    else:
         print("Not found")
def edit():
    name=input("Enter Name of the contact:")
    if name in contact_dict:
         while True:
              print("Select what you want to edit:")
              print("1 Name")
              print("2 phone number")
              print("3 email")
              print("4 none of the above")
              choice_edit=input("Enter your choice(1,2,3,4):")
              if choice_edit == "1":  
                   new_name=input("Enter new Name:")
                   contact_dict[new_name]=contact_dict[name]
                   del contact_dict[name]
                   name=new_name
              elif choice_edit=="2":
                   new_phone_number=input("Enter new phone number")
                   contact_dict[name]["phone_number"]=new_phone_number
              elif choice_edit=="3":
                   new_email=input("Enter new email")
                   contact_dict[name]["email"]=new_email
              elif choice_edit == "4":
                   break
def search():
    user_search=input("Enter the Name of the Contact you want to search:")
    for key in contact_dict:
         if user_search.lower() in str(key).lower():
              print(key,": ",contact_dict[key])              
if os.path.exists("contact_manager_cli.json"):
    with open("contact_manager_cli.json","r") as file:
        contact_dict=json.load(file)
    while True:
        print("1 add")
        print("2 view entire contact dictionary")
        print("3 delete_entry")
        print("4 edit")
        print("5 search")
        print("6 exit")
        choice=int(input("Enter choice(1,2,3,4,5,6):"))
        if choice==1:
                add()
        elif choice==2:
                view_all()
        elif choice==3:
                delete_entry()
        elif choice==4:
                edit()
        elif choice==5:
                search()
        elif choice==6:
            with open("contact_manager_cli.json","w") as file_save:
                json.dump(contact_dict,file_save)
            break
else:
    with open("contact_manager_cli.json","w") as file_created:
        empty={}
        json.dump(empty,file_created)

    