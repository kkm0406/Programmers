cnt = 0
def dfs(depth, num, size, target, numbers):
    global cnt
    if depth == size:
        if num == target:
            cnt+=1
        return cnt
    else:
        dfs(depth+1, num-numbers[depth], size, target, numbers)
        dfs(depth+1, num+numbers[depth], size, target, numbers)

def solution(numbers, target):
    answer = 0
    size = len(numbers)
    dfs(0, 0, size, target, numbers)
    return cnt
