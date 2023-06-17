def solution(s):
    answer = []
    s = s[1:-1]
    s.replace("{", "")
    s = s[1:-1]
    s = s.split("},{")
    s.sort(key=lambda x:len(x))
    size = (len(s[-1])+1)//2
    for item in s:
        item = item.split(",")
        for i in item:
            if int(i) not in answer:
                answer.append(int(i))
            if len(answer) == size:
                return answer

    return answer
