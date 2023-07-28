def f(n):
    if n % 2 == 0:
        return n+1
    else:
        y = '0'+str(format(n, 'b'))
        idx = y.rfind('0')
        y = list(y)
        y[idx], y[idx+1] = y[idx+1], y[idx]
        return int(''.join(y), 2)
        
def solution(numbers):
    answer = []    
    for num in numbers:
        answer.append(f(num))
    return answer
