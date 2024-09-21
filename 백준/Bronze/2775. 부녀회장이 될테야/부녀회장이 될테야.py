for _ in range(int(input())):
    k = int(input())
    n = int(input())

    lst = list(range(1, n + 1))
    for k in range(1, k):
        for i in range(1, n):
            lst[i] = lst[i - 1] + lst[i]

    print(sum(lst))