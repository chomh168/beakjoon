N, M = str(input()).split(' ')
checkList = (input()).split(' ')
cQueue = [x for x in range(1, int(N) + 1)]

count = 0

for each in checkList:
    findNum = int(each)
    if cQueue[0] == findNum:
        cQueue = cQueue[1:]
        continue

    findIndex = cQueue.index(findNum)
    qLen = len(cQueue)
    cQueue = cQueue[findIndex:] + cQueue[:findIndex]
    cQueue = cQueue[1:]
    
    if findIndex > (qLen/2):
        count += (qLen - findIndex)
    else:
        count += findIndex

print(count)