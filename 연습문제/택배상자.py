from collections import deque
def solution(order):
    answer = 0
    sub = []
    idx = 0
    order = deque(order)
    size = len(order)
    while idx != size:
        sub.append(idx+1)
        while sub and sub[-1] == order[0]:
            answer +=1 
            order.popleft()
            if not order:
                break
            sub.pop()
        idx += 1

              
    
    return answer
