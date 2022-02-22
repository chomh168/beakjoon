def solution(clothes):
    group = groupByType(clothes)
    answer = checkProbability(group)
    return answer

def groupByType(clothes):
    result = {}
    for cloth in clothes:
        if result.get(cloth[1]):
            result[cloth[1]] = result.get(cloth[1]) + 1
        else:
            result[cloth[1]] = 1
    return result

def checkProbability(group):
    result = 1
    for cloth in group:
        if len(group) == 1:
            return group.get(cloth)
        result *= (group.get(cloth) + 1)
    return result - 1