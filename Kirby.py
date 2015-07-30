# Author: Rohan Sonecha
# Kirby.py
# draws Kirby!!!

from graphics import *

win = GraphWin("Kirby",1000,1000)
win.setBackground("Yellow")

leftarm = Oval(Point(50,450),Point(150,700))
leftarm.draw(win)
leftarm.setFill("Pink")

rightarm = Oval(Point(850,250),Point(950,500))
rightarm.draw(win)
rightarm.setFill("Pink")

leftfoot = Oval(Point(50,900),Point(400,750))
leftfoot.draw(win)
leftfoot.setFill("Red")

rightfoot = Oval(Point(600,900),Point(950,750))
rightfoot.draw(win)
rightfoot.setFill("Red")

body = Circle(Point(500,500),375)
body.draw(win)
body.setFill("Pink")

lefteye = Oval(Point(350,250),Point(460,450))
lefteye.draw(win)
lefteye.setFill("Black")

lefteyewhite = Oval(Point(370,265),Point(440,400))
lefteyewhite.draw(win)
lefteyewhite.setFill("White")

righteye = Oval(Point(540,250),Point(650,450))
righteye.draw(win)
righteye.setFill("Black")

righteyewhite = Oval(Point(560,265),Point(630,400))
righteyewhite.draw(win)
righteyewhite.setFill("White")


mouth = Oval(Point(400,600),Point(600,700))
mouth.draw(win)
mouth.setFill("Red")
