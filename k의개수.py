def solution(i, j, k):
    a=[]
    c=0
    for i in range(i,j+1,1):
        a.append(str(i))
    a=''.join(a)
    for l in range(len(a)):
        if str(k) == a[l]:
            c+=1
    return c #   .count 를 사용하면 셀 수 있다.
