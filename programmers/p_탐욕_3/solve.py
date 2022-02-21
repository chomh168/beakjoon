number = "1924"	
k = 2	#"94"
number = "1242"	
k = 3	#"242"
number = "1231234"	
k = 3	#"3234"
number = "4177252841"	
k = 4	#"775841"
# number = "1299"	
# k = 2	#"99"
# number = "1121"	
# k = 2	#"99"


def solve(number, k):
    if len(number) - 1 == k:
        return max(number)
    if k == 1:
        return number.replace(min(number),'',1)

    stack = []
    for idx, num in enumerate(number):
        if stack == []:
            stack.append(num)
            continue
        
        while True:
            if stack == []:
                stack.append(num)
                break
            
            if stack[-1] < num:
                stack.pop()
                k -= 1
                if k == 0:
                    break
            else:
                stack.append(num)
                break
        
        if k == 0:
            stack.extend(number[idx:])
            break
            
    return ''.join(stack)
    

def solution(number, k):
    answer = solve(number, k)
    return answer

print(solution(number, k))