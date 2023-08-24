from collections import deque
def solution(picks, minerals):
    answer = 0
    tool = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    value = {
        "diamond":0,
        "iron" : 1,
        "stone" : 2
    }
    
    arr = []
    minerals = minerals[:5*sum(picks)]
    q = deque(minerals)
    while q:
        dig_cnt = 0
        dia, iron, stone = 0, 0, 0
        while dig_cnt < 5:
            dig_cnt += 1
            mineral = q.popleft()
            dia += tool[0][value[mineral]]
            iron += tool[1][value[mineral]]
            stone += tool[2][value[mineral]]
            if not q:
                break
        arr.append([dia, iron, stone])
    arr.sort(key=lambda x:(x[2], x[1], x[0]))
    
    for idx, pick in enumerate(picks):
        for i in range(pick):
            if arr:
                answer += arr.pop()[idx]
            else:
                return answer
    return answer
