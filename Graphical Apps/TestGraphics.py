from graphics import *

def ButtonProject():
    WINDOW_WIDTH, WINDOW_HEIGHT = 200, 150

    win = GraphWin("Simple Breakout", WINDOW_WIDTH, WINDOW_HEIGHT)

    def buttons():
        left = Rectangle(Point(25, 55), Point(55, 85))  # points are ordered ll, ur
        right = Rectangle(Point(145, 55), Point(175, 85))
        quit = Rectangle(Point(85, 116), Point(115, 146))

        left.setFill("red")
        right.setFill("green")
        text = Text(Point(100, 133), "Exit")
        text.draw(win)

        left.draw(win)
        right.draw(win)
        quit.draw(win)

        return left, right, quit

    def inside(point, rectangle):
        """ Is point inside rectangle? """

        ll = rectangle.getP1()  # assume p1 is ll (lower left)
        ur = rectangle.getP2()  # assume p2 is ur (upper right)

        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

    left, right, quit = buttons()

    centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    text = Text(centerPoint, "")
    text.draw(win)

    while True:
        clickPoint = win.getMouse()

        if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
            text.setText("")
        elif inside(clickPoint, left):
            text.setText("left")
        elif inside(clickPoint, right):
            text.setText("right")
        elif inside(clickPoint, quit):
            break
        else:
            text.setText("")

    win.close()

def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

ButtonProject()