password=input("enter a password :")
if len(password)>=6 and len(password)<=16:
    if "2" in password or "8" in password:
        if "A" in password or "Z"  in password:
            print("it is strong passwod")
        else:
            print("try again")
    else:
        print("try again")
else:
    print("try again")









