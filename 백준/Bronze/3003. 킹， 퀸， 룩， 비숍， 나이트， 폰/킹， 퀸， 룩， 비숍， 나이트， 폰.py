chess_set = [1, 1, 2, 2, 2, 8]

chess_lst = list(map(int, input().split()))

[ print(i, end=' ') for i in [i-j for i, j in zip(chess_set, chess_lst) ]]