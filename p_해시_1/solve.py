def solution(participant, completion):
    p = check(participant)
    c = check(completion)
    for name in c:
        if p.get(name):
            if c.get(name) == p.get(name):
                p.pop(name)
    for name in p:
        answer = name
    return answer

def check(checkList):
    result = {}
    for each in checkList:
        if result.get(each):
            result[each] = result.get(each) + 1
        else:
            result[each] = 1
    return result
