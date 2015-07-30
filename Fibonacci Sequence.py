# Author: Rohan Sonecha
# Fibonacci Sequence.py
# computes the fibonacci sequence
def fibRecur(num1,num2,count):
    num3 = num1 + num2
    if(count<= 2):
        return num2
    return fibRecur(num2,num3,count-1)
def fib1(n):
    n = eval(n)
    a = 1
    b = 1
    index = 0
    while(index<n-1):
        c = a + b
        a = b
        b = c
        index = index + 1
    return c
def main():
    '''
    n = input("Which fibonacci number would you like: ")
    n = eval(n)

    answer = fibRecur(1,1,n)
    print (answer)
    '''
    print (fib1(input("Which fibonacci number would you like: ")))
main()
    
