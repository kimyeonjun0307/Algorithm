def solution(my_string, letter):
    number = []
    for i in range(0,len(my_string),+1):
        if my_string[i] != letter:
            number.append(my_string[i])
    return ''.join(number) # ''.join()  리스트의 요소들을 합쳐주는 명령어 ''안에 예를들어 '뷁'이라고 적혀있으면 요소뷁요소뷁요소뷁 으로 출력됨
