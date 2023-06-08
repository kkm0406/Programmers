from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0])
    while q:
        x, cnt = q.popleft()
        if x == target:
            return cnt
        
        for i in range(len(words)):
            tmp_cnt = 0
            for j in range(len(x)):
                if words[i][j] != x[j]:
                    tmp_cnt+=1
            if tmp_cnt == 1:
                q.append([words[i], cnt+1])
    return answer
