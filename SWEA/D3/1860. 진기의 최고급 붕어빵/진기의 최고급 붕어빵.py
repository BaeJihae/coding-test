# 진기의 최고급 붕어빵
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    fish_bread_stack = [0] * 11112

    for i in range(M, 11112, M):
        fish_bread_stack[i] = K


    def is_waiting():
        for t in map(int, input().split()):

            def searching():
                for j in range(t, -1, -1):
                    if fish_bread_stack[j] > 0:
                        fish_bread_stack[j] -= 1
                        return True
                return False

            if searching():
                continue
            else:
                return 'Impossible'

        return 'Possible'

    print(f'#{tc} {is_waiting()}')