# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1



# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 4
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]

from collections import deque

def connect(n, computers):
    visited = [False] * (n)
    que = deque()
    count = 0
    for i in range(n):
        if visited[i] == False:
            count += 1
            que.append(i)
            while len(que) != 0:
                element = que.popleft()
                visited[element] = True
                for idx, each in enumerate(computers[element]):
                    if each == 1 and visited[idx] == False:
                        print(element, idx)
                        que.append(idx)
    return count
    


def solution(n, computers):
    answer = connect(n, computers)
    return answer

print(solution(n, computers))