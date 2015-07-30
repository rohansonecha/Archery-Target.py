# Author: Rohan Sonecha
# N-Factorial.py
# finds factorial of a number using recursion

print("Give me your number and I will find its factorial")
n = input("What is your number: ")
n = eval(n)

def factorial(n):
    if (n == 1):
        return 1
    else:
        return n*factorial(n-1)

def main():
    answer = factorial(n)
    print("answer: ",answer)

main()

