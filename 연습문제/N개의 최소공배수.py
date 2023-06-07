import math 
def solution(arr):
    answer = 0
    arr.sort()
    num = arr[0]
    for i in range(1, len(arr)):
        gcd = math.gcd(num, arr[i])
        num = num*arr[i]//gcd
    answer = num
    return answer
