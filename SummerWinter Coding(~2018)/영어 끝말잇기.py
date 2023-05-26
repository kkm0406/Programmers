from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    result = [words[0]]
    idx = 0%n
    for i in range(1, len(words)):
        idx = (idx+1)%n
        if words[i-1][-1] != words[i][0]:
            answer = [idx+1, (i//n)+1]
            break
        else:
            if not result:
                result.append(words[i])
            else:
                if words[i] not in result:
                    result.append(words[i])
                else:
                    answer = [idx+1, (i//n)+1]
                    break
    return answer
