num = [i for i in range(1, 10000)]

for i in range(1, 10000):
    x = sum(list(map(int, list(str(i))))) + i
    if x in num:
        num.remove(x)
    else:
        continue
        
for n in num:
    print(n)