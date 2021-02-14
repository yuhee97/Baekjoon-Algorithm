def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            SUM = 0
            SUM += (arr1[i][j] + arr2[i][j])
            answer[i].append(SUM)
    return answer
            