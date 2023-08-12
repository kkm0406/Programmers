def check(arr, place):
    if not arr:
        return 1
    for x1,y1 in arr:
        for x2, y2 in arr:
            dist = abs(x1-x2)+abs(y1-y2)
            if dist > 2 or dist == 0:
                continue
            if dist == 1:
                return 0
            elif x1 == x2 and place[x1][(y1+y2)//2] != 'X':
                return 0
            elif y1 == y2 and place[(x1+x2)//2][y1] != 'X':
                return 0
            elif x1 != x2 and y1 != y2:
                if place[x1][y2] == 'P' or place[x1][y2] == 'O' or place[x2][y1] == 'P'or place[x2][y1] == 'O':
                    return 0
    return 1
    
    
def solution(places):
    answer = []
    for place in places:
        arr = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    arr.append([i, j])
        answer.append(check(arr, place))
        
    return answer
