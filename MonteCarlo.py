from random import randint
from matplotlib import pyplot
import numpy

def playOneGame():
    rollResult = randint(1, 6) + randint(1, 6)
    if rollResult == 7 or rollResult == 11:
        return 1
    elif rollResult == 2 or rollResult == 3 or rollResult == 12:
        return -1
    else:
        count = 1
        rollResult2 = 0
        while rollResult2 != rollResult and rollResult2 != 7:
            count += 1
            rollResult2 = randint(1, 6) + randint(1, 6)
        if rollResult2 == rollResult:
            return count
        else:
            return (-1)*count
    return

def tallyResults(n):
    winList  = []
    lossList = []
    winListRolls  = []
    lossListRolls = []
    for i in range(n):
        rollCount = playOneGame()
        if rollCount > 0:
            winList.append(rollCount)
            lossList.append(0)
        else:
            lossList.append(-rollCount)
            winList.append(0)

    for i in range(1, max(max(winList), max(lossList))+1):
        winListRolls.append(winList.count(i))
        lossListRolls.append(lossList.count(i))
    
    return winListRolls, lossListRolls

def plotResults(n):
    winListPercentage  = []
    lossListPercentage = []
    wList, lList = tallyResults(n)

    for i in range(len(wList)):
        winListPercentage.append(wList[i]*100/(sum(wList)+sum(lList)))
        lossListPercentage.append(lList[i]*100/(sum(wList)+sum(lList)))

    print(sum(winListPercentage))
    print(sum(lossListPercentage))
    
    fig = pyplot.figure(figsize=(30,10))
    fig.add_subplot(111)
    index = numpy.arange(len(wList))+1
    pyplot.bar(index-0.15, winListPercentage, 0.3, color = 'b', align='center')
    pyplot.bar(index+0.15, lossListPercentage, 0.3, color ='g', align='center')
    pyplot.xticks(index)
    pyplot.yticks(numpy.arange(0, max(max(winListPercentage), max(lossListPercentage))+1,1))
    pyplot.grid(True)
    pyplot.show()
    return
