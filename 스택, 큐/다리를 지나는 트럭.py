from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    sum = 0
    while truck_weights:
        sum -= bridge.popleft()
        if sum + truck_weights[0] <= weight:
            sum += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
        answer+=1
            
    return answer + len(bridge)
