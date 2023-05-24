def solution(my_string):
    # d={"1":1 ,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}  []는 내장 배열 선언, {}는 딕셔너리 선언
    a=[]
    b=['1',"2","3","4","5","6","7","8","9","0"]
    c=[1,2,3,4,5,6,7,8,9,0]
    for i in range(len(my_string)):
        if my_string[i] in b:
            a.append(int(my_string[i]))
    a.sort()
    return a
