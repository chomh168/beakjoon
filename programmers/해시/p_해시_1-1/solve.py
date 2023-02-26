def solution(nums):
    answer = min(len(set(nums)),int(len(nums)/2))
    return answer

print(solution(nums))