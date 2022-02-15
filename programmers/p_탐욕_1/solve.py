n = 3	
lost = [3]	
reserve = [1]	
# 5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2

n, lost, reserve = (
    6,[6,2,4],[1,5,3] 
)

n, lost, reserve = (
    3,	[3],	[1]
)
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2


result = []
def solve(n, lost, reserve):
    if len(lost) == 0 or len(reserve) == 0:
        global result
        result.append(n - len(lost))
        return
    each = reserve.pop()
    
    check = False
    if lost.count(each - 1) == 1:
        rlost = lost.copy()
        rlost.remove(each-1)
        solve(n, rlost, reserve)
        check = True
    if lost.count(each + 1) == 1:
        rlost = lost.copy()
        rlost.remove(each+1)
        solve(n, rlost, reserve)
        check = True
    
    if check == False:
        solve(n, lost, reserve)
    

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
    result.append(n-len(newLost))
    solve(n, newLost, newReserve)
    return max(result)

print(solution(n, lost, reserve))