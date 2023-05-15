def solution(array):
    array.sort()        #.sort() 오름차순으로 배열을 정리해줌
    return array[len(array)//2]  # 배열[] 인덱스, 배열의 위치 정보값을 넣어줄 수 있음
 
