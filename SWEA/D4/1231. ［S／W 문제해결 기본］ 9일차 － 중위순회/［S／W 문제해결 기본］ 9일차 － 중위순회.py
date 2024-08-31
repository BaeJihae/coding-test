def inorder(current_n):
    global answer
    if current_n:
        inorder(left_node[current_n])
        answer += word_dict[current_n]
        inorder(right_node[current_n])


for tc in range(1, 11):
    N = int(input())
    word_dict, left_node, right_node = [[0] * (N + 1) for _ in range(3)]

    for _ in range(N):
        lst = list(input().split())
        word_dict[int(lst[0])] = lst[1]

        if len(lst) >= 3:
            left_node[int(lst[0])] = int(lst[2])
        if len(lst) >= 4:
            right_node[int(lst[0])] = int(lst[3])

    answer = ''
    inorder(1)
    print(f'#{tc}', answer)
