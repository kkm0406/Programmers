def solution(n):
    answer = 0
    result = bin(n)[2:]
    cnt = result.count("1")
    while True:
        n = n+1
        result = bin(n)[2:]
        if result.count('1') == cnt:
            answer = n
            break

    return answer
