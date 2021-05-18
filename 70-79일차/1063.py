K, S, n = input().split()

alpha = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
move = {'R':[0, 1], 'L':[0, -1], 'B':[1, 0], 'T':[-1, 0], 
        'RT':[-1, 1], 'LT':[-1, -1], 'RB':[1, 1], 'LB':[1, -1]}
kx, ky = 8 - int(K[1]), alpha[K[0]]
sx, sy = 8 - int(S[1]), alpha[S[0]]

for _ in range(int(n)):
    m = input()
    if kx + move[m][0] == sx and ky + move[m][1] == sy:
        if 0 <= sx + move[m][0] < 8 and 0 <= sy + move[m][1] < 8:
            sx, sy = sx + move[m][0], sy + move[m][1]
        else:
            continue
    if 0 <= kx + move[m][0] < 8 and 0 <= ky + move[m][1] < 8:
        kx, ky = kx + move[m][0], ky + move[m][1]
        
reverse_move = dict(map(reversed, alpha.items()))

print(reverse_move[ky] + str(8 - kx))
print(reverse_move[sy] + str(8 - sx))