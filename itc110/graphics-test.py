#basic tests of the graphics library

from graphics import *

#create a Point object
p = Point(50, 60)

print(p.getX())
print(p.getY())

#create a window object
win = GraphWin()

#draw a circle
center = Point(100, 100)
circ = Circle(center, 60)
circ.setFill("pink")
circ.setOutline("aqua")
circ.setWidth(5)

circ.draw(win)

p.draw(win)

#create a second point

p2 = Point(100, 150)

p2.draw(win)

#create a line
line = Line(p, p2)
line.draw(win)
line.setFill("cyan")

#label the circle
label = Text(center, "My Wonderful Circle")
label.setTextColor("cyan")
label.draw(win)

