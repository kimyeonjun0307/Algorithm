def solution(array):
    b=[]
    for i in range(0,1000,1):
        b.append(array.count(i))
    b.sort()
    if b[-1] == b[-2]:
        return -1
    for j in range(0,1000,1):
        if b[-1]==array.count(j):
            return j
