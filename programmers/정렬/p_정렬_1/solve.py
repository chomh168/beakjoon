array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
# [5, 6, 3]

def solve(array, commands):
    result = []
    for command in commands:
        subArr = array[command[0]-1:command[1]]
        subArr.sort()
        result.append(subArr[command[2]-1])
    return result


def solution(array, commands):
    answer = solve(array, commands)
    return answer

print(solution(array, commands))