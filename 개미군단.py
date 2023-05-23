def solution(hp):
        return hp//5 + ((hp-(hp//5)*5)//3) + ((hp-(hp//5)*5)-(((hp-(hp//5)*5)//3)*3)//1)
