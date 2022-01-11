firstStudent  = [1, 2, 3, 4, 5]
secondStudent = [2, 1, 2, 3, 2, 4, 2, 5]
thirdStudent  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solve(param):
    result = []
    score = [0,0,0]

    for count, each in enumerate(param):
        if each == firstStudent[count%len(firstStudent)]:
            score[0] += 1
        if each == secondStudent[count%len(secondStudent)]:
            score[1] += 1
        if each == thirdStudent[count%len(thirdStudent)]:
            score[2] += 1

    for count, each in enumerate(score):
        if each == max(score):
            result.append(count+1)

    return result


def solution(answers):
    return solve(answers)


answers = [1,3,2,4,2]#	[1]

print(solution(answers))