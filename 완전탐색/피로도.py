from itertools import permutations
def solution(k, dungeons):
    answer = -1
    perms = list(permutations(dungeons, len(dungeons)))
    for perm in perms:
        cnt = 0
        tmp = k
        for need, use in perm:
            if tmp >= need:
                tmp -= use
                cnt+=1
            else:
                break
        answer = max(answer, cnt)
            
    return answer
