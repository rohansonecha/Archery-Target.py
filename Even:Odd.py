# Author: Rohan Sonecha
# Even/Odd.py
# prints whether user-chosen integer is even or odd

def main():
    interest = ""
    while (interest != "done"):
        i = input("What is your integer: ")
        i = eval(i)
        if (i % 2 == 0):
            print ("Your number is even\n")
        else:
            print ("Your number is odd\n")
        interest = input("If you would like to stop, type done otherwise type continue: ")
main()
