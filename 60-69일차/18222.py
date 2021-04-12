k = int(input())
left = 1; right = 2**60; result = 0

while left < right:
    mid = (left+right)//2
    if mid < k:
        result += 1
        left = mid + 1
    else:
        right = mid 
        
print(result%2)