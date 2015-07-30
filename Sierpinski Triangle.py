# Author: Rohan Sonecha
# Sierpinski Triangle.py
# draws the Sierpinski Triangle
from Graphics import*

def triangle(p1,p2,p3):   
    tri = Polygon(p1,p2,p3)
    tri.draw(win)

def serp(level,sl,p1,p2,p3):
    if(level==0):
        return
    triangle(sl,p1,p2,p3)
    serp(level-1,sl/2,)
    serp(level-1,sl/2,)
    serp(level-1,sl/2,)
    
def main():
    win = GraphWin("Sierpinski Triangle",500,500)
    x1 = 5
    y1 = 5
    
    x2 = 245
    y2 = 495

    x3 = 495
    y3 = 5
    mainTri = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    mainTri.draw(win)

    tri = Polygon(p1,p2,p3)
    tri.draw(win)
    
    # leftmost side
    mid1 = Point((x1 + x2) / 2, (y1 + y2) / 2)
    mid1x = mid1.getX()
    mid1y = mid1.getY()
    # rightmost side
    mid2 = Point((x2 + x3) / 2, (y2 + y3) / 2)
    mid2x = mid2.getX()
    mid2y = mid2.getY()
    # top side
    mid3 = Point((x3 + x1) / 2, (y3 + y1) / 2)
    mid3x = mid3.getX()
    mid3y = mid3.getY()
main()
