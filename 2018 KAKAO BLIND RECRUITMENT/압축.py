def solution(msg):
    answer = []
    dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = []
    i = 1
    word = msg[0]
    msg = list(msg)
    
    while i<len(msg):
        word += msg[i]
        if word in dict:
            i+=1
        else:
            dict.append(word)
            index.append(dict.index(word[:-1])+1)
            word = ""
        
    index.append(dict.index(word)+1)
    return index
