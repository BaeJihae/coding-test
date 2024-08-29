m, n = map(int, input().split())

def decimal_to_n(val, N):
    if val == 0:
        return '0'
    result = []  # 나머지를 누적할 배열
    digit_to_alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while val != 0:
        val, remain = val // N, val % N
        result.append(digit_to_alpha[remain])

    return ''.join(result[::-1])

print(decimal_to_n(m, n))