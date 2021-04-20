import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apple = []
for _ in range(k): 
    apple.append(list(map(int, sys.stdin.readline().split())))
    
L = int(sys.stdin.readline())
snake = deque()
for _ in range(L): 
    snake.append(list(sys.stdin.readline().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snake_move():
    stack = deque()
    stack.append([0, 0])
    c = 0; dir = 0
    
    while True:
        x = stack[-1][0]
        y = stack[-1][1]
        
        if snake and str(c) == snake[0][0]:
            direction = snake[0][1]
            snake.popleft()
            
            if direction == "D":
                dir += 1
            else:
                dir -= 1
                
            if dir < 0:
                dir = 3
            if dir > 3:
                dir = 0
         
        c += 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if 0 <= nx < n and 0 <= ny < n:
            if [nx+1, ny+1] in apple:
                stack.append([nx, ny])
                apple.remove([nx+1, ny+1])
            elif [nx, ny] in stack:
                break
            else:
                stack.popleft()
                stack.append([nx, ny])
        else:
            break
  
    return c

print(snake_move())