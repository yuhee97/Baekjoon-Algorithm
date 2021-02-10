def solution(prices):
    lis = []
    for i in range(len(prices)):
        c = 0
        if i == len(prices) - 1:
            lis.append(c)
            break
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                c += 1
            else:
                c += 1
                break
        lis.append(c)

    return lis


lis = [4, 2, 3, 1, 2]
solution(lis)