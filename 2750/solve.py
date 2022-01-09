N = input()
numberList = []

for _ in range(int(N)):
    numberList.append(int(input()))

numberList.sort()
for each in numberList:
    print(each)
