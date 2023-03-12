from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for dungeon in dungeons:
        if dungeon[0] > k:
            dungeons.remove(dungeon)
        
    for dungeonCombi in permutations(dungeons):
        count, tempK = 0, k
        outCondi = False
        for dungeon in dungeonCombi:
            if outCondi == True:
                break
            
            if tempK >= dungeon[0]:
                tempK -= dungeon[1]
                count += 1
            else:
                outCondi = True
                break
        answer = max(count,answer)
    
    return answer



k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))