s = "abcdcba"	
#7
s = "abacde"	
#3
# s = "abefbb"
s = "abbb"

from sys import stdin
input = stdin.readline

def solve(s):
    N = len(s)
    dp = [ [0] * N for _ in range(N)]

    max = 1
    for x in range(N):
        dp[x][x] = 1

    for x in range(N-1):
        if s[x] == s[x + 1]:
            dp[x][x+1] = 1
            max = 2

    for y in range(2, N):
        for x in range(0, N-y):
            if s[x] == s[x + y] and dp[x + 1][x + y - 1] == 1:
                dp[x][x + y] = 1
                if y+1 > max:
                    max = y+1

    return max

def solution(s):
    answer = solve(s)
    return answer

print(solution(s))