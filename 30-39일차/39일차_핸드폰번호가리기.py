def solution(phone_number):
    num = len(phone_number) - 4
    return '*' * num + phone_number[num:]