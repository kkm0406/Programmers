def solution(today, terms, privacies):
    answer = []
    today = today.replace(".", "")
    term = {}
    for i in terms:
        kind, period = i.split()
        term[kind] = period

    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        date = list(map(int, date.split(".")))
        
        date[1] += int(term[kind])
        if date[1] % 12 == 0:
            date[0] += date[1]//12 - 1
            date[1] = 12
        else:
            date[0] += date[1]//12
            date[1] = date[1] % 12

        date = "%04d%02d%02d" % (date[0], date[1], date[2])
        if int(date) <= int(today):
            answer.append(i+1)
            
    return sorted(answer)
