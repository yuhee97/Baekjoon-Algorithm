def solution(a, b):
    SUM = 0
    for i in range(len(a)):
        SUM += a[i] * b[i]
    return SUM