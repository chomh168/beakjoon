# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def connect(n, computers, case):
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if computers[i-1][j-1] == 1:
                case[i].extend(case[j])
                case[j] = case[i]
                case[0] -= 1
    print(case)
    return case[0]


def solution(n, computers):
    case = [n]
    for i in range(n):
        case.append([i+1])
    answer = connect(n, computers, case)
    return answer

print(solution(n, computers))