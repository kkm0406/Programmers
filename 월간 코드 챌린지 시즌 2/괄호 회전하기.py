def check(string):
    stack = []
    for s in string:
        if not stack:
            if s == ')' or s == '}' or s == ']':
                return False
            stack.append(s)
        else:
            if stack[-1] == '(' and s == ')':
                stack.pop()
            elif stack[-1] == '[' and s == ']':
                stack.pop()
            elif stack[-1] == '{' and s == '}':
                stack.pop()
            elif s == '[' or s == '{' or s == '(':
                stack.append(s)
            else:
                return False
    if not stack:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        string = s[i+1:]+s[:i+1]
        if check(string):
            answer+=1
    
    return answer
