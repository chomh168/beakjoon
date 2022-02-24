N = 5	
number = 12
#	4
# N = 2	
# number = 11	
#3

def solve(N, number):
    if N == number:
        return 1
    dp = [[],[],[],[],[],[],[],[],[]]

    dp[1] = [int(N)]

    for num in range(2,9):
        dp[num].append(int(str(N)*num))
        for com in range(1,num):
            for each1 in dp[num-com]:
                for each2 in dp[com]:
                    if dp[num].count(each1+each2) == 0:
                        dp[num].append(each1+each2)
                    if dp[num].count(each1-each2) == 0 and each1-each2 > 0:
                        dp[num].append(each1-each2)
                    if dp[num].count(each1*each2) == 0:
                        dp[num].append(each1*each2)
                    if dp[num].count(each1//each2) == 0:
                        dp[num].append(each1//each2)
        
            if number in dp[num]:
                return num
            for _ in range(dp[num].count(0)):
                dp[num].remove(0)

    return -1
                
def solution(N, number):
    answer = solve(N, number)
    return answer

# print(solution(N, number))
print(solution(2,22223),7)