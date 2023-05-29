def solution(array, n):
    a=0
    b=0
    array.sort()
    for i in range(len(array)):
        if array[i] <n:
            a= array[i]
        elif array[i]==n:
            return array[i]
        elif array[i] >n:
            b= array[i]
            break
    if abs(a-n) == abs(b-n):
        return a
    elif abs(a*100-n) > abs(b*100-n):
        return a
    elif abs(a*100-n) < abs(b*100-n): # abs()는 절댓값
        return b
