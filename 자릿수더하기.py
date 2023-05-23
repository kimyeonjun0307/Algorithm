def solution(n):
    c= 0
    for i in range(1,10,1):
        if 10**i <10*n:
            a = (n%10**i-n%10**(i-1))
            c += a//(10**(i-1))
    return c
            
