def solution(n):
    answer = 0
    dp = [0]*2001
    dp[1], dp[2], dp[3] = 1, 2, 3
    for i in range(4, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1234567
        
    answer = dp[n]
    return answer
