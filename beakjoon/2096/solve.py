from sys import stdin
input = stdin.readline

N = int(input())
minMaxList = []
minMaxList.append([0,0,0])
minMaxList.append([0,0,0])

for _ in range(N):
    inputList = [ int(x) for x in input().split(' ')]
    prevMinList = minMaxList[0].copy()
    prevMaxList = minMaxList[1].copy()
    
    minMaxList[0][0] = min(prevMinList[0:2]) + inputList[0]
    minMaxList[0][1] = min(prevMinList[0:3]) + inputList[1]
    minMaxList[0][2] = min(prevMinList[1:3]) + inputList[2]

    minMaxList[1][0] = max(prevMaxList[0:2]) + inputList[0]
    minMaxList[1][1] = max(prevMaxList[0:3]) + inputList[1]
    minMaxList[1][2] = max(prevMaxList[1:3]) + inputList[2]

print(max(minMaxList[1]),min(minMaxList[0]))