def solution(n):
    answer = ''
    div = n-1
    while True:
        div, mod = divmod(div, 3)
        if mod == 0:
            answer += '1'
        elif mod == 1:
            answer += '2'
        else:
            answer += '4'
        if div == 0:
            break
        div -= 1
    return answer[::-1]
