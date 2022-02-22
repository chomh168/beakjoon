m = 4	
n = 3	
puddles = [[2, 2]]#	4

def solve(m, n, puddles):
    DP = [ [0] * (n+1) for _ in range(m+1)]

    DP[1][1] = 1
    for x in range(1,n+1):
        for y in range(1,m+1):
            if [y,x] in puddles or (x == 1 and y == 1):
                continue
            DP[y][x] = (DP[y-1][x] + DP[y][x-1]) % 1000000007
    
    return DP[m][n]

def solution(m, n, puddles):
    answer = solve(m, n, puddles)
    return answer

print(solution(m, n, puddles))