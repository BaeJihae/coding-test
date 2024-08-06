# 정곤이의 단조 증가하는 수
def increase_num_max(str):
    pre = '0'
    for k in str:
        if int(pre) > int(k):
            return False
        else:
            pre = k
            continue
    return True


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    mx = -1

    for i in range(0, N-1):
        for j in range(i+1, N):
            num = num_lst[i] * num_lst[j]
            if increase_num_max(str(num)):
                if mx < num:
                    mx = num

    print(f'#{tc} {mx}')
