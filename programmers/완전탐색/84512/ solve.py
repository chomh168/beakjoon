import itertools


def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U', '']
    words = []

    for combi in itertools.product(arr, repeat= (len(arr) - 1)):
        iword = ''
        for each in combi:
            iword += each

        if iword not in words:
            words.append(iword)

    words.sort()
    answer = words.index(word)
    return answer

print(solution('AAAAE'))