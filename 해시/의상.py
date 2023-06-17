from collections import defaultdict
def solution(clothes):
    answer = 0
    dic = defaultdict(int)
    for name, item in clothes:
        dic[item]+=1
    dic = list(dic.items())
    if len(dic) == 1:
        return dic[0][1]
    
    answer = 1
    for i in range(len(dic)):
        answer = answer*(dic[i][1]+1)


    return answer-1
