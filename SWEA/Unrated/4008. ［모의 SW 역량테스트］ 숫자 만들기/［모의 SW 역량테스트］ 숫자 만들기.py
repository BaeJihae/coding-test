# 숫자 만들기
op_list = ['+','-','*','/']

for tc in range(1, int(input())+1):
    N = int(input()) - 1
    op_count = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    
    mx, mn = -9999999, 9999999

    # 계산기
    def calculater(num1, op, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return int(num1 / num2)

    # 조합
    def combination(idx, current_result):
        global mx, mn
        
        if idx == N:
            mx = max(mx, current_result)
            mn = min(mn, current_result)
            return
        
        for i in range(4):
            if op_count[i] > 0 :
                op_count[i] -= 1
                next_result = calculater(current_result, op_list[i], num_lst[idx + 1])
                combination(idx + 1, next_result)
                op_count[i] += 1
                    
    combination(0, num_lst[0])
    
    print(f'#{tc} {mx - mn}')