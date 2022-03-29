# operations = ["I 16","D 1"]	#[0,0]
operations = ["I 7","I 5","I -5","D -1"]	#[7,5]

def solve(operations):
    que = []
    for each in operations:
        command = each.split(' ')
        if command[0] == 'I':
            que.append(int(command[1]))
        else:
            if len(que) > 0:
                que.sort()
                if command[1] == '1':
                    que.pop()
                else:
                    que = que[1:]
    
    if len(que) > 0:
        que.sort(reverse=True)
        return [que[0],que[-1]]
    return [0,0]


def solution(operations):
    answer = solve(operations)
    return answer

print(solution(operations))