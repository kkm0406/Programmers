def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]

    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1]+dp[i-1][j])%1000000007
                
    answer = dp[n][m]
    return answer
