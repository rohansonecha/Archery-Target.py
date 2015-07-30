# Author: Rohan Sonecha
# prime.py
# Determines if a number is prime

def main():
    print("This program determines whether or not a given number is prime")
    n = input("What is your number: ")
    n = eval(n)

    count = 2
    isPrime = True
    while (count < n):
        if (n % count == 0):
            isPrime = False
            break
        count = count + n
    if (isPrime == False):
        print(n," is not prime")
    else:
        print(n," is prime")
main()
