citations = [3, 0, 6, 1, 5, 2]	#3
# from audioop import reverse


# citations = [0, 0, 0, 1, 10, 2]	#3
citations = [8, 7, 7, 6, 5, 5, 3, 0, 0, 0]

show = {}
citations.sort()
for each in citations:
    show[each] = citations.count(each)
print(show)

def solution(citations):
    if len(citations) == 1:
        if citations[0] == 0:
            return 0
        return 1
    
    citations.sort()
    pivot = 0
    while len(citations) != 0:
        all = len(citations)
        candi = citations.pop(0)
        candiCount = citations.count(candi)
        if candiCount > 0:
            citations = citations[candiCount:]

        if all > candi:
            pivot = max([pivot, candi])
        else:
            pivot = max([pivot, all])
    return pivot
            

print(solution(citations))