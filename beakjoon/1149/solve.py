from sys import stdin
input = stdin.readline

N = int(input())
minList = [0] * 3

for _ in range(N):
    inputList = [ int(x) for x in input().split(' ')]
    prevMinList = minList.copy()
    
    minList[0] = min(prevMinList[1:3]) + inputList[0]
    minList[2] = min(prevMinList[0:2]) + inputList[2]
    prevMinList.pop(1)
    minList[1] = min(prevMinList) + inputList[1]

print(min(minList))

