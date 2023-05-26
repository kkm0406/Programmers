def solution(s):
    answer = True
    arr = []
    for i in s:
        if not arr:
            if i == ")":
                return False
            else:
                arr.append(i)
        else:
            if arr[-1] == "(":
                if i == ")":
                    arr.pop()
                else:
                    arr.append(i)
                    
    if arr:
        return False

    return True
