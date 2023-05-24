def solution(n_str):
    n_str = list(n_str)
    for i in range(len(n_str)):
        if n_str[i] =="0":
            n_str[i] = ""
        elif n_str[i] !="0":
            return "".join(n_str) # return을 줘버리면서 for문을 중간에 끊을 수 있다.
