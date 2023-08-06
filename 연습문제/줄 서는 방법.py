import math          
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    k -= 1
    while nums:
        idx = k // math.factorial(n-1)
        answer.append(nums[idx])
        nums.pop(idx)
        k = k % math.factorial(n-1)
        n -= 1
    
    return answer
