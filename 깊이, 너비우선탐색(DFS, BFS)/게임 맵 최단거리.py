from collections import deque
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                if visited[nx][ny] == -1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y]+1

    return visited[n-1][m-1]
