n = 6	
times = [7, 10]	#28

"""
def solve(n,times):
    times.sort()
    left = [0] * len(times)
    count = [0] * len(times)
    rooms = [times, left, count]
    for _ in range(n):
        # check = False
        minList = []
        for index, leftTime in enumerate(rooms[1]):
            # if leftTime <= 0:
            #     rooms[1][index] += rooms[0][index]
            #     rooms[2][index] += rooms[0][index]
            #     check = True
            #     break
            minList.append(leftTime + rooms[0][index])
        # if check == False:
        minIndex = minList.index(min(minList))
        for index, _ in enumerate(rooms[1]):
            rooms[1][index] -= rooms[0][minIndex]
        rooms[1][minIndex] += rooms[0][minIndex]
        rooms[2][minIndex] += rooms[0][minIndex]

    return max(rooms[2])
"""

def solve(n, times):
    times.sort()
    leftTime, rightTime = 1, times[-1] * n
    midTime = (leftTime + rightTime) // 2

    while leftTime <= rightTime:
        count = 0
        for time in times:
            count += midTime // time

            if count > n:
                break

        if count >= n:
            rightTime = midTime - 1
        else:
            leftTime = midTime + 1
        midTime = (leftTime + rightTime) // 2

    return leftTime

def solution(n, times):
    answer = solve(n,times)
    return answer

print(solution(n, times))