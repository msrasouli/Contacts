name = input("Enter name :")
lastname = input("Enter Lastname :")
phonenumber = input("Enter phone number :")
note = input("Do you want write any notes ?")

if note == "yes" :
    note1=input("Give me note :")
    print(name , lastname , phonenumber , note1 )
else : 
    print(name , lastname , phonenumber )