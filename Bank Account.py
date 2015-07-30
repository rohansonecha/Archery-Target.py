# Author: Rohan Sonecha
# Bank Account.py
# simple features of a bank account
user = "rohan"
pas = "sonecha"
FCPSOwnerAdmin = "FCPSadmin"
FCPSOwnerAdminPass = "2002rohan"

def login(count):
    while(count <= 3):
        u = input("What is your username: ")
        p = input("What is your password: ")
        if (count == 3):
            print("You have been locked out.")
            return (False)
        elif ((u == user or u == FCPSOwnerAdmin) and (p == pas or p == FCPSOwnerAdminPass)):
            print("Welcome",u,"!\n")
            count = 10
        else:
            print("Incorrect. Try again.")
            count += 1



def showBalance(balance):
    print ("$",balance, "\n")

def deposit(balance):
    depos = input("How much money would you like to deposit: ")
    depos = eval(depos)
    while (depos <= 0):
        print ("Invalid deposit")
        deposit(balance)
    balance += depos
    print("You deposited $",depos,"And your new balance is $",balance, "\n")

def withdraw(balance):
    withdraw = input("How much money would you like to withdraw: ")
    withdraw = eval(withdraw)
    while (withdraw <= 0 or withdraw > balance):
        print ("Invalid withdrawal")
        deposit(balance)
    balance -= withdraw
    print("You withdrew $",withdraw,"And your new balance is $",balance, "/n")

def end():
    print("Thanks for banking with FCPS!")



# Runs the functions/puts them together
def main():
    choice = ""
    answer = login(0)
    if(answer):
        while (choice != "4"):
            print("Welcome to the first national FCPS bank!")
            print("What would you like to do?\n")
            print("1. View your balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Quit")
            choice = input("Enter your selection [1, 2, 3, or 4]: ")
            balance = 1500
            if (choice == "1"):
                showBalance(balance)
            elif (choice == "2"):
                deposit(balance)
            elif (choice == "3"):
                withdraw(balance)
            elif (choice == "4"):
                end()
        
main()
