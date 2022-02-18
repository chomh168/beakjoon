name = "JEROEN"	#56
# name = "JAN"	#23
# name = "JAZ"	#11
name = "ABABAABA" #9
name = "AAAABABAAAA" #8
name = "BAAAABAAAAB" #8
name = "AABAAAAB" #8

def solve(name):
    minChar = ord("A")
    maxChar = ord("Z")
    count = 0
    
    cursorCount = len(name) - 1
    subIdx = 0
    
    for idx, each in enumerate(name):
        nowChar = ord(each)
        count += min(nowChar-minChar, maxChar-nowChar+1)
        
        subIdx = idx + 1
        while subIdx < len(name):
            if name[subIdx] == "A":
                subIdx += 1
            else:
                cursorCount = min(cursorCount, idx * 2 + len(name) - subIdx)
                cursorCount = min(cursorCount, idx + (len(name) - subIdx) * 2)
                # 처음부터 뒤에서 탐색
                break
        
        if subIdx == len(name):
            cursorCount = min(cursorCount, len(name) - (subIdx - idx))

    return count + cursorCount

def solution(name):
    answer = solve(name)
    return answer

print(solution(name))