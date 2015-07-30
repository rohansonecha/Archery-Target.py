from graphics import*

win = GraphWin("Shapes",1200,900)
center = Point(100,100)

circ = Circle(center,300)
circ.setFill('red')
circ.draw(win)

label = Text(center,"Red Circle")
label.draw(win)

rect = Rectangle(Point(0,300), Point(700,700))
rect.draw(win)
rect.setFill('black')

line = Line(Point(200,1), Point(1800,1650))
line.draw(win)


oval = Oval(Point(2000,1500),Point(1800,1990))
oval.draw(win)
