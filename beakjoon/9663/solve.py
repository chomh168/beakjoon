from sys import stdin
input = stdin.readline

def checkQueen(queenMap, row):
    length = len(queenMap)
    count = 0
    if N == row:
        return 1
    for col in range(N):
        check = True
        for i in range(length):
            if col == queenMap[i] or abs(col - queenMap[i]) == abs(row - i):
                check = False
                break
        if check == True:
            queenMap.append(col)
            count += checkQueen(queenMap, row+1)
            queenMap.pop()
    return count

global N
N = int(input())
count = 0
for i in range(N):
    map = [i]
    count += checkQueen(map, 1)

print(count)
