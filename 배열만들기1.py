def solution(n, k):
    a=[]
    for i in range(1,n+1,1):
        if i%k==0:
            a.append(i)
    return sorted(a)
