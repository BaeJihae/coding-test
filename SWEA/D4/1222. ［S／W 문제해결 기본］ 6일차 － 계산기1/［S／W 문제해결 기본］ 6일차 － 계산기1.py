# 후위 표기식으로 바꾸기
def change_to_postfix(lst):
    result = []
    stack = []

    for s in calculate:
        if s.isnumeric():
            result.append(s)
        else:
            if stack:
                result.append(stack.pop())
            stack.append(s)
    
    if stack:
        result.append(stack.pop())
    
    return result

# 후위 표기식 계산하기
def calculate_postfix(lst):
    stack = []

    for op in lst:
        if op.isnumeric():
            stack.append(op)
        elif op == '+':
            if len(stack) >= 2:
                num_1, num_2 = int(stack.pop()), int(stack.pop())
                stack.append(str( num_1 + num_2 ))
    
    return stack[0] if stack else 'error'

for tc in range(1, 11):
    N = int(input())
    calculate = list(input())
    
    postfix_lst = change_to_postfix(calculate)
    
    print(f'#{tc} {calculate_postfix(postfix_lst)}')