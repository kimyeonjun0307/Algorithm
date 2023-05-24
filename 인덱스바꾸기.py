def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num2] , my_string[num1] = my_string[num1], my_string[num2] #  1,2 = 2,1라고 하면 1은 2 2는 1이 된다.
    return "".join(my_string)

