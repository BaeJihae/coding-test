i = input
n = int(i())

score = list(map(int, i().split()))

m = max(score)

sum = 0

for i in score:
    sum += ( i / m ) * 100

print(sum/n)