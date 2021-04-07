L, C = map(int, input().split())
alpha = list(input().split())

alpha.sort()

def check(password_can):
    m = 0; j = 0
    for p in password_can:
        if p in 'aeiou':
            m += 1
        else:
            j += 1
    if m > 0 and j > 1:
        return True
    return False

def password(n, a, now, i):
    if len(now) == n:
        if check(now):
            print(now)
        return
    if i == len(a):
        return 
    password(n, a, now+a[i], i+1)
    password(n, a, now, i+1)

password(L, alpha, '', 0)

