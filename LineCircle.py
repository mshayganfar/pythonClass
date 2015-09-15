from graphics import *
from math import sqrt

def getInputValues():
    circleX = eval(input("Enter x coordinate of circle: "))
    circleRadius = eval(input("Enter radius of circle: "))
    return circleX, circleRadius
    
def createWindow():
    win = GraphWin("Line & Circle Intersection", 400, 400)
    win.setCoords(-25,-25,25,25)
    return win

def drawCircle(canvas, circleInfo):
    circle = Circle(Point(circleInfo[0],0), circleInfo[1])
    circle.setFill('yellow')
    circle.setOutline('blue')
    circle.setWidth(3)
    circle.draw(canvas)
    return

def drawLine(canvas, circleInfo):
    p1 = Point((circleInfo[0]-(circleInfo[1]/sqrt(2))), (circleInfo[1]/sqrt(2)))
    p2 = Point((circleInfo[0]+(circleInfo[1]/sqrt(2))), (-circleInfo[1]/sqrt(2)))
    line = Line(p1, p2)
    line.setWidth(2)
    line.draw(canvas)
    intersection1 = Circle(p1,0.5)
    intersection1.setFill('red')
    intersection2 = Circle(p2,0.5)
    intersection2.setFill('red')
    intersection1.draw(canvas)
    intersection2.draw(canvas)
    return p1,p2

def displayText(canvas, p1, p2):
    txtP1x = "x=" , round(p1.getX(), 2)
    txtP1y = "y=" , round(p1.getY(), 2)

    txtP2x = "x=" , round(p2.getX(), 2)
    txtP2y = "y=" , round(p2.getY(), 2)
    
    p1Labelx = Text(Point(p1.getX()-5,p1.getY()), txtP1x)
    p1Labely = Text(Point(p1.getX()-5,p1.getY()-2), txtP1y)

    p2Labelx = Text(Point(p2.getX()+5,p2.getY()), txtP2x)
    p2Labely = Text(Point(p2.getX()+5,p2.getY()-2), txtP2y)
    
    p1Labelx.draw(canvas)
    p1Labely.draw(canvas)

    p2Labelx.draw(canvas)
    p2Labely.draw(canvas)
    return

def main():
    circleInfo = getInputValues()
    win = createWindow()
    drawCircle(win, circleInfo)
    P = drawLine(win, circleInfo)
    displayText(win, P[0] , P[1])
    return
