# 신뢰

for tc in range(1, int(input()) + 1):
    N, *test = input().split()
    pre_btn_O, pre_btn_B = 1, 1
    pre_robot = ''
    answer = 0
    plus_time_B, plus_time_O = 0, 0

    for i in range(int(N)):
        robot, btn = test[i * 2], int(test[i * 2 + 1])

        if robot == 'B':
            c_time = abs(btn - pre_btn_B) + 1
            if pre_robot == 'O':
                if plus_time_O >= c_time:
                    answer += 1
                    plus_time_B = 1
                elif plus_time_O == c_time:
                    answer += 1
                    plus_time_B, plus_time_O = 1, c_time
                else:
                    answer += c_time - plus_time_O
                    plus_time_B = c_time - plus_time_O
            else:
                answer += c_time
                plus_time_B += c_time
            pre_btn_B = btn
            pre_robot = 'B'
        else:
            c_time = abs(btn - pre_btn_O) + 1
            if pre_robot == 'B':
                if plus_time_B >= c_time:
                    answer += 1
                    plus_time_O = 1
                elif plus_time_B == c_time:
                    answer += 1
                    plus_time_B, plus_time_O = c_time, 1
                else:
                    answer += c_time - plus_time_B
                    plus_time_O = c_time - plus_time_B
            else:
                answer += c_time
                plus_time_O += c_time
            pre_btn_O = btn
            pre_robot = 'O'

    print(f'#{tc} {answer}')
