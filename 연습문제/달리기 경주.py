def solution(players, callings):
    answer = {}
    for idx, player in enumerate(players):
        answer[player] = idx
    
    for call in callings:
        idx = answer[call]
        now, prev = players[idx], players[idx-1] 
        answer[now] -= 1
        answer[prev] += 1
        players[idx], players[idx-1]  = players[idx-1], players[idx]

    return players
