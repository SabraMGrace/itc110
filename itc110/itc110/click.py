#click.py

from graphics import *

def main():
    win = GraphWin("Click me!")
    for i in range(10):
        p = win.getMouse()
        print("you clicked at: ", p.getX(), p.getY())
    win.close()

main()
