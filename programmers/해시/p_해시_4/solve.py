genres = ["classic", "pop", "classic", "classic", "pop", "pop","ballad","ballad"]	
plays = [500, 600, 150, 800, 2500, 700, 2000, 500]	
#[4, 1, 3, 0]

def solve(genres, plays):
    result = []
    totalDoc = {}
    for idx, each in enumerate(genres):
        if totalDoc.get(each) is None:
            totalDoc[each] = {'sum':0,'gList':[]}
        totalDoc.get(each)['sum'] += plays[idx]
        totalDoc.get(each).get('gList').append([idx, plays[idx]])

    

    while totalDoc != {}:
        maxList = [0,'']
        for each in totalDoc:
            if maxList[0] < totalDoc.get(each).get('sum'):
                maxList[0] = totalDoc.get(each).get('sum')
                maxList[1] = each
        gListDoc = totalDoc.pop(maxList[1]).get('gList')
        gListDoc.sort(key=lambda x : (-x[1],x[0]))
        for each in gListDoc[:2]:
            result.append(each[0])
    
    return result

def solution(genres, plays):
    answer = solve(genres, plays)
    return answer

print(solution(genres, plays))