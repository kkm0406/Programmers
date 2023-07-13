def solution(records):
    answer = []
    users = {}
    for record in records:
        record = record.split(" ")
        if record[0] == "Enter":
            users[record[1]] = record[2]
            answer.append( [record[1], "님이 들어왔습니다."])
        elif record[0] == "Leave":
            answer.append( [record[1], "님이 나갔습니다."])
        elif record[0] == "Change":
            users[record[1]] = record[2]

    result = []
    for record in answer:
        uid, msg = record
        result.append(f"{users[uid]}"+msg)

    
    return result
