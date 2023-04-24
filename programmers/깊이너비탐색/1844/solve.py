from collections import deque

def bfs(maps):
    m = len(maps)
    n = len(maps[0])

    que = deque()
    visited = [[0 for _ in range(n)] for _ in range(m)]

    que.append((0,0))
    
    if maps[m-1][n-1] == 0:
        return -1

    while len(que) != 0:
        i,j = que.popleft()
        visited[i][j] = 1
        
        if i != 0:
            if visited[i-1][j] == 0 and maps[i-1][j] == 1:
                maps[i-1][j] += maps[i][j]
                que.append((i-1,j))

        if i != m - 1:
            if visited[i+1][j] == 0 and maps[i+1][j] == 1 :
                maps[i+1][j] += maps[i][j]
                que.append((i+1,j))

        if j != 0:
            if visited[i][j-1] == 0 and maps[i][j-1] == 1:
                maps[i][j-1] += maps[i][j]
                que.append((i,j-1))

        if j != n - 1:
            if visited[i][j+1] == 0 and maps[i][j+1] == 1:
                maps[i][j+1] += maps[i][j]
                que.append((i,j+1))

    if maps[m-1][n-1] == 1:
        return -1

    return maps[m-1][n-1]

def solution(maps):
    # m = len(maps)
    # n = len(maps[0])
    # counts = []
    # dfs(maps,0,0,[],0,m,n,counts)
    # if len(counts) == 0:
    #     return -1
    # answer = min(counts)
    answer = bfs(maps) 
    return answer
