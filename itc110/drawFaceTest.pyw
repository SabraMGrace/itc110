# drawFace
#   draw 3 faces, each one smaller than the last using a function.

import math
from graphics import *

def main():
    win = GraphWin()
    win.setBackground("cyan")
    drawFace(win, 40, 150, 150)
    drawFace(win, 30, 75, 75)
    drawFace(win, 20, 25, 25)
    
# draw the face.
def drawFace(win, diameter, xPosition, yPosition):
    center = Point(xPosition, yPosition)
    circ = Circle(center, diameter)
    circ.setFill("lavender")
    circ.setOutline("Aqua")
    circ.setWidth(5)

    circ.draw(win)

main()
