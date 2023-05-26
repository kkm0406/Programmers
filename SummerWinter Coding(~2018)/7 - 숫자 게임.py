from itertools import permutations
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer +=1
            B.pop(0)
        
    
    return answer
