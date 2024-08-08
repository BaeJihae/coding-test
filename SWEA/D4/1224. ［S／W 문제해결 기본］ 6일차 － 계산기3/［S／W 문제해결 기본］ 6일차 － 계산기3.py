# 중위 표기식을 후위 표기식으로 바꾸기
def change_to_postfix(lst):
    stack = []
    result = []

    for x in lst:
        if x.isnumeric():
            result.append(x)
        elif x == '(':
            stack.append(x)
        elif x == '*':
            if len(stack) > 0 and stack[-1] == '*':
                result.append(stack.pop())
            stack.append(x)
        elif x == '+':
            while len(stack) > 0 and stack[-1] in ('+', '*'):
                result.append(stack.pop())
            stack.append(x)
        elif x == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    
    while len(stack) > 0:
        result += stack.pop()

    return result

# 중위 표기식 계산하기
def calculate_postfix(lst):
    result = []

    for x in lst:
        if x.isnumeric():
            result.append(x)
        else:
            if len(result) >= 2:
                n1, n2 = int(result.pop()), int(result.pop())
                if x == '+':
                    result.append(str(n1 + n2))
                elif x == '*':
                    result.append(str(n1 * n2))

    return result[0] if result else 'error'

for tc in range(1, 11):
    N = int(input())
    lst = list(input())

    calculate = change_to_postfix(lst)

    print(f'#{tc} {calculate_postfix(calculate)}')