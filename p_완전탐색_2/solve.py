def isPrimeNum(value):
    if value == 1 or value == 0:
        return False
    for num in range(2, int(value ** 0.5)+1):
        if value % num == 0:
            return False
    return True
    
def makeDigit(result, recvCounts, length, nowNum):
    prevNum = '-1'
    for each in recvCounts:
        counts = recvCounts.copy()
        if prevNum == each:
            continue
        prevNum = each
        newNum = nowNum + each
        result.append( newNum )
        if len(newNum) < length + 1:
            counts.remove(each)
            makeDigit(result, counts, length, newNum)
    return result
    
def solution(numbers):
    answer = 0
    length = len(numbers)
    numbers = list(numbers)
    numbers.sort()

    result = []
    check = makeDigit(result, numbers, length, '')
    check = [int(x) for x in check ]
    for each in set(check):
        print(each)
        if isPrimeNum(int(each)):
            answer+=1
    return answer
