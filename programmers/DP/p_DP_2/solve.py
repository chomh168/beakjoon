triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	#30

def solution(triangle):
    for index,line in enumerate(triangle):
        if len(line) == 1:
            continue
        for li, _ in enumerate(line):
            if li == 0:
                line[li] += triangle[index-1][li]
            elif li == len(line) - 1:
                line[li] += triangle[index-1][li-1]
            else:
                line[li] += max(triangle[index-1][li-1],triangle[index-1][li])

    answer = max(triangle[index])
    return answer

print(solution(triangle))