def solution(age):
    a=[]
                   
    if age == 0:
        return "a"
    elif age == 1:
        return "b"
    elif age == 2:
        return "c"
    elif age == 3:  
        return "d"
    elif age == 4:
        return "e"
    elif age == 5:
        return "f"
    elif age == 6:
        return "g"
    elif age == 7:
        return "h"
    elif age == 8:
        return "i"
    elif age == 9:
        return "j"
    for i in range(1,age,1): 

        if  (age%10**i)//10**(i-1) ==0 and 10**i<=10*age:
            a.append("a")
        elif (age%10**i)//10**(i-1) ==1 and 10**i<=10*age:
            a.append("b")    
        elif (age%10**i)//10**(i-1) ==2 and 10**i<=10*age:
            a.append("c")   
        elif(age%10**i)//10**(i-1) ==3and 10**i<=10*age:
            a.append("d")
        elif (age%10**i)//10**(i-1) ==4 and 10**i<=10*age:
            a.append("e")
        elif (age%10**i)//10**(i-1) ==5and 10**i<=10*age :
            a.append("f")
        elif  (age%10**i)//10**(i-1) ==6 and 10**i<=10*age:
            a.append("g")
        elif (age%10**i)//10**(i-1) ==7and 10**i<=10*age :
            a.append("h")
        elif(age%10**i)//10**(i-1) ==8 and 10**i<=10*age:
            a.append("i")
        elif  (age%10**i)//10**(i-1) ==9 and 10**i<=10*age:
            a.append("j")
  
    return "".join(a[::-1])  
