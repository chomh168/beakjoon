from sys import stdin
input = stdin.readline


def solve():
    AB, AC, BC = input().split(' ')

    AB = int(AB)
    BC = int(BC)
    AC = int(AC)

    ABC = (AB + AC + BC) / 2

    A = ABC - BC
    B = ABC - AC
    C = ABC - AB

    for num in [A,B,C]:
        if num <= 0:
            print(-1)
            return 0
    
    print(1)
    print(round(A,1), round(B,1), round(C,1))

solve()