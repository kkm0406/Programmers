import heapq
def solution(n, k, enemy):
    answer = 0
    if k>=len(enemy):
        return len(enemy)
    arr = []
    sum_enemy = 0
    for item in enemy:
        heapq.heappush(arr, -item)
        sum_enemy += item
        if sum_enemy > n:
            if k == 0:
                break
            max_enemy = -heapq.heappop(arr)
            sum_enemy -= max_enemy
            k -= 1
        answer += 1
    return answer
