move = {
    'U': [-1, 0],
    'D': [1, 0],
    'R': [0, 1],
    'L': [0, -1]
}
path = 0
def solution(dirs):
    answer = 0
    x, y = 0, 0
    result = set()
    for dir in dirs:
        dx, dy = move[dir]
        nx, ny = x+dx, y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            result.add((x, y, nx, ny))
            result.add((nx, ny, x, y))
            x = nx
            y = ny
    answer = len(result)//2
    
    return answer
