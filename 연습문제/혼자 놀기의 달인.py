def solution(cards):
    answer = []
    visited = [False]+[False for i in range(len(cards))]

    for card in cards:
        if not visited[card]:
            arr = []
            while card not in arr:
                arr.append(card)
                card = cards[card-1]
                visited[card] = True
                
            answer.append(len(arr))
            
    if answer[0] == len(cards):
        return 0
    else:
        answer.sort(reverse=True)
        return answer[0]*answer[1]
