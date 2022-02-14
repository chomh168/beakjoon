from sys import stdin
input = stdin.readline

N = [int(x) for x in input().split(' ')]

dp = [[0]*(33) for i in range(33)]

for i in range(33):
    dp[0][i] = 1
    dp[i][0] = 1

def makeTable(all, one):
    if dp[all][one] != 0:
        return dp[all][one]
    if all == 0 or one == 0:
        return dp[all][one]

    dp[all][one] = makeTable(all-1, one-1) + makeTable(all-1, one)

    return dp[all][one]

makeTable(N[0], N[1])

for n in range(N[0], 0, -1):
    if N[2] <= dp[n-1][N[1]]:
        print('0', end="")
    else:
        print('1', end="")
        N[2] -= dp[n-1][N[1]]
        N[1] -= 1