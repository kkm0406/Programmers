from math import gcd
def solution(arrayA, arrayB):
    gcd_a = arrayA[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
    gcd_b = arrayB[0]
    for i in range(1, len(arrayB)):
        gcd_b = gcd(gcd_b, arrayB[i])
        
    flag_a, flag_b = True, True
    for i in range(len(arrayA)):
        if arrayA[i] % gcd_b == 0:
            flag_a = False
        if arrayB[i] % gcd_a == 0:
            flag_b = False

    if flag_a and flag_b:
        return max(gcd_a, gcd_b)
    elif flag_a and not flag_b:
        return gcd_b
    elif flag_b and not flag_a:
        return gcd_a
    elif not flag_a and not flag_b:
        return 0
