record = [
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]	
result = [
    "Prodo님이 들어왔습니다.", 
    "Ryan님이 들어왔습니다.", 
    "Prodo님이 나갔습니다.", 
    "Prodo님이 들어왔습니다."
]

record = ["Enter uid0606 Gimoi", "Enter uid4567 Prodo", "Leave uid0606", "Enter uid1234 Prodo", "Change uid1234 OhYeah"]
        
def makeAnswer(record):
    subResult = []
    result = []
    idList = {}
    for each in record:
        data = each.split(' ')
        if data[0] == 'Enter':
            subResult.append("{}님이 들어왔습니다.".format(data[1]))
            idList[data[1]] = data[2]
        if data[0] == 'Leave':
            subResult.append("{}님이 나갔습니다.".format(data[1]))
        if data[0] == 'Change':
            idList[data[1]] = data[2]
           
    while subResult != []:
        each = subResult.pop(0)
        uid = each.split('님')[0]
        result.append(each.replace(uid, idList.get(uid)))
    return result

def solution(record):
    answer = makeAnswer(record)
    
    return answer

print(solution(record))