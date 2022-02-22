n = 3	
lost = [3]	
reserve = [1]	
# 5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2

n, lost, reserve = (
    6,[6,2,4],[1,5,3] 
)

# n, lost, reserve = (
#     3,	[3],	[1]
# )
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2


result = []
def solve(n, lost, reserve):
    removeCount = 0
    for each in lost:
        if each - 1 in reserve:
            removeCount += 1
            reserve.remove(each-1)
        elif each + 1 in reserve:
            removeCount += 1
            reserve.remove(each+1)

    return len(lost) - removeCount

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost = list(set(lost))
    reserve = list(set(reserve))
    newLost = []
    newReserve = reserve.copy()
    for each in lost:
        if reserve.count(each) == 1:
            newReserve.remove(each)
            continue
        newLost.append(each)
    so = solve(n, newLost, newReserve)
    return n - so

print(solution(n, lost, reserve))