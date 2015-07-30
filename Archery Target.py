from graphics import *

window = GraphWin("Archery Target",500,500)
window.setBackground("Grey")

def ring(radius,color):
    center = Point(250,250)
    ring = Circle(center,radius)
    ring.setFill(color)
    ring.draw(window)

ring(250,"white")
ring(200,"black")
ring(150,"blue")
ring(100,"red")
ring(50,"yellow")

line = Line(Point(50,700),Point(250,250))
line.draw(window)






