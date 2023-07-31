from collections import deque
def solution(number, k):
    answer = ''
    arr = []
    for num in number:
        if not arr:
            arr.append(num)
            continue
        if k > 0:
            while arr[-1] < num:
                arr.pop()
                k-=1
                if not arr or k == 0:
                    break
        arr.append(num)
    
    if k > 0:
        arr = arr[:-k]
        return ''.join(arr)
    else:
        return ''.join(arr)
