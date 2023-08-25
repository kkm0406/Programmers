from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, board):
    n, m = len(board), len(board[0])
    visited = [[0]*m for i in range(n)]
    q = deque([[sx, sy]])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == 'G':
            return visited[x][y] - 1
        for i in range(4):
            nx, ny = x, y
            while True:
                nx = nx+dx[i]
                ny = ny+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                else:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return -1
                    
    

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                x, y = i, j
            if board[i][j] == 'G':
                ex, ey = i, j
    return bfs(x, y, board)
