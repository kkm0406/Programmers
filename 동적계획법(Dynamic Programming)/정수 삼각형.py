def solution(triangle):
    answer = 0
    size = len(triangle)
    dp = [[0]*size for i in range(size)]
    dp[0][0] = triangle[0][0]
    for i in range(1, size):
        for j in range(i+1):
            dp[i][j] = max(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])
    answer = max(dp[-1])
    return answer
