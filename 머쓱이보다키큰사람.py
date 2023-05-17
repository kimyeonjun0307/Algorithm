def solution(array, height):
    array.append(height)
    array.sort()
    answer = 0
    for i in range(len(array)):
        if array[i]>height:
            answer+=1
        else:
            answer+=0
    return answer
