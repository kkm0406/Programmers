from collections import deque
def solution(elements):
    answer = 0
    size = len(elements)
    elements = deque(elements)
    result = set()
    for k in range(size):
        elements.rotate(1)
        for i in range(1, size+1):
            result.add(sum(list(elements)[:i]))
    result.add(sum(list(elements)))
            

    return len(result)
