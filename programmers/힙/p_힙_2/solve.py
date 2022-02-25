jobs = [[0, 3], [1, 9], [2, 6]]	#9
#[[0, 3], [4, 4], [5, 3], [4, 1]]#[[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]#[[0, 3], [0, 2], [1, 9], [2, 6]]#
from collections import deque

def solve(jobs):
    jobs.sort(key=lambda x:[x[0],x[1]])
    jobs = deque(jobs)
    
    checkList = []
    base = jobs.popleft()
    time = [base[1]]
    while len(jobs) != 0:
        checkList = []
        for each in jobs:
            if each[0] <= sum(base):
                checkList.append(each)

        if len(checkList) > 0:
            checkList.sort(key=lambda x:x[1])
            base[1] += checkList[0][1]
            time.append(sum(base) - checkList[0][0])
            jobs.remove(checkList[0])

        else:
            base = jobs.popleft()
            time.append(base[1])

    return sum(time)//len(time)

def solution(jobs):
    answer = solve(jobs)
    return answer

print(solution(jobs))