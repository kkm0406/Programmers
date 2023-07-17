def solution(word):
    answer = 0
    vowels = ['', 'A', 'E', 'I', 'O', 'U']
    arr = ['A', 'E', 'I', 'O', 'U']
    
    for vowel1 in vowels:
        for vowel2 in vowels:
            for vowel3 in vowels:
                for vowel4 in vowels:
                    for vowel5 in vowels:
                        arr.append(vowel1+vowel2+vowel3+vowel4+vowel5)
    arr.sort()
    arr = sorted(list(set(arr)))
    arr.pop(0)
    answer = arr.index(word)+1
    return answer
