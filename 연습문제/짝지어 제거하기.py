def solution(s):
    answer = -1
    arr = []
    for i in range(0, len(s)):
        if not arr:
            arr.append(s[i])
        else:
            if arr[-1] == s[i]:
                arr.pop()
            else:
                arr.append(s[i])
    print(arr)
    if not arr:
        answer = 1
    else:
        answer = 0

    return answer
