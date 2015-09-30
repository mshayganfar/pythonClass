
def timeToSeconds(time):
    timeSplitted = time.split(':')
    print(timeSplitted)
    print((eval(timeSplitted[0])*3600)+(eval(timeSplitted[1])*60)+(eval(timeSplitted[2])))
    return

def secondsToTime(totalSeconds):
    seconds = totalSeconds % 60
    minutes = (totalSeconds // 60) % 60
    hours   = (totalSeconds // 3600)
    
    hour   = hours if hours > 9 else '0'+str(+hours)
    minute = minutes if minutes > 9 else '0'+str(+minutes)
    second = seconds if seconds > 9 else '0'+str(+seconds)

    time = "{0}:{1}:{2}"
    print(time.format(hour, minute, second))
    return

def parseDate(dateString):
    dateList = []
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    splittedDate = dateString.split(" ")
    dateList.append(int((months.find(splittedDate[0])/3)+1))
    dateList.append(int(splittedDate[1]))
    dateList.append(int(splittedDate[2]))
    return dateList

