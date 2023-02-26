def solution(arr):
    answer = []
    preEach = -1
    for each in arr:
        if preEach != each:
            answer.append(each)
        preEach = each
    return answer


arr = [1,1,3,3,0,1,1]

print(solution(arr))