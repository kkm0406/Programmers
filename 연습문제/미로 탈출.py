from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, ex, ey, maps):
    visited = [[-1]*len(maps[0]) for i in range(len(maps))]
    q = deque([[sx, sy]])
    visited[sx][sy] = 0
    n, m = len(maps), len(maps[0])
    
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return visited[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                if maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                    
    return -1

        
    

def solution(maps):
    sx, sy = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
      
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
            if maps[i][j] == 'L':
                lx, ly = i, j
            if maps[i][j] == 'E':
                ex, ey = i, j

    answer1 = bfs(sx, sy, lx, ly, maps)
    answer2 = bfs(lx, ly, ex, ey, maps)
    
    if answer1 == -1 or answer2 == -1:
        return -1
    return answer1+answer2
