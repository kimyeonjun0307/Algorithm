def solution(numbers):
    if numbers[0:3]!="zero":
        numbers = numbers.replace("zero","0")
        numbers = numbers.replace("one","1")# enumerate() 함수를 이용해서 반복, 인덱스가 0,1,2,3,4,,,식으로 되는 것을 이용하여 제로의 인덱스를 0으로 원의 인덱스를 1로 두는 형식으로 풀 수 있음
        numbers = numbers.replace("two","2")
        numbers = numbers.replace("three","3")
        numbers = numbers.replace("four","4")
        numbers = numbers.replace("five","5")
        numbers = numbers.replace("six","6")
        numbers = numbers.replace("seven","7")
        numbers = numbers.replace("eight","8")
        numbers = numbers.replace("nine","9")
    return int(numbers)
