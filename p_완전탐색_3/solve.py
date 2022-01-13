def makeRectByYellow(yellow):
    yellowRect = []
    for each in range(1, int(yellow**0.5)+1):
        if yellow % each == 0:
            yellowRect.append([max(each, int(yellow/each)),min(each, int(yellow/each))])
    return yellowRect

def makeRectByBrown(yellowRect, brown):
    for each in yellowRect:
        if (each[0] * 2 + each[1] * 2 + 4) == brown:
            return [each[0] + 2, each[1] + 2]

def solution(brown, yellow):
    yellowRect = makeRectByYellow(yellow)
    answer = makeRectByBrown(yellowRect, brown)
    return answer

# 수학적 사고 => 넓이를 통한 접근
# def solution(brown, yellow):
#     mn = brown + yellow
#     for m in range(3, int(mn ** 0.5) + 1):
#         if mn % m == 0 and 2 * (mn // m + m - 2) == brown:
#             return [mn // m, m]