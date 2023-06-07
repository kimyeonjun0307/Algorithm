def solution(numbers, k):
    while k*2>len(numbers):
        for i in range(len(numbers)):
            numbers.append(numbers[i])
    return   numbers[(k-1)*2]
