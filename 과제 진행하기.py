from collections import deque
def solution(plans):
    answer = []
    wait = []
    for i in range(len(plans)):
        time = plans[i][1].split(":")
        time = int(time[0])*60+int(time[1])
        plans[i][1] = time
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    
    for i in range(len(plans)):
        time = plans[i][1] + plans[i][2]
        if i == len(plans)-1:
            answer.append(plans[i][0])
        else:
            next_start = plans[i+1][1]
            if time > next_start:
                plans[i][2] = plans[i][2] - (plans[i+1][1] - plans[i][1])
                wait.append([plans[i][0], plans[i][2]])
            else:
                answer.append(plans[i][0])
                until_next = next_start - time
                if wait and until_next > 0:
                    tmp_arr = wait[:]
                    for idx in range(len(tmp_arr)-1, -1, -1):
                        tmp_name, tmp_play = tmp_arr[idx]
                        if tmp_play < until_next:
                            wait.pop(idx)
                            answer.append(tmp_name)
                            until_next -= tmp_play
                        elif tmp_play == until_next:
                            wait.pop(idx)
                            answer.append(tmp_name)
                            break
                        else:
                            wait[idx][1] -= until_next
                            break
                            
    for item in wait[::-1]:
        answer.append(item[0])

    return answer
