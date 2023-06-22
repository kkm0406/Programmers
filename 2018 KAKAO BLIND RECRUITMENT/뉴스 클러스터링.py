def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    arr1, arr2 = [], []
    for i in range(len(str1)-1):
        if 'a'<=str1[i]<='z' and 'a'<=str1[i+1]<='z':
            arr1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if 'a'<=str2[i]<='z' and 'a'<=str2[i+1]<='z':
            arr2.append(str2[i]+str2[i+1])
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536

    tmp1 = arr1[:] 
    intersection = []
    union = arr1[:]
    for i in arr2:
        if i not in tmp1:
            union.append(i)
        else:
            tmp1.remove(i)
            
    for i in arr2:
        if i in arr1:
            intersection.append(i)
            arr1.remove(i)
               
    answer = int(len(intersection)/len(union)*65536)
    return answer
