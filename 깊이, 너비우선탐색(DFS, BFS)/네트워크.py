from collections import deque
def bfs(node, n, computers, visited):
    q = deque([node])
    while q:
        x = q.popleft()
        for i in range(n):
            if i == computers:
                continue
            if not visited[i] and computers[x][i] == 1:
                visited[i] = True
                q.append(i)
    
def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i, n, computers, visited)
            cnt+=1
    answer = cnt
    return answer
