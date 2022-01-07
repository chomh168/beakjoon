Dic = []

while 1:
    N = input()
    if N == '0':
        break
    for each in range(int(N)):
        if each == 0:
            word = input()
            Ele = [(word,word.lower())]
        else:
            word = input()
            Ele.append((word,word.lower()))
    Dic.append(Ele)

for checkList in Dic:
    checkList.sort(key=lambda x:x[1])
    print(checkList[0][0])