import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    while q[0] < K:
        if len(q) < 2:
            return -1
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, first+2*second)
        answer+=1
    return answer
