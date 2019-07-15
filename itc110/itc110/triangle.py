#triangle.pyw
from graphics import *

def main():
    win = GraphWin("Draw a triangle.")
    #setCoords(xll, yll, xur, yur)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 0.5), "Click on three points.")
    message.draw(win)

#get the mouse clicks from the user and raw the triangle vertices.
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)
    
    p3 = win.getMouse()
    p3.draw(win)

#draw a triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
