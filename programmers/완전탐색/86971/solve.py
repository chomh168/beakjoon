import copy

def findOne(inWires):
    queue = inWires.pop()
    connected = 2
    while len(queue) != 0:
        key = queue.pop()
        tempwires =  copy.deepcopy(inWires)
        for each in tempwires:
            count = each.count(key)
            if count == 1:
                idx = each.index(key)
                otherKey = each[(idx + 1) % 2]
                queue.append(otherKey)
                inWires.remove(each)
                connected += 1
    return inWires, connected

def solution(n, wires):
    answers = []
    for each in wires:
        print(each, wires)
        tempwires = copy.deepcopy(wires)
        tempwires.remove(each)
        reservedWires, firstCount = findOne(tempwires)
        if reservedWires == []:
            answers.append(firstCount-1)
        else:
            lastWires, secondCount = findOne(reservedWires)
            if lastWires == []:
                answers.append(abs(firstCount - secondCount))

    return min(answers)


n = 9
wires = [[1,2],[2,3],[3,4]]#[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

print(solution(n, wires))
