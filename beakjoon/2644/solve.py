from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

map = [[ 0 for _ in range(N) ] for _ in range(N) ]

for _ in range(M):
    nums = [int(x) for x in input().split(' ')]
    map[nums[0]-1][nums[1]-1] = 1
    map[nums[1]-1][nums[0]-1] = 1


def connect(n, map):
    visited = [False] * (n)
    que = []
    count = 0
    
    visited[0] == True
    que.append(0)
    virusList = []
    
    while len(que) != 0:
        element = que.pop(0)
        visited[element] = True
        for idx, each in enumerate(map[element]):
            if each == 1 and visited[idx] == False:
                visited[idx] = True
                virusList.append(idx+1)
                count += 1
                que.append(idx)
    if 1 in virusList:
        count -= 1
    return count


print(connect(N,map))

"""
7
6
1 2
2 3
2 5
5 2
5 6
4 7
"""

"""
7
5
1 2
2 3
1 3
5 2
5 6
"""