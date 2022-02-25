

scoville = [1, 2, 3, 9, 10, 12]	
K = 7	
#2

# scoville = [1, 1, 1, 10, 1]	
# K = 5

scoville = [1,2,3,4]
K = 8

import heapq

def solve(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        count += 1
        new = a + 2 * b
        heapq.heappush(scoville, new)

        if len(scoville) <= 1 and scoville[0] < K:
            return -1
    return count

def solution(scoville, K):
    answer = solve(scoville, K)
    return answer

print(solution(scoville, K))