A = [ int(x) for x in input().split(' ')]

startValue = max(A[0], A[1])/2

while 1:
    if A[0] % startValue == 0 and A[1] % startValue == 0:
        LCM = startValue
        GCD = LCM * (A[0] / startValue) * (A[1] / startValue)
        break
    else:
        startValue -= 1

print(int(LCM))
print(int(GCD))