a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    max_num = max(a, b, c)
    print(max_num * 100)
else:
    if a == b:
        print(a*100 + 1000)
    elif b == c:
        print(b*100 + 1000)
    else:
        print(c*100 + 1000)