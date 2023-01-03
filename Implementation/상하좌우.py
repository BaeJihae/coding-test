N = int(input())

LRUD = list(map(str, input().split()))

(x, y) = (1, 1)

for forward in LRUD:
    if forward == 'R':
        con_x, con_y = x, y + 1
    elif forward == 'L':
        con_x, con_y = x, y - 1
    elif forward == 'U':
        con_y, con_x = y, x - 1
    elif forward == 'D':
        con_y, con_x = y, x + 1
    if(0 < con_x < N+1 and 0 < con_y < N+1):
        x = con_x
        y = con_y

print(x, y)