n = int(input())
lst = list(map(int, input().split()))

stack = []
answer = []

for idx, value in enumerate(lst):
    if stack == []:
        stack.append(idx)
        answer.append(0)
    else:
        while stack:
            if lst[stack[-1]] > value:
                answer.append(stack[-1] + 1)
                stack.append(idx)
                break
            else:
                stack.pop()
        else:
            stack.append(idx)
            answer.append(0)

for ans in answer:
    print(ans, end=' ')