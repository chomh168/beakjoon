numbers = [6, 10, 2]	#"6210"
numbers = [3, 30, 34, 5, 9]	#"9534330"
# numbers = [3, 30, 34, 5, 9, 31]	#"9534330"

numbers = [3, 34, 342, 5, 9]
# numbers = [1, 10, 100, 1000]

from functools import cmp_to_key

def str_cmp(a,b):
    if a+b>b+a:
        return -1
    if a+b<b+a:
        return 1
    if a+b==b+a:
        return 0

def solve(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(str_cmp))
    result = ''
    for number in numbers:
        result += number
    if int(result) == 0:
        return '0'
    return result

def solution(numbers):
    answer = solve(numbers)
    return answer

print(solution(numbers))