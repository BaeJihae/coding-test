# 게임판 크기 입력받기
n, m = map( int,input().split())
# 현재 캐릭터의 위치와 방향 입력 받기
x, y, dir = map( int, input().split())

# 북, 동, 남, 서 방향 정의
A = [ -1, 0, 1, 0]
B = [ 0, 1, 0, -1]

# 전체 맵 정보를 입력받기
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1 :
        dir = 3

# 방문한 위치 저장하는 맵 생성하여 0으로 초기화
stack = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(0)
    stack.append(line)
stack[x][y] = 1

count = 1
turn = 0
while True:
    turn_left()
    a = x + A[dir]
    b = y + B[dir]
    # 가려는 방향이 육지이고, 한번도 방문한 적이 없을 때
    if stack[a][b] == 0 and board[a][b] == 0 :
        stack[a][b] = 1
        x, y = a, b
        count += 1
        dir = (dir+1)%4
        turn = 0
        continue
    # 가려는 방향이 바다이거나 방문한 적이 있을 때
    else :
        turn += 1
    # 네 방향 모두 갈 수 없을 때
    if turn == 4:
        a = x - A[dir]
        b = y - A[dir]
        # 뒤에가 육지라면 이동하기
        if stack[a][b] == 0:
            x = a
            y = b
        # 뒤에가 바다라면 반복문 종료
        else : 
            break
        turn = 0

print( count )
