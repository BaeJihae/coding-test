def inorder(c_n):
    global answer

    if c_n == 0:
        return

    inorder(left_node[c_n])
    answer.append(word_dict[c_n])
    inorder(right_node[c_n])


for tc in range(1, 11):
    N = int(input())

    word_dict = [0] * (N + 1)
    left_node = [0] * (N + 1)
    right_node = [0] * (N + 1)

    for _ in range(N):
        lst = list(input().split())
        word_dict[int(lst[0])] = lst[1]

        if len(lst) == 3:
            left_node[int(lst[0])] = int(lst[2])
        elif len(lst) == 4:
            left_node[int(lst[0])] = int(lst[2])
            right_node[int(lst[0])] = int(lst[3])

    answer = []
    inorder(1)
    print(f'#{tc}', ''.join(answer))
