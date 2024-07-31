T = int(input())

dict_num = {1: 4, 2: 5, 3: 6, 4: 1, 5: 2, 6: 3}

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    sm = sum(lst)
    answer = 0

    while sm <= N:
        answer += 1
        new_lst = lst[:]
        for j in range(len(lst)):
            new_lst[j] += lst[dict_num[j+1]-1]
            new_lst[j] += lst[(j - 1) % len(lst)]
            new_lst[j] += lst[(j + 1) % len(lst)]

        sm = sum(new_lst)
        lst = new_lst[:]
    
    print(answer+1)
