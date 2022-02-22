p1="hit"	
p2="cog"	
p3=["hot", "dot", "dog", "lot", "log", "cog"]	#4
# p1="hit"	
# p2="cog"	
# p3=["hot", "dot", "dog", "lot", "log"]	#0

begin = p1
target = p2
words = p3

from collections import deque

def bfs(begin, target, words):
    if not target in words:
        return 0
    checkList = deque()
    checkList.append((begin, 0))
    
    while len(checkList) != 0:
        check, count = checkList.popleft()
        for word in words:
            if wordCheck(word, check):
                if word == target:
                    return count+1
                checkList.append((word, count+1))

def wordCheck(word, check):
    count = 0
    for idx, each in enumerate(word):
        if each == check[idx]:
            count += 1
    if count == len(word) - 1:
        return True
    return False

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer

print(solution(begin, target, words))