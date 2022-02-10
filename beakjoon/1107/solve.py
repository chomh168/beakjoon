from sys import stdin
from itertools import product
input = stdin.readline

N = int(input())
M = int(input())
exceptionList = []
if M != 0:
    exceptionList = [ int(x) for x in input().split(' ')]
numberList = [ x for x in range(10) ]

for each in exceptionList:
    numberList.remove(each)

numberList = numberList

defaultChannel = 100

resultList = []

if N == defaultChannel:
    print(0)
else:
    strN = str(N)
    resultList.append(abs(N-100))
    if M == 0:
        resultList.append(len(strN))
        print(min(resultList))
    else:
        minlen = 1
        if len(strN)-1 > minlen:
            minlen = len(strN)-1
        for each in range(minlen, len(strN)+2):
            for com in list(product(numberList, repeat = each)):
                result = ''
                for char in com:
                    result += str(char)
                resultList.append(abs(N - int(result)) + len(result))
        print(min(resultList))