def get_num(number, n):
    tmp = "0123456789ABCDEF"
    q, r = divmod(number, n)
    if q == 0:
        return tmp[r]
    else:
        return get_num(q, n)+tmp[r]
        
def solution(n, t, m, p):
    answer = ''
    num = 0
    result = ""
    while num <= t*m:
        result += str(get_num(num, n))
        num+=1

    while len(answer) < t:
        answer+=result[p-1]
        p+=m

    return answer
