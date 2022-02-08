from sys import stdin
input = stdin.readline

N = int(input())
board = list(map(int, input().split()))
dp = [ [0] * N for _ in range(N)]

for x in range(N):
    dp[x][x] = 1

for x in range(N-1):
    if board[x] == board[x + 1]:
        dp[x][x+1] = 1

for y in range(2, N):
    for x in range(0, N-y):
        if board[x] == board[x + y] and dp[x + 1][x + y - 1] == 1:
            dp[x][x + y] = 1

M = int(input())

result = []
for _ in range(M):
    indexs = list(map(int, input().split()))
    print(dp[indexs[0]-1][indexs[1]-1])


# 8
# 1 2 1 3 1 2 1 1
# 5
# 1 3
# 2 5
# 3 3
# 5 7
# 7 8