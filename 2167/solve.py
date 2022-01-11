def caseInput():
    P = [ int(x) for x in input().split(' ')]

    rectMap = []
    for _ in range(P[0]):
        rectMap.append([ int(x) for x in input().split(' ')])

    searchList = []
    N = int(input())

    for _ in range(N):
        searchList.append([ int(x) for x in input().split(' ')])

    return rectMap, P, searchList

def rectSum(rectMap, point):
    result = 0
    for subMap in rectMap[point[0] - 1:point[2]]:
        result += sum(subMap[point[1]- 1:point[3]])
    return result

def findDP(rectMap, DP, P):
    if P[0] == -1 or P[1] == -1:
        return 0
    if DP[P[0]][P[1]] == 0:
        DP[P[0]][P[1]] = rectMap[P[0]][P[1]] + findDP(rectMap, DP, (P[0]-1,P[1])) + findDP(rectMap, DP, (P[0],P[1]-1)) - findDP(rectMap, DP, (P[0]-1,P[1]-1))
    return DP[P[0]][P[1]]

def findSolve(rectMap, DP, search):
    return findDP(rectMap, DP, (search[2]-1,search[3]-1)) - findDP(rectMap, DP,(search[0]-2,search[3]-1)) - findDP(rectMap, DP,(search[2]-1,search[1]-2)) + findDP(rectMap, DP, (search[0]-2,search[1]-2))

rectMap, P, searchList = caseInput()
DP = [[0 for _ in range(P[1])] for _ in range(P[0])]


for index in range(P[1]):
    if index == 0:
        DP[0][index] = rectMap[0][index]
    else:
        DP[0][index] = DP[0][index-1] + rectMap[0][index]
for index in range(P[0]):
    if index == 0:
        DP[index][0] = rectMap[index][0]
    else:
        DP[index][0] = DP[index-1][0] + rectMap[index][0]

for search in searchList:
    print(findSolve(rectMap, DP, search))

"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
"""