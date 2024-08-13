N = int(input())
 
for i in range(1, N+1):
    cnt = 0
    for j in str(i):
        if j in ['3', '6', '9']:
            cnt += 1
 
    print('-'*cnt if cnt > 0 else i, end = ' ')