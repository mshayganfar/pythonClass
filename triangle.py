from graphics import *

def createWindow():
    win = GraphWin("Triangle Information", 400, 400)
    win.setCoords(-25,-25,25,25)
    return win

def showMessage(canvas):
    txtMessage = Text(Point(0,0), "Click three points within the window.")
    txtMessage.draw(canvas)
    return txtMessage

def getTrianglePoints(canvas, txtMessage):
    p1 = canvas.getMouse()
    p1.draw(canvas)
    txtMessage.undraw()
    p2 = canvas.getMouse()
    p2.draw(canvas)
    p3 = canvas.getMouse()
    p3.draw(canvas)
    return [p1, p2, p3]

def drawTriangle(canvas, points):
    line1 = Line(points[0], points[1])
    line2 = Line(points[1], points[2])
    line3 = Line(points[2], points[0])

    line1.setWidth(2)
    line2.setWidth(2)
    line3.setWidth(2)

    line1.draw(canvas)
    line2.draw(canvas)
    line3.draw(canvas)
    return [line1, line2, line3]

def main():
    win = createWindow()
    txtMessage = showMessage(win)
    tPoints = getTrianglePoints(win, txtMessage)
    drawTriangle(win, tPoints)
    return
