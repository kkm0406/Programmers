import math
def solution(brown, yellow):
    answer = []
    area = brown+yellow
    size = (brown+4)//2
    for i in range(2, int(math.sqrt(area))+1):
        if area % i == 0:
            if i + area//i == size:
                print(i, area//i)
                answer = [area//i, i]
                break
    return answer
