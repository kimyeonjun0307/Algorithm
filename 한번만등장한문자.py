def solution(s):
    a=[]
    b=[]
    c=[]
    for i in range(len(s)):
        if s[i] not in a:
            a.append(s[i])
        elif s[i] in a:
            b.append(s[i])
    for j in range(len(a)):
        if a[j] not in b:
            c.append(a[j])
    return ''.join(sorted(c))  
