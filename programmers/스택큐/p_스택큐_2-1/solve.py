def solution(s):
    answer = True
    if s[0] != '(' or s[-1] != ')':
        return False
    if s.count('(') != s.count(')'):
        return False
    
    count = 0
    for each in s:
        if each == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False


    return answer