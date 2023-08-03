def get_string(string):
    tmp_m = ''
    for i in range(len(string)-1):
        if string[i+1] == '#':
            tmp_m += string[i].lower()
        elif string[i] == '#':
            continue
        else:
            tmp_m += string[i]
    if string[-1] != '#':
        tmp_m += string[-1]
    return tmp_m

def solution(m, musicinfos):
    answer = []
    m = get_string(m)
    for info in musicinfos:
        s, e, name, code = info.split(',')
        s_h, s_m = map(int, s.split(":"))
        e_h, e_m = map(int, e.split(":"))
        time = (e_h-s_h)*60+(e_m-s_m)
        code = get_string(code)
        if time <= len(code):
            code = code[:time]
        else:
            new_code = ""
            while True:
                new_code += code
                if len(new_code) >= time:
                    break
            code = new_code
        if code.count(m) > 0:
            answer.append([name, time, -len(answer)])
    if not answer:
        return "(None)"
    answer.sort(key=lambda x:(x[1], x[2]))
    return answer[-1][0]
