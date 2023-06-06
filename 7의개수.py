def solution(array):
    answer = ''.join(map(str,array))#리스트를 문자열로 변환
    return list(answer).count('7')
