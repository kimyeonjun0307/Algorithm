def solution(my_string):
    answer=0
    a=my_string.lower()
    a=a.replace('a',' ')
    a=a.replace('b',' ')
    a=a.replace('c',' ')
    a=a.replace('d',' ')
    a=a.replace('e',' ')
    a=a.replace('f',' ')
    a=a.replace('g',' ')
    a=a.replace('h',' ')
    a=a.replace('i',' ')
    a=a.replace('j',' ')
    a=a.replace('k',' ')
    a=a.replace('l',' ')
    a=a.replace('m',' ')
    a=a.replace('n',' ')
    a=a.replace('o',' ')
    a=a.replace('p',' ')
    a=a.replace('q',' ')
    a=a.replace('r',' ')
    a=a.replace('s',' ')
    a=a.replace('t',' ')
    a=a.replace('u',' ')
    a=a.replace('v',' ')
    a=a.replace('w',' ')
    a=a.replace('x',' ')
    a=a.replace('y',' ')
    a=a.replace('z',' ')#속도를 위해 이렇게 품
    a=a.split() # 스페이스, 텝 , 엔터 기준으로 나눌려고할때는 그냥 공백으로 놔두면 됨
    for i in range(len(a)):
        answer+=int(a[i])
    return answer
:wq
