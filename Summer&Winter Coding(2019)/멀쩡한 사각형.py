import math
def solution(w,h):
    answer = 0
    incline = h/w
    x = min(w, h)
    y = max(w, h)
    
    if x == y:
        return sum(range(1,x))*2
    
    for i in range(1, x+1):
        tmp = math.floor(y*(x-i)/x)
        answer += tmp
        
    return answer*2
