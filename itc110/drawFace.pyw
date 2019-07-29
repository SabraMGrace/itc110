# drawFace
#   draw 3 faces, each one smaller than the last using a function.

from graphics import *

def main():
    win = GraphWin()
    win.setBackground("cyan")
    center = Point(150, 150)
    drawFace(center, 40, win)
    center = Point(75, 75)
    drawFace(center, 30, win)
    center = Point(25, 25)
    drawFace(center, 20, win)
    
# draw the face.
def drawFace(center, size, win):
    circ = Circle(center, size)
    circ.setFill("lavender")
    circ.setOutline("Aqua")
    circ.setWidth(5)

    circ.draw(win)

main()
