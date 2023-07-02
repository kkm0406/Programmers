def solution(n, k):
    answer = 0
    num = ''
    while n:
        num+=str(n%k)
        n = n//k
    num = num[::-1]
    num = num.split('0')
    for i in num:
        flag = True
        if len(i) == 0 or i == '1':
            continue
        tmp = int(i)
        for j in range(2, int(tmp**0.5)+1):
            if tmp % j == 0:
                print(tmp, j)
                flag = False
        if flag:
            answer+=1
    return answer
