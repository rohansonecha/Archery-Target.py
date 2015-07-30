# Author: Rohan Sonecha
# Syracuse Sequence.py
# if x is even, x becomes x/2 and if x is odd, x becomes 3x + 1 until the output is 1
def main():
    print("This program will implment the Syracuse Sequence.")
    x = input("What number should I implement the Syracuse Sequence to: ")
    x = eval(x)
    while (x != 1):
        if (x % 2 == 0):
            x /= 2
            print (x)
        else:
            x = 3 * x + 1
            print (x)
main()
