import graphics
import csv

def initializeMap(mapFile, xPixels, yPixels):
    win = graphics.GraphWin('Scaramento Area', xPixels, yPixels)
    win.setCoords(0, 0, xPixels, yPixels)
    center = graphics.Point( xPixels/2, yPixels/2)

    image = graphics.Image(center, mapFile)
    image.draw(win)

    return win

def LatLongToPixels(latitude, longitude):
    x = round((707*(39.03-latitude))/0.79)
    y = round((744*abs(120.6-longitude))/0.96)

    return x,y

def getLatLongValues2(dataFile):
    file = open(dataFile, 'r')

    file.readline()

    latLongList = []
    
    for line in file:
        lineList = line.split(',')
        latLongList.append((float(lineList[-2]), abs(float(lineList[-1]))))

    return latLongList

def getLatLongValues(dataFile):
    file = open(dataFile, 'r')

    dictReader = csv.DictReader(file)

    latLongList = []
    
    for lineDict in dictReader:
        latLongList.append((float(lineDict['latitude']), abs(float(lineDict['longitude']))))

    return latLongList

def plotCircle(latitude, longitude, win, color):
    x, y = LatLongToPixels(latitude, longitude)
    
    circle = graphics.Circle(graphics.Point(x, y), 5)
    circle.setFill(color)
    circle.draw(win)
    return

def main(dataFile):
    win = initializeMap("SacramentoMap.gif", 707, 744)
    
    latLongDict = getLatLongValues(dataFile)

    for latLongValue in latLongDict:
        plotCircle(latLongValue[0], latLongValue[1], win, 'red')

    return
