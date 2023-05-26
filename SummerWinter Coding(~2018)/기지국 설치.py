import math
def solution(n, stations, w):
    answer = 0

    result = []
    for i in range(1, len(stations)):
        result.append((stations[i]-w)-(stations[i-1]+w)-1)
    result.append(stations[0]-w-1)
    result.append(n-stations[-1]-w)
    
    for i in result:
        if i>0:
            answer += math.ceil(i/(2*w+1))

    return answer
