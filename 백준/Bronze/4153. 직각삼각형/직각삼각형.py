while True:
    s1, s2, s3 = map(int, input().split())
    if s1 == s2 == s3 == 0:
        break
    s1, s2, s3 = sorted([s1, s2, s3])
    if s1**2 + s2**2 == s3**2:
        print('right')
    else:
        print('wrong')