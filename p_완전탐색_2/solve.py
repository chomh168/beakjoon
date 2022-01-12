def isPrimeNum(value):
    if value == 1 or value == 0:
        return False
    for num in range(2, int(value ** 0.5)+1):
        if value % num == 0:
            return False
    return True
    
def makeDigit(result, recvCounts, length, nowNum):
    for each in recvCounts:
        each = each.copy()
        counts = recvCounts.copy()
        newNum = nowNum + each[0]
        result.append( newNum )
        if len(newNum) < length + 1:
            if each[1] == 1:
                counts.remove(each)
            else:
                each[1] -= 1
            
            makeDigit(result, counts, length, newNum)
    return result

def countNumber(numbers):
    counts = []
    for each in range(10):
        if numbers.count(str(each)) > 0:
            counts.append([str(each), numbers.count(str(each))])
    return counts

# 0~9, len 1~7
# numbers = "17"	#3
# numbers = "1276543"	#2
# numbers = '232'

def solution(numbers):
    answer = 0
    length = len(numbers)
    numbers = list(numbers)
    numbers.sort()
    counts = countNumber(numbers)

    result = ['0']
    count = 0
    check = makeDigit(result, counts, length, '0')
    check = [ int(x) for x in check ]
    check = set(check)
    for each in check:
        if isPrimeNum(int(each)):
            count+=1
    answer = count
    return answer

# print(solution(numbers))