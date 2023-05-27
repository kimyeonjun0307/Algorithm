def solution(my_string):
    b=[]
    for i in range(len(my_string)):
        if my_string[i] not in b:
            b.append(my_string[i])
            
    return "".join(b)
