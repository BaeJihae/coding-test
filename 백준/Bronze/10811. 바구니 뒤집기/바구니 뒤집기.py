n, m = map(int, input().split())

ball_list = [ i+1 for i in range(n) ]

for _ in range(m):
    a, b = map(int, input().split())
    ball_list[a-1:b] = ball_list[a-1:b][::-1]

print(" ".join(map(str, ball_list)))