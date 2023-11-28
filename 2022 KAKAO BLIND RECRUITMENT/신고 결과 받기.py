def solution(id_list, report, k):
    answer = []
    alarm = {}
    cnt = {}
    report = list(set(report))
    for id in id_list:
        cnt[id] = 0
        alarm[id] = []
        
    for i in report:
        user, target = i.split()
        cnt[target] += 1
    
    for i in report:
        user, target = i.split()
        if cnt[target] >= k:
            alarm[user].append(target)
            
    for id in id_list:
        answer.append(len(alarm[id]))
    return answer
