from collections import deque
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def solution(maps):
    answer = []
    new_map = []
    n = len(maps)
    m = len(maps[0])
    for map in maps:
        new_map.append(list(map))
    visited = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and new_map[i][j] != 'X':
                q = deque([[i, j]])
                visited[i][j] = True
                cnt = int(new_map[i][j])
                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and new_map[nx][ny] != 'X':
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            cnt += int(new_map[nx][ny])
                answer.append(cnt)
    return [-1] if not answer else sorted(answer)
