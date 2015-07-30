from graphics import *

win = GraphWin("Dice",610,110)
win.setBackground('Orange')

die1 = Rectangle(Point(10,10), Point(100,100))
die1.setFill('White')
die1.draw(win)

die2 = Rectangle(Point(110,10), Point(200,100))
die2.setFill('White')
die2.draw(win)

die3 = Rectangle(Point(210,10), Point(300,100))
die3.setFill('White')
die3.draw(win)

die4 = Rectangle(Point(310,10), Point(400,100))
die4.setFill('White')
die4.draw(win)

die5 = Rectangle(Point(410,10), Point(500,100))
die5.setFill('White')
die5.draw(win)

die6 = Rectangle(Point(510,10), Point(600,100))
die6.setFill('White')
die6.draw(win)

# Dot Function
def dot(a,b,c):
    dot1 = Circle(Point(a,b),c)
    dot1.setFill('Black')
    dot1.draw(win)

dot(55,55,10)
dot(132.5,55.5,10)
dot(177.5,55.5,10)
dot(230,30,10)
dot(255,55.5,10)
dot(280,78,10)
dot(335,30,10)
dot(375,30,10)
dot(335,80,10)
dot(375,80,10)
dot(435,30,10)
dot(475,30,10)
dot(435,80,10)
dot(475,80,10)
dot(455,55,10)
