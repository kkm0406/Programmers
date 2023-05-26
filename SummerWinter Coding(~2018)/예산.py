def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        if budget - i < 0:
            break
        else:
            budget -= i
            cnt+=1
    answer = cnt
    return answer
