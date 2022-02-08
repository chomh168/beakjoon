s = "abcdcba"	
#7
# s = "abacde"	
#3
# s = "abefbb"

import re

def solve(s):
    leng = 0
    while len(s) != 0:
        checkList = []
        checkChar = s[0]
        

        for m in re.finditer(checkChar, s):
            checkList.append(m.start()+1)

        print(checkList)
        checkList.sort(reverse=True)
        result = True
        check = 0
        for check in checkList:
            if check == 1:
                check = 1
                break
            for each in range(1, check//2+1):
                if check == 6:
                    print(s[check - each], s[each], check - each, each)
                if s[check - each] != s[each]:
                    result = False
                    break
            if result == True:
                break
        if leng < check and result == True:
            leng = check
        s = s[1:]
    return leng + 1
    
    
def solution(s):
    answer = solve(s)
    return answer

print(solution(s))