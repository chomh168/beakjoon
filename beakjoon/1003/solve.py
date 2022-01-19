N = int(input())
checkList = []

checkCount = [[1, 0],[0, 1]]

def checkNumberCount(index):
    if index < 2 or len(checkCount) > index:
        return checkCount[index]
    
    checkOne = checkNumberCount(index - 1)
    checkTwo = checkNumberCount(index - 2)
    checkCount.append([checkOne[0]+checkTwo[0],checkOne[1]+checkTwo[1]])
    return checkCount[index]

for _ in range(N):
    checkList.append(int(input()))

for each in checkList:
    print(checkNumberCount(each)[0], checkNumberCount(each)[1])