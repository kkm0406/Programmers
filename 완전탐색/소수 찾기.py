from itertools import permutations
import math
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    perms = []
    
    for i in range(1, len(numbers)+1):
        perms += list(permutations(numbers, i))
    
    perms = [int(''.join(num)) for num in perms]
    perms = set(perms)

    for perm in perms:
        if perm == 1 or perm == 0:
            continue
        if is_prime(perm):
            print(perm)
            answer+=1
    return answer
