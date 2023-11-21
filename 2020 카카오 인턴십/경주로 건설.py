from collections import deque
dir = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}

def bfs(start, board):
    q = deque()
    q.append([0, 0, 0, start])
    n = len(board)
    visited = [[1e9]*n for i in range(n)]
    visited[0][0] = 0
    while q:
        x, y, cost, dir_idx = q.popleft()

        for i in range(4):
            nx = x+dir[i][0]
            ny = y+dir[i][1]

            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                if i == dir_idx:
                    dist = cost + 100
                else:
                    dist = cost + 600
                if dist < visited[nx][ny]:
                    visited[nx][ny] = dist
                    q.append([nx, ny,dist, i])
                    
    return visited[-1][-1]

def solution(board):
    result1 = bfs(1, board)
    result2 = bfs(2, board)
    return min(result1, result2)
