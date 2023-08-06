from collections import deque
def check(start, end, tree):
    visited = [0 for i in range(len(tree))]
    visited[start] = 1
    cnt = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for x in tree[node]:
            if x == end:
                continue
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)
    return sum(visited[1:])

def solution(n, wires):
    answer = 1e9
    tree = [[] for i in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    for node_a, node_b in wires:
        cnt = check(node_a, node_b, tree)
        answer = min(answer, abs(cnt - (n-cnt)))
    return answer
