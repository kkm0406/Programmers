def solution(n):
    answer = 0
    dp = [0]*(100001)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, 100001):
        dp[i] = (dp[i-1]+dp[i-2])%1234567
        
    answer = dp[n]
    return answer
