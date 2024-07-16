number = [0] * 30

for _ in range(28):
    number[int(input())-1] = 1

for i, data in enumerate(number):
    if data == 0:
        print(i+1)