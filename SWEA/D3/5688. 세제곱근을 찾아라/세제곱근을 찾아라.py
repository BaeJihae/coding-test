def find_cube_root(N):
    X = round(N ** (1 / 3))
    
    if X ** 3 == N:
        return X
    else:
        return -1


for tc in range(1, int(input()) + 1):
    N = int(input())
    result = find_cube_root(N)
    print(f'#{tc} {result}')
