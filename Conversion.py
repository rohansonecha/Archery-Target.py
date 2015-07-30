# Author: Rohan Sonecha
# conversion.py
# converts different units

def horsetosears():
    amount = input("How many horses do you want to convert to sears: ")
    amount = eval(amount)
    amount2 = amount * 8/1703
    print (amount2, " sears towers")
def horsetoempire():
    amount = input("How many horses do you want to convert to empires: ")
    amount = eval(amount)
    amount2 = amount * 8/1473
    print (amount2, " empire state buildings")
def empiretohorse():
    amount = input("How many empires do you want to convert to horses: ")
    amount = eval(amount)
    amount2 = amount * 1473/8
    print (amount2, " horses")
def empiretosears():
    amount = input("How many empires do you want to convert to sears: ")
    amount = eval(amount)
    amount2 = amount * 1473/1703
    print (amount2, " sears")
def searstohorse():
    amount = input("How many sears do you want to convert to horses: ")
    amount = eval(amount)
    amount2 = amount * 1703/8
    print (amount2, " horses")
def searstoempire():
    amount = input("How many sears do you want to convert to empires: ")
    amount = eval(amount)
    amount2 = amount * 1703/1473
    print (amount2, " empires")

def convert():
    print("The three units this program converts are: Horse, Empire State Building and Sears Tower")
    orig = input("What is your original unit: ")
    new = input("What unit would you like to convert your original unit to: ")
    if (orig == "horses" and new == "sears towers"):
        horsetosears()
    elif (orig == "horses" and new == "empire state buildings"):
        horsetoempire()
    elif (orig == "empire state buildings" and new == "horses"):
        empiretohorse()
    elif (orig == "empire state buildings" and new == "sears towers"):
        empiretosears()
    elif (orig == "sears towers" and new == "horses"):
        searstohorse()
    elif (orig == "sears towers" and new == "empire state buildings"):
        searstoempire()
    else:
        convert()
convert()
