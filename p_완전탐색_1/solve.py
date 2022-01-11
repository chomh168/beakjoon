firstStudent  = [1, 2, 3, 4, 5]
secondStudent = [2, 1, 2, 3, 2, 4, 2, 5]
thirdStudent  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solve(param):
    one = [1,0]
    two = [2,0]
    thr = [3,0]
    
    count = 0
    for each in param:
        if each == firstStudent[count%len(firstStudent)]:
            one[1] += 1
        if each == secondStudent[count%len(secondStudent)]:
            two[1] += 1
        if each == thirdStudent[count%len(thirdStudent)]:
            thr[1] += 1
        count += 1
    
    compare = [one,two,thr]
    compare.sort(key=lambda x:(-x[1],x[0]))

    result = []
    max = compare[0][1]
    for each in compare:
        if each[1] == max:
            result.append(each[0])

    return result


def solution(answers):
    answer = []
    return solve(answers)
