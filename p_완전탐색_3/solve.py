# 10	2	[4, 3]
# 8	1	[3, 3]
brown = 10
yellow = 2



def makeRectByYellow(yellow):
    yellowRect = []
    for each in range(1, yellow//2+2):
        if yellow % each == 0:
            yellowRect.append([max(each, int(yellow/each)),min(each, int(yellow/each))])
    return yellowRect

def makeRectByBrown(yellowRect, brown):
    for each in yellowRect:
        if (each[0] * 2 + each[1] * 2 + 4) == brown:
            return [each[0] + 2, each[1] + 2]

# yellowRect = makeRectByYellow(yellow)
# print(yellowRect)
# print(makeRectByBrown(yellowRect, brown))

def solution(brown, yellow):
    yellowRect = makeRectByYellow(yellow)
    # print(yellowRect)
    answer = makeRectByBrown(yellowRect, brown)
    return answer

print(solution(brown, yellow))