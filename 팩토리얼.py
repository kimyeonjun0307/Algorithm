def solution(n):
    a=1
    if  n>a:
        for j in range(1,21,1):
            a=a*j
            if a>n:
                return j-1
    elif n==a:
        return 1
            
