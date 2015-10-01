
def readWords(strFilePath):
    fileList = []
    wordList = []
    tupleList = []
    count = 0
    file = open(strFilePath, 'r')
    fileList = file.read()
    file.seek(0,0)
    #print(fileList)
    for line in file:
        for word in line.split():
            if word not in wordList:
                wordList.append(word)
                tupleList.append((fileList.count(word), word))
            count += 1
    print('Total: ', count, ' , Unique: ', len(wordList))
    file.close()
    return sorted(tupleList)

def writeWords(tupleList):
    file = open('sortedWords.txt', 'w')

    for oneTuple in tupleList:
        file.write(str(oneTuple) + '\n')

    file.close()
    return

def processFile(strFilePath):
    tupleList = readWords(strFilePath)
    writeWords(tupleList)
    return
