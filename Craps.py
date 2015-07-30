# Author: Rohan Sonecha
# Craps.py
# creates the casino game: Craps
import random
from Graphics import*

def graphics(die1,die2):
    win = GraphWin("Dice",210,110)
    win.setBackground('Orange')

    firstDie = Rectangle(Point(10,10), Point(100,100))
    firstDie.setFill('White')
    firstDie.draw(win)

    secondDie = Rectangle(Point(110,10), Point(200,100))
    secondDie.setFill('White')
    secondDie.draw(win)

    # Die 1 dots
    if (die1 == 1):
        dot1 = Circle(Point(55,55),10)
        dot1.setFill("Black")
        dot1.draw(win)
    elif (die1 == 2):
        dot1 = Circle(Point(55,45),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(55,65),10)
        dot2.setFill("Black")
        dot2.draw(win)
    elif (die1 == 3):
        dot1 = Circle(Point(25,25),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(55,55),10)
        dot2.setFill("Black")
        dot2.draw(win)

        dot3 = Circle(Point(85,85),10)
        dot3.setFill("Black")
        dot3.draw(win)
    elif (die1 == 4):
        dot1 = Circle(Point(15,15),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(15,95),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(95,95),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(95,15),10)
        dot4.setFill("Black")
        dot4.draw(win)        
    elif (die1 == 5):
        dot1 = Circle(Point(35,35),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(35,85),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(75,75),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(75,35),10)
        dot4.setFill("Black")
        dot4.draw(win) 

        dot5 = Circle(Point(55,55),10)
        dot5.setFill("Black")
        dot5.draw(win)
    elif (die1 == 6):
        dot1 = Circle(Point(25,25),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(25,95),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(95,85),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(85,25),10)
        dot4.setFill("Black")
        dot4.draw(win)

        dot5 = Circle(Point(25,55),10)
        dot5.setFill("Black")
        dot5.draw(win)        

        dot6 = Circle(Point(85,55),10)
        dot6.setFill("Black")
        dot6.draw(win)
    else:
        pass
    # Die 2 dots
    if (die2 == 1):
        dot1 = Circle(Point(155,155),10)
        dot1.setFill("Black")
        dot1.draw(win)
    elif (die2 == 2):
        dot1 = Circle(Point(155,145),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(155,165),10)
        dot2.setFill("Black")
        dot2.draw(win)
    elif (die2 == 3):
        dot1 = Circle(Point(125,125),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(155,155),10)
        dot2.setFill("Black")
        dot2.draw(win)

        dot3 = Circle(Point(185,185),10)
        dot3.setFill("Black")
        dot3.draw(win)
    elif (die2 == 4):
        dot1 = Circle(Point(115,115),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(115,195),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(195,195),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(195,115),10)
        dot4.setFill("Black")
        dot4.draw(win)        
    elif (die2 == 5):
        dot1 = Circle(Point(135,135),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(135,185),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(175,175),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(175,135),10)
        dot4.setFill("Black")
        dot4.draw(win) 

        dot5 = Circle(Point(155,155),10)
        dot5.setFill("Black")
        dot5.draw(win)
    elif (die2 == 6):
        dot1 = Circle(Point(135,135),10)
        dot1.setFill("Black")
        dot1.draw(win)

        dot2 = Circle(Point(125,195),10)
        dot2.setFill("Black")
        dot2.draw(win)        

        dot3 = Circle(Point(195,185),10)
        dot3.setFill("Black")
        dot3.draw(win)

        dot4 = Circle(Point(185,125),10)
        dot4.setFill("Black")
        dot4.draw(win)

        dot5 = Circle(Point(125,155),10)
        dot5.setFill("Black")
        dot5.draw(win)        

        dot6 = Circle(Point(185,155),10)
        dot6.setFill("Black")
        dot6.draw(win)

def dice():
    # actual game
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    # graphics
    graphics(die1,die2)

    # game cont.
    dieval = die1 + die2
    if (dieval == 2 or dieval == 3 or dieval == 12):
        print ("You got a ",dieval)
        return False
    elif (dieval == 7 or dieval == 11):
        print ("You got a ",dieval)
        return True
    else:
        print ("You are now in play for point mode")
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dieval2 = die1 + die2
        while (dieval2 != 7):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            dieval2 = die1 + die2
            if (dieval2 == dieval):
                return True
        return False

def main():
    # runs the program
    result = dice()
    print (result)
    if (result != True):
        print ("You lose")
    else:
        print ("You win")
main()
