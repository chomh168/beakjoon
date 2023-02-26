N = input()

S = []

for _ in range(int(N)):
    S.append(input())

print(S)

T = []

for _ in range(len(S)):
    if S[0] < S[-1]:
        T.append(S[0])
        S = S[1:]
    elif S[0] > S[-1]:
        T.append(S[-1])
        S = S[:-1]
    elif S[0] == S[-1] and len(S) > 3:
        if S[1] < S[-2]:
            T.append(S[0])
            S = S[1:]
        elif S[1] > S[-2]:
            T.append(S[-1])
            S = S[:-1]
        else:
            T.append(S[0])
            S = S[1:]
    else:
        T.append(S[0])
        S = S[1:]

print(T)