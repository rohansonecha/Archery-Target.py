# Author: Rohan Sonecha
# Number Sorter.py
# sorts numbers from highest to lowest

def main():
    print("I will sort your three numbers from greatest to smallest")
    n1 = input("Give me your first number: ")
    n1 = eval(n1)

    n2 = input("Give me your second number: ")
    n2 = eval(n2)

    n3 = input("Give me your third number: ")
    n3 = eval(n3)

    if (n1 >= n2):
        if (n1 >= n3):
            print("The greatest number is",n1)
            # maximum = n1
        else:
            # print("The greatest number is",n3)
            maximum = n3
    else:
        if (n2 >= n3):
            # print("The greatest number is",n2)
            maximum = n2
        else:
            # print("The greatest number is",n23
            maximum = n3

    print(maximum, " is the biggest")
main()
