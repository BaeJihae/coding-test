n = int(input())
lst = list(map(int, input().split()))

def solution(m):
    is_prime = [True for x in range(m + 1)]
    p = 2
    while (p * p) <= m:
        if is_prime[p]:
            for i in range(p * p, m + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, m + 1) if is_prime[p]]

    return prime_numbers

answer = 0
prime_numbers_lst = solution(max(lst))

for i in lst:
    if i in prime_numbers_lst:
        answer += 1

print(answer)