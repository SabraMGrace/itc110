#draw an eye

from graphics import *

win = GraphWin("Eyes", 500, 500)

leftEye = Oval(Point(80, 50), Point(40, 30))
leftEye.setFill("cyan")
leftEye.setWidth(3)

#make a copy of the left eye
rightEye = leftEye.clone()
rightEye.move(60, 0)
rightEye.draw(win)

#draw a pupil for left eye
center = Point(40,25)
circ = Circle(center, 20)
circ.setFill("black")
leftEye.draw(win)
