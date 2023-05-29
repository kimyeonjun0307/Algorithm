def solution(emergency):
    a=[]
    b=[]
    for i in range(len(emergency)):
        a.append(emergency[i])
    a.sort() 
    for j in range(len(emergency)):
        b.append(len(emergency)-(emergency.index(a[j])))
    return b
