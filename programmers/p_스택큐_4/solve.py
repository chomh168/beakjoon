prices = [1, 2, 3, 2, 3]	
# [4, 3, 1, 1, 0]

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1          
            if prices[j] < prices[i]:
                break

    return answer
    
print(prices)
print(solution(prices))
