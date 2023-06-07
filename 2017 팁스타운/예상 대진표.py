import math
def solution(n,a,b):
    answer = 1
    first, second = min(a, b), max(a, b)
    if second % 2 == 0 and (second-first) == 1:
        return answer
    while True:
        answer+=1
        first = math.ceil(first/2)
        second = math.ceil(second/2)

        if second % 2 == 0 and (second-first) == 1:
            break
            
    return answer 
