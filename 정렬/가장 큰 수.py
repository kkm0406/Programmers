def solution(numbers):
    arr = [str(num) for num in numbers]
    arr = sorted(arr, key=lambda x:x*3, reverse=True)
    return str(int(''.join(arr)))
