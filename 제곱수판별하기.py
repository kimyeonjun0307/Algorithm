def solution(n):
    for i in range(1,n,1):
        if n%i==0 and i*i ==n:
            return 1
    return 2
