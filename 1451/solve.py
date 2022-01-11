# input
def caseInput():
    P = [ int(x) for x in input().split(' ')]

    rectMap = []
    for _ in range(P[0]):
        rectMap.append([ int(x) for x in input()])

    return rectMap, P

# point (top, bottom, left, right)
def rectSum(rectMap, point):
    result = 0
    for subMap in rectMap[point[0]:point[1]]:
        result += sum(subMap[point[2]:point[3]])
    return result

def caseTwo(rectMap, P):
    result = [0]
    for i in range(P[0]):
        for j in range(P[1]):
            # v
            if i == P[0] - 1:
                if ((P[1] - j) >= 2):
                    result.append(rectSum(rectMap,(0,i+1,0,j+1)) * veritcalMaxRect(rectMap, P, (0,j+1)))
                if ((P[0]) >= 2):
                    result.append(rectSum(rectMap,(0,i+1,0,j+1)) * horizonMaxRect(rectMap, P, (0,j+1)))
            # h
            elif j == P[1] - 1:
                if ((P[0] - i) >= 2):
                    result.append(rectSum(rectMap,(0,i+1,0,j+1)) * horizonMaxRect(rectMap, P, (i+1,0)))
                if ((P[1]) >= 2):
                    result.append(rectSum(rectMap,(0,i+1,0,j+1)) * veritcalMaxRect(rectMap, P, (i+1,0)))  
                
            # other
            else:
                part1 = rectSum(rectMap,(0,i+1,0,j+1))
                part2 = rectSum(rectMap,(i+1,P[0],0,j+1))
                part3 = rectSum(rectMap,(0,i+1,j+1,P[1]))
                part4 = rectSum(rectMap,(i+1,P[0],j+1,P[1]))
                result.append(part1 * max(((part2+part4) * part3), (part4+part3) * part2))
                
    return max(result)

def veritcalMaxRect(rectMap, P, Q):
    result = [0]
    for i in range(Q[1], P[1] - 1):
        result.append(rectSum(rectMap, (Q[0], P[0], Q[1], i + 1)) * rectSum(rectMap, (Q[0], P[0], i + 1, P[1])))
    return max(result)

def horizonMaxRect(rectMap, P, Q):
    result = []
    for i in range(P[0]):
        result.append(rectSum(rectMap, (Q[0], i + 1, Q[1], P[1])) * rectSum(rectMap, (i + 1, P[0], Q[1], P[1])))
    return max(result)

rectMap, P = caseInput()
print(caseTwo(rectMap, P))