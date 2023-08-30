def solution(name):
    answer = 0
    min_move = len(name) - 1
        
    for idx, alpha in enumerate(name):
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
        
        next = idx + 1
        
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 2*idx+len(name)-next, idx+2*(len(name)-next)])
        
    answer += min_move
        
    return answer
