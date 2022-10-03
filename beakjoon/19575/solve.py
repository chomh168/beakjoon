from sys import stdin
input = stdin.readline


def solve():
    param = input().split(' ')
    N, x = int(param[0]), int(param[1])

    total = 0
    for index in range(N+1):
        param = input().split(' ')
        if index == 0:
            total = int(param[0])
        else:
            total = (total * x + int(param[0])) % 1000000007

    print(total)
    

solve()