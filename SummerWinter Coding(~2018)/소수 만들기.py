cnt = 0
from itertools import combinations

def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))
    for comb in combs:
        tmp = sum(comb)
        flag = True
        for i in range(2, tmp):
            if tmp % i==0:
                flag = False
                break
        if flag:
            answer+=1
    return answer
