def solution(want, number, discount):
    answer = 0
    num = sum(number)
    for i in range(len(discount)):
        idx = i+num
        if idx<=len(discount):
            tmp = discount[i:idx]
            flag = True
            for j in range(len(want)):
                n = tmp.count(want[j])
                if n != number[j]:
                    flag = False
                    break
            if flag:
                answer+=1
                    
                
    return answer
