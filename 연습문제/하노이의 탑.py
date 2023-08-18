result = []
def hanoi(n, src, tmp, dst):
    global result
    if n == 1:
        result.append([src, dst])
        return
    else:
        hanoi(n-1, src, dst, tmp)
        result.append([src, dst])
        hanoi(n-1, tmp, src, dst)
        
def solution(n):
    global result
    hanoi(n, 1, 2, 3)
    print(result)
    return result
