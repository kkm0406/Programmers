from collections import Counter
def solution(topping):
    answer = 0
    c = Counter(topping)
    b = set()
    for i in topping:
        c[i] -= 1
        b.add(i)
        if c[i] == 0:
            c.pop(i)
        if len(c) == len(b):
            answer += 1
        
    return answer
