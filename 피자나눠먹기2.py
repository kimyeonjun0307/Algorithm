def solution(n):
    for i in range(1,1000000,1):
        if (6*i)%n == 0: #어떠한 수를 0으로 나눌 때 발생하는 오류입니다.
            return i     #ZeroDivisionError: integer division or modulo by zero
                         #ZeroDivisionError: division by zero
        
