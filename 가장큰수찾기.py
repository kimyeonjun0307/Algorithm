def solution(array):
    big = array[0]
    for i in range(len(array)):  # 이런식으로 가장 큰 수 , 가장 작은 수를 구할 수 있다.
        if array[i] > big:
            big = array[i]
    return [big,array.index(big)] # 배열.index(찾고자하는것)  하면 찾고자하는 것의 인덱스를 알 수 있음
