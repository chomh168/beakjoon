def solution(sizes):
    new = []
    new0 = []
    new1 = []
    for each in sizes:
        if each[0] > each[1]:
            new0.append(each[0])
            new1.append(each[1])
        else:
            new0.append(each[1])
            new1.append(each[0])

    answer = max(new0) * max(new1)
    return answer

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]] #4000
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]] #120
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] #133

print(solution(sizes))