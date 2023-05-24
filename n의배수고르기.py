def solution(n, numlist):
    a=[]
    for i in range(0,len(numlist),1):
        if numlist[i] % n ==0:
            a.append(numlist[i])
    return a
