def solution(s):
    answer = ''
    result = list(map(int, s.split(" ")))
    answer = str(min(result)) +" "+str(max(result))
    return answer
