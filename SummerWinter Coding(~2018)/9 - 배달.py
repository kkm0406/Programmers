import heapq
import sys
inf = sys.maxsize
def dijkstra(start, arr, N):
    distance = [inf]*(N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in arr[now]:
            cost = node[1]+dist
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, [cost, node[0]])
                
    return distance
             
def solution(N, road, K):
    answer = 0
    
    arr = [[] for i in range(N+1)]
    
    for i in road:
        a, b, c = i
        arr[a].append([b, c])
        arr[b].append([a, c])
        
        
    dist = dijkstra(1, arr, N)
    for i in dist:
        if i<=K:
            answer+=1


    return answer
