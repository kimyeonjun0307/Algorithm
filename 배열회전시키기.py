def solution(numbers, direction):
    a=[]
    if direction=="left":
        numbers.append(numbers[0])
        return numbers[1:]
    elif direction =="right":
        a.append(numbers[-1]) ###굉장히 중요한것 immutability를 지키는 것이 좋음
        for i in range(len(numbers)-1):
            a.append(numbers[i])
        return a # 인덱스는 앞에서부터는 0,1,2,3 으로 나타냄
                                 # 슬라이싱은 사이로 위치를 나타넴 0:1 0과 1 사이
                                 # 인덱스 뒤에서부터는 -1,-2,-3,-4로 나타낼 수 있다.
