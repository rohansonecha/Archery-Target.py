# Author: Rohan Sonecha
# Binary Converter.py
# Converts base 10 numbers to binary

def main():
    print("This program converts your base 10 numbers to binary numbers \n")
    x = input("Base-10 Number: ")
    x = eval(x)
    while(x != 0):
        m = x % 2
        x = x // 2
        print("m: ",m)
main()
