def solution(n):
    answer = []
    directions = ['d', 'r', 'l']
    dirs = {
        'd': (1, 0),
        'l': (-1, -1),
        'r': (0, 1)
    }
    orders = []
    idx = 0
    cnt = n
    while cnt>=1:
        orders += directions[idx]*cnt
        idx = (idx+1)%3
        cnt -= 1
    
    orders = orders[1:]
    numbers = [[0]*(n) for i in range(n)]
    sx, sy = 0, 0
    numbers[sx][sy] = 1
    for order in orders:
        dir = dirs[order]
        nx = sx + dir[0]
        ny = sy + dir[1]
        numbers[nx][ny] = numbers[sx][sy] + 1
        sx, sy = nx, ny
        
    for i in range(n):
        for j in range(n):
            if numbers[i][j] != 0:
                answer.append(numbers[i][j])
    return answer
