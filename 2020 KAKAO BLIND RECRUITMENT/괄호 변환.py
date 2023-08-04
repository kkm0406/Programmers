def divide(p):
    open, close = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return (p[:i+1], p[i+1:])
        
def is_balanced(u):
    st = []
    for i in u:
        if i == '(':
            st.append(i)
        else:
            if not st:
                return False
            st.pop()
    return True

def solution(p):
    if not p:
        return ""
    
    u, v = divide(p) 
    
    if is_balanced(u):
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer
