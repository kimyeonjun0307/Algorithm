def solution(price):
    import math
    answer = 0
    if price>=100000 and price<300000:
        answer = price -price*5/100
    elif price>=300000 and price<500000:
        answer = price - price*1/10
    elif price>=500000 :
        answer = price - price*1/5
    else:
        answer = price
    return math.trunc(answer)
