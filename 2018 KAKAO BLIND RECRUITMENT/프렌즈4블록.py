def solution(m, n, board):
    answer = 0
    delete = set()
    for i in range(m):
        board[i] = list(board[i])
        
    while 1:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                target = board[i][j] 
                if board[i+1][j] == target and board[i][j+1] == target and board[i+1][j+1] == target:
                    delete.add((i+1, j))
                    delete.add((i, j+1))
                    delete.add((i+1, j+1))
                    delete.add((i, j))

        if delete:
            answer+=len(delete)
            for x, y in delete:
                board[x][y] = '0'
            delete = set()
        else:
            return answer
            
        
        while True:
            flag = True
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != '0'  and board[i+1][j] == '0':
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        flag = False
            if flag:
                break
            
