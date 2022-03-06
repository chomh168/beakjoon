# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
5
A
BC
DEF
GHJI
KLONM
"""

user_input = int(input())

map = []
# minMap = [ [0] * (user_input) for _ in range(user_input)]
maxMap = [ [0] * (user_input) for _ in range(user_input)]

for _ in range(user_input):
    map.append(input())

map = map[::-1]

for col, each in enumerate(map[0]):
    # minMap[0][col] = (ord(each) - 64)
    maxMap[0][col] = (ord(each) - 64)

for row, strings in enumerate(map[:-1]):
    for col, _ in enumerate(strings[:-1]):
        # minMap[row+1][col] = (ord(map[row+1][col]) - 64) + min(minMap[row][col],minMap[row][col+1])
        maxMap[row+1][col] = (ord(map[row+1][col]) - 64) + max(maxMap[row][col],maxMap[row][col+1])

# print(minMap[user_input-1][0])
print(maxMap[user_input-1][0])