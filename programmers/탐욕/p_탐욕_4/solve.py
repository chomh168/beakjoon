people = [60, 50, 80, 50, 50, 40]*100
limit = 100 
# return = 30000
# people = [70, 80, 50]*100
# limit = 100
# return = 250

from collections  import deque

def solve(people, limit):
    people.sort()
    people = deque(people)
    count = 0
    while len(people) > 1:
        if people[0] + people[-1] > limit:
            people.pop()
            count += 1
        else:
            people.popleft()
            people.pop()
            count += 1

    if len(people) == 1:
        people.pop()
        count += 1

    return count

def solution(people, limit):
    answer = solve(people, limit)
    return answer

print(solution(people, limit))