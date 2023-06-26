def solution(phone_book):
    answer = True
    hash = {}
    for number in phone_book:
        hash[number] = 1
    
    for numbers in phone_book:
        string = ""
        for number in numbers:
            string+=number
            if string in hash and string !=numbers:
                return False

    return answer
