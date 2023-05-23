def solution(my_string):
    a=[]
    for i in range(len(my_string)):
        if my_string[i].isupper(): # if true 면 실행, if false면 실행안함
            a.append(my_string[i].lower())
        elif my_string[i].islower():
            a.append(my_string[i].upper())
    return "".join(a)
