answer = 1e9
def dfs(st, cnt):
    global answer
    if st == 0:
        answer = min(answer, cnt)
        return
    move = st%10
    if move > 5:
        dfs(st//10+1, cnt+(10-move))
    elif move < 5:
        dfs(st//10, cnt+move)
    else:
        dfs(st//10+1, cnt+move)
        dfs(st//10, cnt+move)
        
def solution(storey):
    global answer
    dfs(storey, 0)
    return answer
