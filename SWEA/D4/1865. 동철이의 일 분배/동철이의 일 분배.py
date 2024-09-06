# 순열 + 최대 확률 계산
def permutation(idx, success_rate):
    global visited, answer

    # 기저조건
    if idx == N:
        if success_rate > answer:
            answer = success_rate
        return

    if success_rate <= answer:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            permutation(idx + 1, success_rate * probability_succeed[idx][i])
            visited[i] = False


for tc in range(1, int(input()) + 1):
    # 입력
    N = int(input())
    probability_succeed = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(N)]

    # 로직
    answer = 0.0
    visited = [False] * N  # 방문기록
    permutation(0, 1.0)

    # 출력
    print(f'#{tc} {answer*100:.6f}')
