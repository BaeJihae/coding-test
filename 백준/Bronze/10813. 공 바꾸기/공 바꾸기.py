n, m = map(int, input().split())

ball_list = [(i+1) for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    ball_list[a-1], ball_list[b-1] = ball_list[b-1], ball_list[a-1]

for ball_num in ball_list:
    print(ball_num, end=" ")