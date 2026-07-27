name = input("Enter name :")
lastname = input("Enter Lastname :")
phonenumber = input("Enter phone number :")
note = input("Do you want add any notes ?")

if note == "yes" :
    note1=input("Give me note :")
    print(f"Name: {name}")
    print(f"lastname: {lastname}")
    print(f"phone number: {phonenumber}")
    print(f"note: {note1}")
else : 
    print(f"Name :{name}")
    print(f"lastname: {lastname}")
    print(f"phone number: {phonenumber}")
