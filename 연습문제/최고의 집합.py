def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    while s>0:
        answer.append(s//n)
        s -=answer[-1]
        n-=1
        
    answer = sorted(answer)
  
    return answer
