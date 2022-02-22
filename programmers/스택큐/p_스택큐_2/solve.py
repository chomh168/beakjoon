# param1 = [2, 1, 3, 2]	
# param2 = 2	
#1
# param1 = [1, 1, 9, 1, 1, 1]	
# param2 = 0	
#5
param1 = [1,2,8,3,4]
param2 = 4	
#2
# param1 = [1]
# param2 = 0
#1

priorities = param1
location = param2

def checkOrder(priorities, location):
    orderPriorities = []
    order = 0
    
    orderPriorities = [(idx, each) for idx, each in enumerate(priorities)]
    
    while True:
        orderPriority = orderPriorities.pop(0)
        if len(orderPriorities) == 0 or orderPriority[1] >= max([Priority[1] for Priority in orderPriorities]):
            order += 1
            if orderPriority[0] == location:
                return order
        else:
            orderPriorities.append(orderPriority)

def solution(priorities, location):
    answer = checkOrder(priorities, location)
    return answer

print(solution(priorities, location))