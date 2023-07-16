def solution(prices):
    answer = []
    for i in range(len(prices)-1, -1, -1):
        answer.append(i)
        
    stack = []
    for i in range(len(prices)):
        if not stack:
            stack.append(i)
        else:
            while stack:
                idx = stack[-1]
                if prices[idx] > prices[i]:
                    answer[idx] = abs(idx-i)
                    stack.pop()
                else:
                    break
            stack.append(i)
    

    return answer
