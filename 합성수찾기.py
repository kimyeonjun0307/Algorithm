def solution(n):
    c=0
    for i in range(1,n+1,1):
        a=0
        for j in range(1,n+1,1):
            if i%j==0 and i>=j:
                a += 1
        if a>=3:
            c+= 1            
    return c:
