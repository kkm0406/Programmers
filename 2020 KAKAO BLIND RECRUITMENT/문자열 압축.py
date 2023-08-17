def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        string = ''
        cnt = 1
        prev = s[:i]
        
        for j in range(i, len(s), i):
            if prev == s[j:i+j]: 
                cnt += 1
            else:
                if cnt != 1:
                    string  = string + str(cnt) + prev
                else:
                    string = string + prev
                prev = s[j:i+j]
                cnt = 1
        if cnt != 1:
            string = string + str(cnt) + prev
        else:
            string = string + prev
        answer.append(len(string))
        
    return min(answer)
