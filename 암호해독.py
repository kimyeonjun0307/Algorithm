def solution(cipher, code):
    a=[]
    array = list(cipher)
    for i in range(len(array)):
        if (i+1) %code ==0:
            a.append(cipher[i])           
    return "".join(a)
