# arr = ["1", "-", "3", "+", "5", "-", "8"]	#2
arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	#3

def solution(arr):
    answer = -1
    
    numList = [int(arr[0])]
    for idx in range(len(arr)//2): #
        numList.append(int(arr[idx * 2 + 1] + arr[idx * 2 + 2]))
    
    minmax = [numList[-1],numList[-1]]
    stackSum = 0
    numList = numList[:-1]

    for idx, each in enumerate(numList[::-1]):
        if each < 0:
            premin = minmax[0]
            premax = minmax[1]
            minmax[0] = min((abs(each) + stackSum + premax) * -1, (abs(each) + stackSum) * -1 + premin)
            minmax[1] = max((abs(each) + stackSum + premin) * -1, each + stackSum + premax)

            stackSum = 0

        else:
            stackSum += each

    answer = minmax[1] + stackSum
    return answer

print(solution(arr))
