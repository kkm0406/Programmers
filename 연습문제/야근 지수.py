import heapq
def solution(n, works):
    answer = 0
    result = sum(works) - n
    if result <= 0:
        return 0
    q = []
    for i in works:
        heapq.heappush(q, -i)
        
    while n > 0:
        top = -1*heapq.heappop(q)
        top -= 1
        n-=1
        heapq.heappush(q, -1*top)
        
    for i in q:
        answer+=i**2
        
    return answer
