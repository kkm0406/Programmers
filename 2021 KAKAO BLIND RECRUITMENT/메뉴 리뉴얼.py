from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        arr = []
        for order in orders:
            combs = list(combinations(sorted(order), c))
            arr += combs
        
        counter = Counter(arr).most_common()
        if len(counter) != 0 and counter[0][1] > 1:
            for key, value in counter:
                if value == counter[0][1]:
                    answer.append(''.join(key))
    
    return sorted(answer)
