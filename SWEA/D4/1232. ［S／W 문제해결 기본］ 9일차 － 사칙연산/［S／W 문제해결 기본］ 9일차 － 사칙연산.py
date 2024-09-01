from collections import deque

def inorder(current_n):
    global result
    if current_n:
        inorder(left_node.get(current_n, 0))
        inorder(right_node.get(current_n, 0))
        result.append(word_dict[current_n])


def calculator(lst):
    operand = deque()
    for x in lst:
        if x in ('+', '-', '/', '*'):
            second, first = operand.pop(), operand.pop()
            if x == '+':
                operand.append(first + second)
            elif x == '-':
                operand.append(first - second)
            elif x == '*':
                operand.append(first * second)
            elif x == '/':
                operand.append(first // second)
        else:
            operand.append(int(x))
    return operand.pop()


for tc in range(1, 11):
    N = int(input())
    word_dict, left_node, right_node = {}, {}, {}

    for _ in range(N):
        lst = list(input().split())
        word_dict[int(lst[0])] = lst[1]

        if len(lst) == 4:
            left_node[int(lst[0])] = int(lst[2])
            right_node[int(lst[0])] = int(lst[3])

    result = []
    inorder(1)
    answer = calculator(result)
    print(f'#{tc}', answer)
