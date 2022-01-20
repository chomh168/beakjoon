# TC
# param1 = [93, 30, 55]	
# param2 = [1, 30, 5]	#[2, 1]
# param1 = [95, 90, 99, 99, 80, 99]	
# param2 = [1, 1, 1, 1, 1, 1]	#[1, 3, 2]
# param1 = [100, 100, 100, 100, 100, 100]	
# param2 = [1, 1, 1, 1, 1, 1]

# progresses = param1
# speeds = param2

def checkCount(progresses, speeds):
    prevDay = 0
    count = 0
    result = []
    for index, each in enumerate(progresses):
        if (each + (speeds[index] * prevDay)) >= 100:
            count += 1
        else:
            if count >= 1:
                result.append(count)
                count = 0

            if (100 - each) % speeds[index] == 0:
                day = ((100 - each - speeds[index] * prevDay) // speeds[index])
            else:
                day = ((100 - each - speeds[index] * prevDay) // speeds[index]) + 1
            
            prevDay += day
            count += 1
        
    result.append(count) 

    return result

def solution(progresses, speeds):
    answer = checkCount(progresses, speeds)
    return answer

# print(solution(progresses, speeds))
