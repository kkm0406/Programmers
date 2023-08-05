from itertools import permutations
import copy

def calculate(num1, op, num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    else:
        return num1*num2
    
def solution(expression):
    answer = 0
    marks = set()
    for i in expression:
        if i == '-' or i == '*' or i == '+':
            marks.add(i)
    marks = list(permutations(marks, len(marks)))  
    
    arr = []
    tmp = ""
    for i in expression:
        if i.isdigit():
            tmp+=i
        else:
            arr.append(int(tmp))
            arr.append(i)
            tmp = ""
    arr.append(int(tmp))

    for mark in marks:
        tmp_arr = copy.deepcopy(arr)
        for op in mark:
            cnts = tmp_arr.count(op)
            for _ in range(cnts):
                idx = tmp_arr.index(op)
                tmp_arr[idx] = calculate(tmp_arr[idx-1], op, tmp_arr[idx+1])
                tmp_arr.pop(idx+1)
                tmp_arr.pop(idx-1)
        answer = max(answer, abs(tmp_arr[-1]))

    return answer
