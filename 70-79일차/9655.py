def game(n): 
    c = 0
    while True:
        c += 1
        if n == 3 or n == 1:
            if c % 2 == 1:
                return "SK"
                break
            else:
                return "CY"
                break
        n -= 1
        
print(game(int(input())))
