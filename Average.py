# Author: Rohan Sonecha
# Average Finder.py
# Finds the average

def main():
    print("This program will find the average of your numbers")
    print("Type done if you would like to stop entering new numbers \n")
    nums = []
    while (True):
        x = input("Enter a number OR type done: ")
        if (x == "done"):
            break
        x = eval(x)
        nums.append(x)
    average = sum(nums)/len(nums)
    print ("Your numbers are: ", nums)
    print ("\nThe average of your numbers is: ",average)
main()

