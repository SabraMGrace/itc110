# Sabra Grace
# ITC110 - Assignment 4
# Draw a truck


from graphics import *

def main():
    win = GraphWin()
    win.setBackground("green")
    
    # draw rectangle for truck body
    shape = Rectangle(Point(20,50), Point(160,100))
    shape.setOutline("blue")
    shape.setFill("blue")
    shape.draw(win)

    #draw second rectangle for cab of truck
    ###

    # draw a circle for the left wheel
    leftWheel = Circle(Point(40, 100), 15)
    leftWheel.setFill("black")
    leftWheel.setOutline("black")

    leftWheel.draw(win)
    
    # make a copy of the left wheel
    # to create the right wheel
    rightWheel = leftWheel.clone() 
    rightWheel.move(100, 0)
    rightWheel.draw(win)

main()
