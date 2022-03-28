money = [10, 2, 2, 100, 2]#[0,0,2,1,0,0,1]#[1, 2, 3, 1]	#4

def solve(money):
    DP = []
    for idx, cost in enumerate(money[:-1]):
        if idx > 1:
            maxMoney = max(cost + DP[idx - 2], DP[idx - 1])
            DP.append(maxMoney)
        elif idx == 1:
            maxMoney = max(cost, DP[idx - 1])
            DP.append(maxMoney)
        else:
            DP.append(cost)
    first = DP[-1]

    DP = []
    for idx, cost in enumerate(money[1:]):
        if idx > 1:
            maxMoney = max(cost + DP[idx - 2], DP[idx - 1])
            DP.append(maxMoney)
        elif idx == 1:
            maxMoney = max(cost, DP[idx - 1])
            DP.append(maxMoney)
        else:
            DP.append(cost)
    second = DP[-1]
    
    return max(first, second)


def solution(money):
    answer = solve(money)
    return answer

print(solution(money))