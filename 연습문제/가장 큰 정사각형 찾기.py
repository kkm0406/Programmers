def solution(board):
    answer = board[0][0]**2
    n = len(board)
    m = len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                answer = max(answer, board[i][j]**2)
    return answer
