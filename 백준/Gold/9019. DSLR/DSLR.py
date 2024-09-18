import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def solution(A, B):
    visited = [False] * 10_000
    visited[A] = True

    q = deque([(A, '')])

    while q:
        current_A, current_cmd = q.popleft()

        if current_A == B:
            return current_cmd

        next_A = (current_A * 2) % 10_000
        if not visited[next_A]:
            visited[next_A] = True
            q.append((next_A, current_cmd + 'D'))

        next_A = (current_A - 1) % 10_000
        if not visited[next_A]:
            visited[next_A] = True
            q.append((next_A, current_cmd + 'S'))

        next_A = (current_A % 1000) * 10 + (current_A // 1000)
        if not visited[next_A]:
            visited[next_A] = True
            q.append((next_A, current_cmd + 'L'))

        next_A = current_A // 10 + 1000 * (current_A % 10)
        if not visited[next_A]:
            visited[next_A] = True
            q.append((next_A, current_cmd + 'R'))

    return []


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(''.join(solution(A, B)))
