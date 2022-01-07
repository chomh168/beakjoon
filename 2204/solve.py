Dic = []

while 1:
    N = input()
    if N == '0':
        break
    for each in range(int(N)):
        if each == 0:
            word = input()
            Ele = [word]
        else:
            word = input()
            Ele.append(word)
    Dic.append(Ele)

for checkList in Dic:
    checkList.sort(key=lambda x: x.lower())
    print(checkList[0])