def solution(my_string):
    a=0
    list(my_string)
    for i in range(len(my_string)):
        if my_string[i] in ["1","2","3","4","5","6","7","8","9"]:
            a += int(my_string[i])
    return a

