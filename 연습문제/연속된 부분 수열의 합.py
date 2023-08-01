def solution(sequence, k):
    answer = []
    dp = [0]
    for i in range(len(sequence)):
        dp.append(dp[i] + sequence[i])
    l = 0
    r = 0
    sum = 0
    while l < len(dp) and r < len(dp):
        sum = dp[r]-dp[l]
        if sum == k:
            answer.append([l, r-1])
        if sum < k:
            r += 1
        else:
            l += 1
            
    answer.sort(key=lambda x:(x[-1]-x[0], x[0]))
    return answer[0]
