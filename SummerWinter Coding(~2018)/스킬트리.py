def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        string = ""
        for i in tree:
            if i in skill:
                string+=i
        
        if skill[:len(string)] == string:
            answer+=1
            

    return answer
