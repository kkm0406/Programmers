from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    num = defaultdict(int)
    for i in tangerine:
        num[i] += 1
    num = sorted(num.items(), key=lambda x:(x[1], x[0]), reverse=True)
    
    for size, cnt in num:
        if k <= 0:
            break
        k-=cnt
        answer+=1
            
    return answer
