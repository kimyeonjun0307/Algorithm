def solution(order):
    a=0
    order = str(order)
    for i in range(len(order)):
        if order[i] in ["3","6","9"]:
            a+=1
    return a

 # return order[2] 했는데 안됐음
    
    #중요!!!!  문자열로 바꾸면 인덱스가 생김, 근데 order[1]이 안됬던 이유는 테스트 2 는 order가 29423 즉 인덱스가 0에서4까지 있지만 테스트 1은 3 인덱스가 0밖에 없었기 때문에 테스트 1에서 오류가 났던 것이다.
