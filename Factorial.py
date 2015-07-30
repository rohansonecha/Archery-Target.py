# Author: Rohan Sonecha
# Factorial.py
# finds factorial of a number

def main():
    print("Give me your number and I will find its factorial")
    n = input("What is your number: ")
    n = eval(n)
    b = n
    while (n > 1):
        b = b * (n-1)
        n -= 1
    print ("The Factorial of ",n," is ",b)
main()
