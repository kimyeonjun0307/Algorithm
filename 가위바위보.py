def solution(rsp):
    a=[]
    list(rsp)
    for i in range(len(rsp)):
        if rsp[i] == "2":
            a.append("0")
        elif rsp[i] == "0":
            a.append("5")
        elif rsp[i]:
            a.append("2")
    return "".join(a)
