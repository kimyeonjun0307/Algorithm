def solution(money):
    answer = []
    array1 = money//5500 
    array2 = money%5500
    answer.append(array1)
    answer.append(array2)
    return answer
