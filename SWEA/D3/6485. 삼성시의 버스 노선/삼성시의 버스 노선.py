# 삼성시의 버스 노선
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stack = [0]*5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            stack[i] += 1

    P = int(input())
    print(f'#{tc}', end = ' ')
    C = []
    for _ in range(P):
        C.append(stack[int(input())])
    print(*C)