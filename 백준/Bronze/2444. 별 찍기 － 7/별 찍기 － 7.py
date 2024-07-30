N = int(input())

for i in range(1, N):
    [ print(' ', end='') for _ in range(N-i)]
    [ print('*', end='') for _ in range(2*i-1)]
    print()

for i in range(N, 0, -1):
    [ print(' ', end='') for _ in range(N-i)]
    [ print('*', end='') for _ in range(2*i-1)]
    print()