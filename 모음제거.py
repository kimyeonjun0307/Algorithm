def solution(my_string):
    answer = ''
    array = ["a","e","i","o","u"] # 변수가 아니라 문자열로 만들어줘야함
    for i in range(len(my_string)):
        if my_string[i] in array: # in 을 쓰면 배열 안에 들어있기만 하면 true
            answer+= ''      # 리스트가 아니고 문자열일때는 append가 아니라 +=를 써야함
        else:
            answer+=my_string[i]
    return answer
                   
