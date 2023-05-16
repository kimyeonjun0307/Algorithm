def solution(array, n):
    number = 0
    for i in range(0,len(array),1):
        if array[i] == n:
            number = number + 1   # number = number + 1  쌓아올리는 식으로 저장가능
    return number
