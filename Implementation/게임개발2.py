n, m = map( int, input().split())
x, y, dir = map( int, input().split())

board = []
for i in range(n):
    board.append(list(map( int, input().split())))

stack = [ [0]*m for _ in range(n) ]
stack[x][y] = 1

def turn_left():
    global dir
    dir -= 1
    if dir == -1 :
        dir = 3

x_dir = [ -1, 0, 1, 0]
y_dir = [ 0, -1, 0, 1]

turn = 0
count = 1
while True :
    turn_left()
    dx = x + x_dir[dir]
    dy = y + y_dir[dir]
    if stack[dx][dy] == 0 and board[dx][dy] == 0 :
        x = dx
        y = dy
        count += 1
        stack[dx][dy] = 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        dx = x - x_dir[dir]
        dy = y - x_dir[dir]
        if stack[dx][dy] == 0 :
            x = dx
            y = dy
        else :
            break
        turn = 0

print(count)