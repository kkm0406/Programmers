import heapq
def solution(cacheSize, cities):
    answer = 0
    arr = []
    if cacheSize == 0:
        return len(cities)*5
    
    for item in cities:
        city = item.lower()
        if city not in arr:
            if len(arr) < cacheSize:
                arr.append(city)
            elif len(arr) == cacheSize:
                arr.pop(0)
                arr.append(city)
            answer+=5
        else:
            arr.pop(arr.index(city))
            arr.append(city)
            answer+=1

    return answer
