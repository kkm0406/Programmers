def solution(survey, choices):
    answer = ''
    n = len(survey)
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    
    for i in range(n):
        first, second = survey[i][0], survey[i][1]
        if 1<= choices[i] and  choices[i] <=3:
            score[first] += 4-choices[i]
        elif 5<= choices[i] and  choices[i] <=7:
            score[second] += choices[i] - 4
            
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
