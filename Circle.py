# Author: Rohan Sonecha
# circle.py
# Example of a while loop to calculate a and c of a circle

def main():

    # repeats
    while (True):
        print("This program calculates the circumference and area of a circle")

        # ask what is user's radius and convert to int from str
        r = input("What is the radius of your circle: ")
        r = eval(r)

        # define circumference and area
        c = r * 2 * 3.14
        a = 3.14 * r ** 2
        
        # calculate/display circumference
        print("circumference:")
        print(c)

        # make a space between circumference and area
        print()
        
        # calculate/display area
        print("area:")
        print(a)


main()
