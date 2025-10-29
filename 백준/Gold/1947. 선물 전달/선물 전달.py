n = int(input())
f, s = 0, 1
for i in range(3, n + 1):
    c = ((i-1) * (f + s)) % 1000000000
    f, s = s, c
    
if n == 1:
    print(0)
else:
    print(s)