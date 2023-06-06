from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while q:
        left, right = q[0], q[-1]
        q.pop()
        if not q:
            answer+=1
            break
        if left+right<=limit:
            q.popleft()
            answer+=1
        else:
            answer+=1
    return answer
