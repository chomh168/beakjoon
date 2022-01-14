def makeReulst(numbers, target, index, nowResult):
    if index == len(numbers):
        return int(nowResult == target)
    else:
        count  = makeReulst(numbers, target, index + 1, nowResult + numbers[index])
        count += makeReulst(numbers, target, index + 1, nowResult - numbers[index])
        return count

def solution(numbers, target):
    answer = makeReulst(numbers, target, 0, 0)
    return answer
