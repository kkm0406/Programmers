one, zero = 0, 0
def divide(arr, n):
    global one, zero
    sum = 0
    for i in arr:
        for j in i:
            sum += j
    if sum == 0:
        zero += 1
        return
    elif sum == n*n:
        one += 1
        return
    
    if n == 2:
        tmp_one, tmp_zero = 0, 0
        tmp_sum = 0
        for i in arr:
            for j in i:
                if j == 1:
                    one += 1
                else:
                    zero += 1
    else:
        tmp = [arr[i][:n//2] for i in range(n//2)]
        divide(tmp, n//2)
        tmp = [arr[i][:n//2] for i in range(n//2, n)]
        divide(tmp, n//2)
        tmp = [arr[i][n//2:n] for i in range(n//2)]
        divide(tmp, n//2)
        tmp = [arr[i][n//2:n] for i in range(n//2, n)]
        divide(tmp, n//2)
        
        
def solution(arr):
    global zero, one
    answer = []
    n = len(arr)
    sum = 0
    for i in arr:
        for j in i:
            sum += j
    if sum == 0:
        return [1, 0]
    elif sum == n*n:
        return [0, 1]
    
    tmp = [arr[i][:n//2] for i in range(n//2)]
    divide(tmp, n//2)
    tmp = [arr[i][:n//2] for i in range(n//2, n)]
    divide(tmp, n//2)
    tmp = [arr[i][n//2:n] for i in range(n//2)]
    divide(tmp, n//2)
    tmp = [arr[i][n//2:n] for i in range(n//2, n)]
    divide(tmp, n//2)
    return [zero, one]
