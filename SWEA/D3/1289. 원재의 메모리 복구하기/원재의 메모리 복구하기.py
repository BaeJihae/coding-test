T = int(input())

for tc in range(1, T+1):
    memory_data = input()
    pre = '0'
    count = 0

    for data in memory_data:
        if data != pre:
            count += 1
            pre = data

    print(f'#{tc} {count}')