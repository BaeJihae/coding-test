T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = input().split()
    lst_1, lst_2 = [], []
    stack = []

    if n % 2 == 0:
        lst_1, lst_2 = lst[:n//2], lst[n//2:]
    else:
        lst_1, lst_2 = lst[:n//2+1], lst[n//2+1:]

    for k in range(len(lst_2)):
        stack.append(lst_1[k])
        stack.append(lst_2[k])

    if len(lst_1) == n//2+1 :
        stack.append(lst_1[n//2])

    answer = ' '.join(stack)
    print(f'#{tc} {answer}')