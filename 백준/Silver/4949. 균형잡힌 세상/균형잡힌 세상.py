while True:
    string = input()
    is_no = False
    if string == '.':
        break
    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack.pop() == '(':
                continue
            else:
                is_no = True
                break
        elif i == ']':
            if stack and stack.pop() == '[':
                continue
            else:
                is_no = True
                break

    if is_no or stack:
        print('no')
    else:
        print('yes')