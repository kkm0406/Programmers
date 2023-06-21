from collections import deque
def solution(priorities, location):
    answer = 0
    q = []
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    cnt = 0
    while True:
        if q[0][0] == max(q)[0]:
            cnt+=1
            if q[0][1] == location:
                return cnt
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))    
        

    return answer
