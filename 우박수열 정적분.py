def solution(k, ranges):
    answer = []
    n = k
    arr = [k]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        arr.append(n)
    
    for x1, x2 in ranges:
        x2 = len(arr) + x2
        area = arr[x1: x2]
        if x1 >= x2:
            answer.append(-1)
        else:
            size = 0
            for i in range(1, len(area)):
                size += (area[i-1] + area[i])/2
            answer.append(size)
    return answer
