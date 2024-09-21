# 입력
n, r, c = map(int, input().split())
answer = 0


def solution(i, j, n):
    global answer

    if n == 0:
        print(answer)
        return
    k = 2 ** (n - 1)
    if i < k and j < k:
        answer += k * k * 0
        solution(i, j, n - 1)
    elif i < k and j >= k:
        answer += k * k * 1
        solution(i, j - k, n - 1)
    elif i >= k and j < k:
        answer += k * k * 2
        solution(i - k, j, n - 1)
    elif i >= k and j >= k:
        answer += k * k * 3
        solution(i - k, j - k, n - 1)


solution(r, c, n)
