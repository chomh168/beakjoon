N = input()
A = str(input()).split(' ')
B = str(input()).split(' ')
A = [ int(x) for x in A ]
B = [ int(x) for x in B ]

A.sort()
B.sort(reverse=True)

C = 0
for index in range(int(N)):
    C += (A[index] * B[index])

print(C)
