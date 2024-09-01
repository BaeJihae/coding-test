password_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    is_checking = False

    for i in range(N):
        tmp = input()
        if tmp.count('0') != M and not is_checking:
            code = tmp
            is_checking = True

    n = M - 1
    code_lst = []
    while n >= 0:
        if code[n] == '1':
            code_lst.append(password_code.get(code[n - 6:n + 1], -1))
            n -= 7
        else:
            n -= 1

    code_lst.reverse()
    odd_num = 0  # 홀수
    even_num = 0  # 짝수

    for i in range(8):
        if i % 2 == 0:
            odd_num += code_lst[i]
        else:
            even_num += code_lst[i]

    if (odd_num * 3 + even_num) % 10 == 0:
        print(f'#{tc}', sum(code_lst))
    else:
        print(f'#{tc}', 0)