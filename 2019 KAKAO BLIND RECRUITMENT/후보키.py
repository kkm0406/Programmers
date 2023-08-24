from itertools import combinations
def solution(relation):
    answer = 0
    n = len(relation)
    m = len(relation[0])
    
    combs = []
    for i in range(1, m+1):
        combs += list(combinations(range(m), i))
    
    unique = []
    for comb in combs:
        tmp = [tuple([item[i] for i in comb]) for item in relation]
        if len(set(tmp)) == n:
            unique.append(comb)
            
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                
    return len(answer)
