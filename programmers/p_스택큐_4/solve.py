prices = [1, 2, 3, 2, 3]	
# [4, 3, 1, 1, 0]
# prices = [5, 4, 5, 2, 7]
# prices = [1, 2, 3, 2, 3, 1]

#           5, 4, 1, 2, 1, 0
# 5 4 1 2 1 0 
prices = [1, 2, 3, 2, 3, 3, 1]
#[6, 5, 1, 3, 2, 1, 0]

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


# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             answer[i] += 1          
#             if prices[j] < prices[i]:
#                 break

#     return answer