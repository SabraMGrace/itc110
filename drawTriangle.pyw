# draw a triangle

from math     import *

from graphics import *


def square(x):
    answer = x * x
    return answer


def distance(p1, p2):
    xDist = p2.getX() - p1.getX()
    yDist = p2.getY() - p1.getY()
    dist = sqrt (square(xDist) + square(yDist))
     
    
##    dist = sqrt( (square ( p2.getX() - p1.getX() ) ) +
##                 (square ( p2.getY() - p1.getY() ) ) )
    
    print("DEBUG :   distance is : ", dist)
    return dist

def drawTriangle():
    win = GraphWin("Draw Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # get and draw the vertices of the triangle
    p1 = win.getMouse()
