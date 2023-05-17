def solution(num_list):
    answer = []
    array1 =0
    array2 = 0
    for i in range(len(num_list)):
        if num_list[i]%2 ==0:
            array1+=1
        else:
            array2+=1
    answer.append(array1)  # answer.append(array1,array2) 처럼 append로 두개를 한 번에 넣을 수 없다.
    answer.append(array2)
    return answer
