#draw circles, then draw squares instead
    #textbook page 125-126

from graphics import *

def main():
    win = GraphWin()
    #draw rectangle
    shape = Rectangle(Point(10,20), Point(30,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        #draw additional rectangles
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    #add text message
    Text(Point(100,100), "Click again to quit.").draw(win)
    win.getMouse()
    win.close()
        
main()




