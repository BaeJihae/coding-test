# 새로운 불면증 치료법
for tc in range(1, int(input()) + 1):
    N_str = input()
    N_int = int(N_str)
    num_dict = {str(i): False for i in range(10)}
    lst = []
    num = 1
    while len(lst) != 10:
        N_str = str(N_int * num)
        num += 1
        for num_chr in N_str:
            if not num_dict[num_chr]:
                lst.append(num_chr)
                num_dict[num_chr] = True

    print(f'#{tc} {N_str}')