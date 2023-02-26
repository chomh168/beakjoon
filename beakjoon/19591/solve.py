from sys import stdin
input = stdin.readline


def solve():
    param = input()

    print(findOperation(param))
    
def findOperation(param):
    listIndex = []
    for each in ['*','/','+','-']:
        if param.find(each) != -1:
            listIndex.append(param.find(each))

    return min(listIndex)

solve()