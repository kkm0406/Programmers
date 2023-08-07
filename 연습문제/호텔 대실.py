import heapq 
def solution(book_time):
    answer = 0
    time = []
    for start, end in book_time:
        start = list(map(int, start.split(":")))
        end = list(map(int, end.split(":")))
        time.append([start[0]*60+start[1],end[0]*60+end[1] ])
    time.sort()
    room = []
    for s, e in time:
        if not room:
            heapq.heappush(room, e)
            answer+=1
            continue
        if room[0] <= s:
            heapq.heappop(room)
        else:
            answer+=1
        heapq.heappush(room, e+10)
                
    
    return answer
