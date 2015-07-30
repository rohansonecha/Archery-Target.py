# Author: Rohan Sonecha
# Login.py
# Checks username and password in order to let someone into account
def Login(count):
    
    print(count)

    u = input("What is your username: ")
    p = input("What is your password: ")
    
    if (count == 3):
        print("You have been locked out.")
    elif (u == "FCPSrules" and p == "101010"):
        print("You are correct!!")
        count = 10
    else:
        Login(count + 1)

Login(0)
