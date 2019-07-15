#basic tests of the graphics library

from graphics import *

win = GraphWin()
rect = Rectangle(Point(20,30), Point(180,165))
#set color
rect.setFill("cyan")
rect.draw(win)

#draw an oval
oval = Oval(Point(20, 150), Point(180, 199))
oval.setFill("violet")
oval.draw(win)
