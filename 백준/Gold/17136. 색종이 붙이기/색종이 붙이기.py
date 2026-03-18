import sys
readline = sys.stdin.readline

board = [ list(map(int, readline().split())) for _ in range(10)]
answer = 26 # 색종이의 최소 개수
remain_paper = [0, 5, 5, 5, 5, 5]   # 1X1 ~ 5X5 색종이의 개수를 관리
checking_count = [(0,1), (1,1), (1,0), (0,2), (1,2), (2,2), (2,1), (2,0), (0,3), (1,3), (2,3), (3,3), (3,2), (3,1), (3,0), (0,4), (1,4), (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0)]

def checking(x, y):
    cnt = 0
    for i, j in checking_count:
        if x + i < 10 and y + j < 10 and board[x + i][y + j] == 1:
            cnt += 1
        else:
            break
    
    if cnt == 24:
        return 5
    elif cnt >= 15:
        return 4
    elif cnt >= 8:
        return 3
    elif cnt >= 3:
        return 2
    
    return 1 

def backtracking(n, depth):
    global remain_paper, answer
    
    if n == 100:
        if answer > depth:
            answer = depth
        return
    
    x, y = n // 10, n % 10
    
    if depth >= answer:
        return

    if board[x][y] == 1:
        mx = checking(x, y)
        
        for k in range(mx, 0, -1):
            if remain_paper[k] > 0:
                
                remain_paper[k] -= 1
                for i in range(k):
                    for j in range(k):
                        board[x + i][y + j] = 0
                        
                backtracking(n + 1, depth + 1)
                
                remain_paper[k] += 1
                for i in range(k):
                    for j in range(k):
                        board[x + i][y + j] = 1
    else:
        backtracking(n + 1, depth)

backtracking(0, 0)

if answer == 26:
    print(-1)
else:
    print(answer)