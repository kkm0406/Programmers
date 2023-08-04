def solution(rows, columns, queries):
    answer = []
    map = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            map[row][column] = num
            num += 1
            
    for query in queries:
        x1, y1, x2, y2 = query
        init = map[x1][y1]
        min_num = init
        for i in range(x1, x2):
            prev = map[i+1][y1]
            map[i][y1] = prev
            min_num = min(min_num, prev)
            
        for i in range(y1, y2):
            prev = map[x2][i+1]
            map[x2][i] = prev
            min_num = min(min_num, prev)
            
        for i in range(x2, x1, -1):
            prev = map[i-1][y2]
            map[i][y2] = prev
            min_num = min(min_num, prev)
            
        for i in range(y2, y1, -1):
            prev = map[x1][i-1]
            map[x1][i] = prev
            min_num = min(min_num, prev)
        
        map[x1][y1+1] = init
        answer.append(min_num)
                

    return answer
