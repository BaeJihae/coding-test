for tc in range(1, int(input()) + 1):
    N = int(input())
    wire_dict = {}
    A = []
    cnt = 0

    for i in range(N):
        a, b = map(int, input().split())
        wire_dict[a] = b
        A.append(a)
    
    # 정렬
    A.sort()

    # A를 탐색하며, 자기자신보다 위에 있는 전선의 짝 비교
    for i in range(N - 1):
        for j in range(i + 1, N):
            if wire_dict[A[i]] > wire_dict[A[j]]:
                cnt += 1

    print(f'#{tc} {cnt}')