# p1 = 2	
# p2 = 10	
# p3 = [7,4,5,4]	
# 7

# p1 = 2	
# p2 = 10	
# p3 = [7,4,5,6]	
# 8

# p1 = 3	
# p2 = 10	
# p3 = [2,3,4,5]
# 8

# p1 = 100	
# p2 = 100	
# p3 = [10]	
#101

# p1 = 100
# p2 = 100
# p3 = [10,10,10,10,10,10,10,10,10,10]
#110

p1 = 5	
p2 = 5	
p3 = [2, 2, 2, 2, 1, 1, 1, 1, 1]
# 19

# p1 = 1	
# p2 = 2	
# p3 = [1, 1, 1]
# #4

# p1 = 5	
# p2 = 5	
# p3 = [2,2,2,2]
# 12

bridge_length = p1
weight = p2
truck_weights = p3

def check(bridge_length, weight, truck_weights):
    time = 1
    bridge = [0] * (bridge_length - 1)
    bridge.append(truck_weights.pop(0))
    while not sum(bridge) == 0:
        if len(truck_weights) == 0:
            break
        time += 1
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            if bridge[0] == 0:
                for idx, truck in enumerate(bridge):
                    if truck != 0:
                        break
                bridge = bridge[idx+1:] + [0] * (idx + 1)
                time += idx + 1
                if sum(bridge) + truck_weights[0] <= weight:
                    bridge.append(truck_weights.pop(0))
                else:
                    bridge.append(0)
            else:
                bridge.append(0)
            

    return time + bridge_length

def solution(bridge_length, weight, truck_weights):
    answer = check(bridge_length, weight, truck_weights)
    return answer

print(solution(bridge_length, weight, truck_weights))